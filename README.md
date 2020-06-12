
## MyProject

				AUTOMATISER L'INSTALLATION DE GLPI AVEC PYTHON

Pour ce projet, j'ai créé un script permettant d’automatiser des tâches d’administration. 

## SCRIPT PYTHON ET YAML

Ce script personnalisé de python fait appel au script yaml sur lequel sont stockées les commandes d'installation. 

Concernant les téléchargements, voir les liens ci-dessous.

	PRÉ-REQUIS

1. Python version 3 ou supérieur: apt install python3
2. Pip3 version 19.2.1 ou supérieur: apt install python3-pip pip3 install --upgrade pip
3. Module python yaml: apt install python3-yaml
4. Module python mysql-connector: pip3 install mysql-connector
5. Modules Python Wget: pip3 install wget
6. Importer les modules suivants dans le script python: os, sys, yaml, mysql.connector, subprocess, urllib.request, tarfile, shutil

Ces pré-requis sont nécessaires à l'exécution du script

	EXÉCUTION DU SCRIPT PYTHON

Pour lancer l'exécution du script, il faut exécuter en root la commande suivante: 

- python3 installation.py commandes.yaml

Une fois l’exécution du script terminée sans erreurs, il faut désormais ouvrir votre navigateur favori 
et taper dans la barre d’adresse l'IP de votre machine, suivie de /glpi comme ci-dessous:

- http://IP_serveur/glpi

La page d'accueil de glpi doit alors s'ouvrir.

	LANGAGE UTILISÉ

- Python3

## pyBreakDown

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

## COMMANDES GIT

	INITIALISATION DE GIT

# Identité
git config --global user.name "mon_nom"

# Adresse mail
git config --global user.email "mon_email@open-source.fr"

# Outil de l'éditeur
git config --global core.editor subl

# Diffusion de l'outil
git config --global merge.tool filemerge


# CLONER LE DÉPÔT EN LOCAL
	
git clone https://github.com/oupasbenith/MyProject.git

	
# ACTIVATION DES COULEURS
	
git config --global color.diff auto

git config --global color.status auto

git config --global color.branch auto


# CHANGER L'ÉDITEUR

git config --global core.editor notepad++

git config --global merge.tool vimdiff

	
# LISTE GLOBALE

git config --list


# STATUT DES FICHIERS

git status


# LISTER LES BRANCH

git branch -a (on au '*' sur la branche courante.)

	
# CRÉER UNE BRANCH
	
	Deux lignes: créer et basculer sur la nouvelle branch

git branch nom_de_ma_branch_nouvelle

git checkout nom_de_ma_branch_nouvelle

	Une seule ligne: créer et basculer

git checkout -b nom_de_ma_branch_nouvelle


	SUPPRIMER UNE BRANCH
	
	Si la branch est local et n'est pas créée sur le repo distant

git branch -d nom_de_ma_branch_local

	Si la branch est présente sur le repo distant

git push origin --delete nom_de_ma_branch_distante

	
# CHANGER DE BRANCH
	
git checkout nom_de_ma_branch


# FAIRE UN COMMIT

git add . (pour commiter tous les fichiers)

git add nom_du_fichier_à_commiter (pour commiter un fichier spécifique)

git commit -m "Voici ma modification sur le fichier"


# ANNULER LE DERNIER COMMIT ET MODIFSICATIONS

git reset --hard mon_dernier_commit

git push --force


# ANTIDATER UN COMMIT.

git add .

GIT_AUTHOR_DATE="2020-06-1 08:32 +100" git commit -m "Commit antidaté"


# METTRE À JOUR LE DÉPÔT LOCAL

git pull


# METTRE À JOUR LE DÉPÔT LOCAL D'UNE BRANCH SPÉCIFIQUE

git pull origin ma_branch_cible


# ENVOYER SES COMMITS VERS LE DÉPÔT DISTANT

git push


# ENVOYER SES COMMIT VERS LE DÉPÔT DISTANT SUR UNE BRANCH SPÉCIFIQUE

git push origin ma_branch_spécifique


# SUPPRIMER UN FICHIER DU RÉPERTOIRE DE TRAVAIL ET DE L'INDEX

git rm nom_du_fichier


# SUPPRIMER UN FICHIER DE L'INDEX

git rmg --cached nom_du_fichier


# VERSION DE GIT
	
git --version

git version 2.27.0.windows.1

---

## CARACTÉRISTIQUES DE GLPI:

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

	LES VERSIONS REQUISES POUR L'INSTALLATION DE GLPI

	GLPI est une application web qui nécessite :

- Pour le serveur web (Apache/2.4.38);
- Le serveur web devra supporter PHP (version: PHP 7.3.14-1);
- Pour la base de données (MariaDB --> version: 10.3.22-MariaDB).

	EXTENSIONS PHP OBLIGATOIRES:

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

	EXTENSIONS PHP OPTIONNELLES

Les extensions PHP suivantes sont requises pour des fonctionnalités annexes de GLPI :

- cli : pour utiliser PHP en ligne de commande (script, actions automatiques, entre autres) ;
- domxml : pour l’authentification utilisateur CAS ;
- imap : utilisé pour la collection des courriels ou l’authentification de l’utilisateur ;
- ldap : utiliser un répertoire LDAP pour l’authentification ;
- openssl: communications sécurisées;
- xmlrpc: utilisé par l’API XMLRPC.
- APCu: peut être utilisé - parmi d’autres - comme système de cache ; voir la configuration du cache.

---

## TÉLÉCHARGEMENT

- [Glpi](https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz)
- [FusionInventory](https://github.com/fusioninventory/fusioninventory-for-glpi/archive/glpi9.4+2.4.tar.gz)
- [Git](https://git-scm.com/download/win)	
- [GitHub](https://github.com/)
- [Git Clone](https://github.com/oupasbenith/Projet6.git)

---

## INSTALLATION 



## DOCUMENTATION

- [Openclassrooms](https://openclassrooms.com/fr)
- [Licence open-source](https://choosealicense.com/)
- [Youtube](https://www.youtube.com/watch?v=4o9qzbssfII)
- [Glpi](https://glpi-install.readthedocs.io/en/latest/index.html)

---

## CONTRIBUTEURS

- D. GOMIS <yes@darillbenith.ca>

---

## LICENSE & COPYRIGHT

D. GOMIS, étudiant Openclassrooms

Ce projet est sous [MIT License](LICENCE).

---