#!/usr/bin/python3 
# -*-coding:Utf-8 -*

import os, sys, yaml, mysql.connector, subprocess, urllib.request, tarfile, shutil

glpi = sys.argv[1]

def lecture_yaml(glpi):
    with open(glpi, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as ErrLectGlpi:
            print(f"*** Impossible de lire le fichier yaml : {ErrLectGlpi} ***")

if __name__ == "__main__":
    data = lecture_yaml(glpi)
	
os.system(data["mise_a_jour"])
os.system(data["install_apache2"])
os.system(data["enable_apache2"])
os.system(data["start_apache2"])
os.system(data["install_php7"])
os.system(data["install_mariadb"])

# Créationde la base de donnée et tilisateur
print("*** Début création de la base de donnée et utilisateur ***")
create_user_req = 'mysql -e "CREATE USER "' + data["db_user"] + '"@"localhost" IDENTIFIED BY \'' + data["db_userPwd"] + '\'"'
create_db_req = 'mysql -e "CREATE DATABASE '+ data["db_name"] + '"'
priv_req = 'mysql -e "GRANT ALL PRIVILEGES ON *.* TO "' + data["db_user"] + '"@"localhost" IDENTIFIED BY \'' + data["db_userPwd"] + '\'"'
try:
    os.system(create_user_req)
    os.system(create_db_req)
    os.system(priv_req)
except Exception as r:
    print(f"*** Erreur création base de donnée et user : {r} ***")
    exit(1)
else:
    print("*** Base de donnée et user créés avec succès ***")	
print("*** Connexion mysql close ***")

# Création du repertoire Downloads pour les téléchargements.
print("*** Début de la création du dossier Downloads ***")
try:
    os.chdir('/tmp/')
    os.system(data["rep_create"])
except Exception as z:
    print(f"***Erreur de création du répertoire Downloads : {z} !***")
    sys.exit(3)
else:
    print("*** Le dossier Downloads a été créé avec succès ***")

#Attribution des droits sur le répertoire /tmp/Downloads
print("*** Attribution des droits sur le répertoire temporaire ***")
try:
    os.system('chmod -R 777 /tmp/Downloads')
except Exception as g:
    print("*** Erreur d'attribution des droits sur tmp : {g} ***")
    sys.exit(4)
else:
    print("*** Droits accordés sur le dossier Downloads avec succès ***")

# Téléchargement de GLPI)
print("*** Début du téléchargement de glpi ***")
try:
    url = data['url_glpi']
    filename, headers = urllib.request.urlretrieve(data['url_glpi'], filename = data["working_folder"] + data["glpi_archive"])
except Exception as e:
    print(f"*** Erreur de téléchargement glpi : {e} ***")
    sys.exit(5)
else:
    print("*** GLPI téléchargé avec succès ***")
print("*** Localisation des fichiers: ", filename)
print("*** Localisation des entêtes: ", headers)

# Décompression de glpi
print("*** Début de la décompression de glpi ***")
try:
    my_tar1 = tarfile.open(data["working_folder"] + data["glpi_archive"])
    my_tar1.extractall(data["working_folder"])
except:
    print("*** Erreur de décompression de glpi ***")
    sys.exit(6)
else:
    print("*** La décompression glpi est terminée avec succès ***")
my_tar1.close()

# Déplacement de glpi dans le répertoire /html
print("*** Début de déplacement de glpi dans le répertoire /html ***")
try:
    shutil.move(data["working_folder"] + data["glpi_folder"], data["webroot"])
except:
    print("*** Erreur de déplacement de glpi ***")
    sys.exit(7)
else:
    print("*** GLPI déplacé avec succès ***")
print("*** Fin de la décompression de glpi ***")

# On crée la base de donnée et le compte dans la console
print("*** Début de la création de la base de donnée et du compte dans la console ***")
try:
    os.chdir(data["webroot"] + data["glpi_folder"])
    os.system('php bin/console db:install -d '+ data["db_name"] +' -u '+ data["db_user"] +' -p '+ data["db_userPwd"] +' -H localhost -P 3306 -L fr_FR -f -n')
except:
    print("*** Erreur de création du compte et de la base de donnée dans la console ***")
    sys.exit(8)
else:
    print("*** Compte et base de donnée créés dans la console avec succès ***")

# Téléchargement de fusioninventory
print("*** Début téléchargement fusioninventory ! ***")
try:
    url = data["url_fusinv"]
    filename, headers = urllib.request.urlretrieve(url, filename = data["working_folder"] + data["fusinv_archive"])
except:
    print("*** Erreur téléchargement de fusioninventory ***")
    sys.exit(9)
else:
    print("*** Fusioninventory téléchargé avec succès ***")
print("*** Localisation du fichier: ", filename)
print("*** Localisation des entêtes: ", headers)

# Décompression de fusioninventory
print("*** Début de la décompression de fusioninventory ***")
try:
    my_tar2 = tarfile.open(data["working_folder"] + data["fusinv_archive"])
    my_tar2.extractall(data["working_folder"])
except:
    print("*** Erreur décompression fusioninventory ***")
    sys.exit(10)
else:
    print("*** Fusioninventory décompressé avec succès ***")
my_tar2.close()

# Déplacement de fionsioninventory dans le répertoire /fusioninventory
print("*** Début déplacement de fusioninventory dans le répertoire /fusioninventory ***")
try:
    shutil.move(data["working_folder"] + data["fusinv_folder"], data["droit_plugins"] + data["fusinv_working_folder"])
except Exception as q:
    print(f"*** Erreur déplacement fusioninventory : {q} ***")
    sys.exit(11)
else:
    print("*** Fusioninventory déplace avec succès ***")

# Droits LAMP sur les fichiers glpi
print("*** Début d'attribution des droits au serveur LAMP sur les fichiers de glpi ***")
try:
    os.system('chown -R www-data.www-data ' + data["droit_glpi"])
except:
    print("*** Erreur d'attribution des droits au serveur LAMP sur les fichiers de glpi ***")
    sys.exit(12)
else:
    print("*** Droits attribués au serveur LAMP pour agir sur les fichiers de glpi ***")
	
print("*** INSTALLATION GLPI TERMINEE...!!! ***")