import re
import openai
from time import time, sleep
from halo import Halo
import textwrap
import yaml


###     file operations


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)



def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()


###     API functions


def chatbot(conversation, model="gpt-4-0613", temperature=0, max_tokens=2000):
    max_retry = 7
    retry = 0
    while True:
        try:
            spinner = Halo(text='Thinking...', spinner='dots')
            spinner.start()
            
            response = openai.ChatCompletion.create(model=model, messages=conversation, temperature=temperature, max_tokens=max_tokens)
            text = response['choices'][0]['message']['content']

            spinner.stop()
            
            return text, response['usage']['total_tokens']
        except Exception as oops:
            print(f'\n\nError communicating with OpenAI: "{oops}"')
            exit(5)


def chat_print(text):
    formatted_lines = [textwrap.fill(line, width=120, initial_indent='    ', subsequent_indent='    ') for line in text.split('\n')]
    formatted_text = '\n'.join(formatted_lines)
    print('\n\n\nCHATBOT:\n\n%s' % formatted_text)


if __name__ == '__main__':
    openai.api_key = open_file('../../key_openai.txt').strip()
    
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_01_intake.md')})
    user_messages = list()
    all_messages = list()
    print('अपने लक्षणों का विवरण करें रजिस्ट्री बॉट को। अंत होने पर DONE टाइप करें।')
    
    ## INTAKE PORTION
    
    while True:
        # get user input
        text = input('\n\nPATIENT: ').strip()
        if text == 'DONE':
            break
        user_messages.append(text)
        all_messages.append('PATIENT: %s' % text)
        conversation.append({'role': 'user', 'content': text})
        response, tokens = chatbot(conversation)
        conversation.append({'role': 'assistant', 'content': response})
        all_messages.append('INTAKE: %s' % response)
        print('\n\nINTAKE: %s' % response)
    
    ## CHARTING NOTES
    
    print('\n\nआवंटन नोट जनरेट कर रहा है')
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_02_prepare_notes.md')})
    text_block = '\n\n'.join(all_messages)
    chat_log = '<<BEGIN PATIENT INTAKE CHAT>>\n\n%s\n\n<<END PATIENT INTAKE CHAT>>' % text_block
    save_file('logs/log_%s_chat.txt' % time(), chat_log)
    conversation.append({'role': 'user', 'content': chat_log})
    notes, tokens = chatbot(conversation)
    print('\n\n(हिन्दी): बातचीत का नोट संस्करण:\n\n%s' % notes)
    save_file('logs/log_%s_notes.txt' % time(), notes)
    
    ## GENERATING REPORT

    print('\n\nअनुमान रिपोर्ट उत्पन्न करना')
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_03_diagnosis.md')})
    conversation.append({'role': 'user', 'content': notes})
    report, tokens = chatbot(conversation)
    save_file('logs/log_%s_diagnosis.txt' % time(), report)
    print('\n\nअनुमान रिपोर्ट:\n\n%s' % report)

    ## CLINICAL EVALUATION

    print('\n\nक्लिनिकल मूल्यांकन के लिए तैयारी')
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_04_clinical.md')})
    conversation.append({'role': 'user', 'content': notes})
    clinical, tokens = chatbot(conversation)
    save_file('logs/log_%s_clinical.txt' % time(), clinical)
    print('\n\nनैदानिक मूल्यांकन:\n\n%s' % clinical)

    ## REFERRALS & TESTS

    print('\n\n रेफरल्स और टेस्ट जनरेट करना')
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_05_referrals.md')})
    conversation.append({'role': 'user', 'content': notes})
    referrals, tokens = chatbot(conversation)
    save_file('logs/log_%s_referrals.txt' % time(), referrals)
    print('\n\n संज्ञान और परीक्षण:\n\n%s' % referrals)
