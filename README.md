
## MyProject

				AUTOMATISER L'INSTALLATION DE GLPI AVEC PYTHON

Pour ce projet, j'ai créé un script permettant d’automatiser des tâches d’administration de GLPI. 

### SCRIPT PYTHON

Ce script personnalisé de python fait appel au script yaml sur lequel sont stockées les commandes d'installation dans des variables. 

1. Dans la première partie du script, j'ai défini une fonction nommée "lecture_yaml" pour appeler le script yaml, le lire, afficher et exécuter son contenu.

Ensuite, à tour de rôle, le script execute les variables suivantes depuis yaml:

- mise_a_jour : Mise à jour de la liste des paquets et les paquets eux-même 
- install_apache2 : Installation de Apache2
- enable_apache2 : Activation de Apache2 : 
- start_apache2 : Redémarrage de Apache2 
- install_php7 : Installation de PHP avec les modules complémentaires pour le bon fonctionnement de GLPI 
- install_mariadb : Installation de MariaDB
2. Dans la deuxième partie, le script va créer l’utilisateur et la base de donnée qui nous permettra d’installer GLPI.
3. Dans la troisième partie, le script crée le répertoire /tmp/Downloads pour accueillir tous nos téléchargements.
4. Le script donne des droits d’accès sur le répertoire /Downloads
5. Le Script va récupérer les paquets GLPI sur le serveur miroir pour les stocker directement dans le nouveau répertoire /Downloads précédemment créé et nous affiche la localisation de ce répertoire et des entêtes.
6. Le script va ouvrir le répertoire de stockage de ces paquets pour les y décompresser,  
7. Une fois ces derniers décompressés, le script les déplace dans le répertoire /var/www/html
8. Le script va créer la base de donnée et le compte dans la console. 
9. Le script va télécharger le plugin FusionInventory sur le serveur miroir et le stocke dans le répertoire /Downloads et affiche la localisation du répertoire et des entêtes.
10. Le script décompresse les paquets téléchargés dans le répertoire /var/www/html/glpi/plugins,
11. A partir de ce dernier, le script déplace les paquets décompressés dans le répertoire /FusionInventory 
12. Pour cette dernière partie, le script attribue les droits au serveur LAMP pour agir sur les fichiers du répertoire GLPI ainsi que les droits d'accès au serveur web sur le répertoire des plugins.

---

### SCRIPT YAML

Ce script yaml sert à lister les paquets nécessaires à la mise à jour du serveur et à l'installation de GLPI.

Les variables contenues dans ce scripte stockent nos commandes.

Il est fait de sorte que toutes les modifications futures (changement de version, user, mdp,..) ne se 
feront que sur lui même et pas sur le script python.

---

### PRÉ-REQUIS

1. Python version 3 ou supérieur: apt install python3
2. Pip3 version 19.2.1 ou supérieur: apt install python3-pip pip3 install --upgrade pip
3. Module python yaml: apt install python3-yaml
4. Module python mysql-connector: pip3 install mysql-connector
5. Modules Python Wget: pip3 install wget
6. Importer les modules suivants dans le script python: os, sys, yaml, mysql.connector, subprocess, urllib.request, tarfile, shutil

Ces pré-requis sont nécessaires à l'exécution du script

---

### EXÉCUTION DU SCRIPT PYTHON

Pour lancer l'exécution du script, il faut exécuter en root la commande suivante: 

- python3 installation.py commandes.yaml

Une fois l’exécution du script terminée sans erreurs, il faut désormais ouvrir votre navigateur favori 
et taper dans la barre d’adresse l'IP de votre machine, suivie de /glpi comme ci-dessous:

- http://IP_serveur/glpi

La page d'accueil de glpi doit alors s'ouvrir.

---

	LANGAGE UTILISÉ

- Python3

---

### PyBreakDown

