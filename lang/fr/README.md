# MediBot - Assistant Médical Intelligent

1. Utilisateurs cibles
  a. Médecins cliniciens
  b. Infirmiers/infirmières
  c. Experts médicaux
  d. Patients

2. Fonctions principales
  2.1 Admission des patients et collecte des symptômes (Admission des patients)
    a. Pose automatique de questions pour aider les patients à décrire clairement leurs symptômes.
    b. Conversion des enregistrements de discussion en dossiers médicaux.

  2.2 Recommandations cliniques (Recommandations cliniques)
    a. Génération de diagnostics possibles ou d'orientations d'investigation en fonction des symptômes du patient et de son historique médical.
    b. Fourniture de conseils sur les examens cliniques, y compris les sens à utiliser pour les examens.

  2.3 Références et examens de suivi (Références et examens de suivi)
    a. Recommandation de références spécialisées possiblement nécessaires.
    b. Proposition d'examens de laboratoire et de tests de suivi.

  2.4 Génération de questions d'entrevue (Questions d'entrevue)
    a. Génération d'une liste de questions pour les entretiens entre le médecin et le patient.

3. Mise en œuvre technologique
  a. Utilisation de grands modèles de langage pour le traitement automatique du langage naturel et la compréhension.
  b. Intégration de bases de données médicales pour des diagnostics et des conseils plus précis.
  c. Utilisation d'algorithmes d'apprentissage automatique pour améliorer la précision des diagnostics.

4. Sécurité des données et conformité
  a. Conformité à la loi HIPAA (Health Insurance Portability and Accountability Act) des États-Unis.
  b. Stockage et transmission chiffrés des données.

5. Modèle économique
  a. Modèle d'abonnement : Les établissements de santé peuvent s'abonner mensuellement ou annuellement.
  b. Frais de service ponctuels : Pour les patients individuels ou les petites cliniques.

6. Feuille de route de développement
  a. Développement de prototypes et tests internes.
  b. Projets pilotes à petite échelle.
  c. Collecte de commentaires et optimisation.
  d. Expansion de la gamme de services.
  e. Mises à jour et optimisations continues.

# Ce n'est pas un dispositif médical. Pas pour usage médical.

Ce logiciel, trouvé sous ce dépôt et sous licence MIT, est un projet expérimental et N'EST PAS un dispositif médical. Il n'est pas destiné à être utilisé comme un dispositif médical ou comme un substitut aux conseils médicaux professionnels, au diagnostic ou au traitement.

Le logiciel est conçu pour tester la capacité de l'intelligence artificielle à effectuer l'admission des patients, à prendre des notes sur les dossiers médicaux et à offrir une aide à l'investigation et au diagnostic. Cependant, il est important de noter que ce logiciel N'A PAS été testé, validé ou approuvé par la Food and Drug Administration (FDA) ou tout autre organisme de réglementation des dispositifs médicaux.

Le logiciel est fourni "EN L'ÉTAT", sans garantie d'aucune sorte, expresse ou implicite, y compris mais sans s'y limiter aux garanties de qualité marchande, d'adéquation à un usage particulier et de non-violation. En aucun cas, les auteurs ou les détenteurs des droits d'auteur ne seront responsables de toute réclamation, dommages ou autre responsabilité, que ce soit dans le cadre d'un contrat, d'un délit ou autre, résultant de, découlant de ou en relation avec le logiciel ou son utilisation ou d'autres transactions dans le logiciel.

L'utilisation de ce logiciel est purement à des fins de recherche scientifique et ne doit pas être utilisée pour diagnostiquer ou traiter des problèmes de santé, ou pour prescrire des médicaments ou d'autres traitements. Consultez toujours l'avis de votre médecin ou d'un autre fournisseur de soins de santé qualifié pour toute question concernant un état médical. Ne négligez jamais les conseils médicaux professionnels et ne retardez pas la recherche de ces conseils en raison de quelque chose que vous avez lu ou interprété à partir du logiciel.

En utilisant ce logiciel, vous reconnaissez et acceptez que vous comprenez cet avertissement et que vous utilisez le logiciel à vos propres risques. Si vous n'êtes pas d'accord avec cet avertissement, n'utilisez pas le logiciel.

Cet avertissement peut être mis à jour de temps en temps, et il incombe à l'utilisateur de consulter et de se conformer à la version actuelle de l'avertissement.

# Comment utiliser l'application

1. Installer Python :
Si ce n'est pas déjà fait, assurez-vous d'installer Python sur votre ordinateur. Vous pouvez le télécharger depuis le site officiel de Python à l'adresse python.org.

2. Installer les bibliothèques Python :
Ouvrez votre terminal ou votre invite de commandes, accédez au répertoire de l'application et exécutez la commande suivante pour installer les bibliothèques Python requises :
'''
pip install -r requirements.txt
'''

3. Démarrer l'application :
Une fois les bibliothèques installées, vous pouvez démarrer l'application en exécutant la commande suivante dans votre terminal :
'''
cd ./lang/fr
python ./chat.py
'''

4. Répondre aux questions :
L'application vous posera des questions auxquelles vous pourrez répondre en conséquence.

5.Enregistrer les résultats :
Après avoir répondu aux questions, les résultats seront enregistrés dans le dossier ./logs du répertoire de l'application.