Afin de stopper le script en cas de rencontre d'erreurs, des breakdown ont été mis en place :

    0 : Erreur de lecture du fichier YAML
	1 : Quelque chose s'est mal passé
    2 : Erreur de création du répertoire Downloads
	3 : Erreur d'attribution des droits sur tmp
    4 : Erreur de téléchargement glpi
    5 : Erreur décompression glpi
    6 : Erreur déplacement glpi
    7 : Erreur de création du compte et de la base de donnée dans la console
    8 : Erreur téléchargement fusioninventory
    9 : Erreur décompression fusioninventory
    10 : Erreur déplacement fusioninventory
    11 : Erreur d'attribution des droits au serveur LAMP sur les fichiers de glpi

---

### VERSION DE GIT

git version 2.27.0.windows.1

---

### CARACTÉRISTIQUES DE GLPI:

- Inventaire des ordinateurs, des périphériques, des imprimantes réseau et de tous les composants 
associés via une interface, avec des outils d'inventaire tels que: FusionInventory ou OCS Inventory    
- Gestion de l'infrastructure du centre de données (DCIM)    
- Gestion du cycle de vie des articles    
- Gestion des licences (conforme ITIL)    
- Gestion de la garantie et des informations financières (bon de commande, garantie et extension, amortissement)    
- Gestion des contrats, contacts, documents liés aux articles en stock    
- Gestion des incidents, demandes, problèmes et changements    
- Base de connaissances et foire aux questions (FAQ)    
- Réservation d'actifs

De plus, GLPI prend en charge de nombreux plugins qui offrent des fonctionnalités supplémentaires.

---

### LES VERSIONS REQUISES POUR L'INSTALLATION DE GLPI

	GLPI est une application web qui nécessite :

- Pour le serveur web (Apache/2.4.38);
- Le serveur web devra supporter PHP (version: PHP 7.3.14-1);
- Pour la base de données (MariaDB --> version: 10.3.22-MariaDB).

---

### EXTENSIONS PHP OBLIGATOIRES:

Les extensions PHP suivantes sont requises pour que l’application fonctionne correctement :

- curl : pour l’authentification CAS, la vérification de la version de GLPI, la télémétrie, … ;
- fileinfo : pour obtenir des informations sur des fichiers ;
- gd : pour générer des images ;
- json : pour avoir le support du format de données JSON ;
- mbstring : gestion des caractères multi-octet ;
- mysqli : pour se connecter et interroger la base de données ;
- session : pour le support des sessions utilisateur ;
- zlib: pour activer les fonctionnalités de sauvegarde et de restauration ;
- simplexml;
- xml.

---

### EXTENSIONS PHP OPTIONNELLES

Les extensions PHP suivantes sont requises pour des fonctionnalités annexes de GLPI :

- cli : pour utiliser PHP en ligne de commande (script, actions automatiques, entre autres) ;
- domxml : pour l’authentification utilisateur CAS ;
- imap : utilisé pour la collection des courriels ou l’authentification de l’utilisateur ;
- ldap : utiliser un répertoire LDAP pour l’authentification ;
- openssl: communications sécurisées;
- xmlrpc: utilisé par l’API XMLRPC.
- APCu: peut être utilisé - parmi d’autres - comme système de cache ; voir la configuration du cache.

---

### TÉLÉCHARGEMENT

- [Glpi](https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz)
- [FusionInventory](https://github.com/fusioninventory/fusioninventory-for-glpi/archive/glpi9.4+2.4.tar.gz)
- [Git](https://git-scm.com/download/win)	
- [GitHub](https://github.com/)
- [Git Clone](https://github.com/oupasbenith/Projet6.git)

---

### DOCUMENTATION

- [Openclassrooms](https://openclassrooms.com/fr)
- [Licence open-source](https://choosealicense.com/)
- [Youtube](https://www.youtube.com/watch?v=4o9qzbssfII)
- [Glpi](https://glpi-install.readthedocs.io/en/latest/index.html)

---

### CONTRIBUTEURS

- D. GOMIS <yes@darillbenith.ca>

---

### LICENSE & COPYRIGHT

D. GOMIS, étudiant Openclassrooms

Ce projet est sous [MIT License](LICENCE).

---