#!/usr/bin/python3 
# -*-coding:Utf-8 -*

import os, sys, yaml, mysql.connector, subprocess, urllib.request, tarfile, shutil

glpi = sys.argv[1]

def lecture_yaml(glpi):
    with open(glpi, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as ErrLectGlpi:
            print(ErrLectGlpi)

if __name__ == "__main__":
    data = lecture_yaml(glpi)
	
os.system(data["mise_a_jour"])
os.system(data["install_apache2"])
os.system(data["enable_apache2"])
os.system(data["start_apache2"])
os.system(data["install_php7"])
os.system(data["install_mariadb"])

# Création base de donnée et user
print("***Utilisation de mysql.connector***")
		# ou plus simple --> os.system(data["bd_privileges"])
os.system('mysql -e "GRANT ALL PRIVILEGES ON *.* TO  "+ data["db_user"] +"@"localhost" + IDENTIFIED BY "+ data["db_userPwd"]""')
try:
    conn = mysql.connector.connect(
        host = 'data["db_host"]',
        port = '3306',
        user = 'data["db_user"]',
		password = 'data["db_userPwd"]')

    mycursor = conn.cursor()
    mycursor.execute('CREATE DATABASE' + ' data["db_name"]')

    for db in mycursor:
        os.system("db")

except mysql.connector.Error as ErrMysql:
    print(f"***Quelque chose s'est mal passé : {ErrMysql} !")
    sys.exit(1)
else:
    print("***Pas d'erreur lors de la création de la bd***")
finally:
	if(conn.is_connected()):
		mycursor.close()
		conn.close()
print("***Connexion mysql close***")

# Création du dossier Downloads pour les téléchargements
try:
	os.chdir('/tmp/')
	os.system(data["rep_create"])
except Exception as z:
	print(f"*** Erreur de création du répertoire Downloads : {z} ! ***")
	sys.exit(2)

# Téléchargement de GLPI)
print("***Début téléchargement glpi***")
try:
    url = 'data["url_glpi"]'
    filename, headers = urllib.request.urlretrieve(url, filename = 'data["working_folder"]' + 'data["glpi_archive"]')
except Exception as e:
    print(f"***Erreur de téléchargement glpi : {e} !***")
    sys.exit(3)
else:
    print("***GLPI téléchargé***")
print("***Localisation des fichiers: ", filename)
print("***Localisation des entêtes: ", headers)

# Décompression de glpi
print("***Début de décompression de glpi***")
try:
    my_tar1 = tarfile.open('data["working_folder"]'+'data["glpi_archive"]')
    my_tar1.extractall(data["working_folder"])
except Exception as b:
    print(f"***Erreur décompression glpi : {b} !***")
    sys.exit(4)
else:
    print("***Décompression terminée***")
my_tar1.close()

# Déplacement de glpi dans le répertoire /html
print("***Début de déplacement de glpi dans le répertoire /html***")
try:
    shutil.move('data["working_folder"]'+'data["glpi_folder"],' + ' data["webroot"]')
except Exception as c:
	print(f"***Erreur déplacement glpi : {c} !***")
    sys.exit(5)
else:
    print("GLPI déplacé")
print("***Fin décompression de glpi***")

# On crée la base de donnée et le compte dans la console
print("***Début de création de la base de donnée et du compte dans la console***")
try:
    os.chdir('data["webroot"]'+'data["glpi_folder"]')
    os.system('php bin/console db:install -d' + ' data["db_name"] ' + '-u' + ' data["db_user"] ' + '-p' + ' data["db_userPwd"] ' + '-L fr_FR')
except Exception as dg:
    print(f"***Erreur de création du compte et de la base de donnée dans la console : {dg} !***")
	sys.exit(6)
else:
    print("**Compte et base de donnée créés dans la console**")

# Téléchargement de fusioninventory
print("***Début téléchargement fusioninventory!***")
try:
    url = ('data["url_fusinv"]')
    filename, headers = urllib.request.urlretrieve(url, filename = 'data["working_folder"]' + 'data["fusinv_archive"]')
except Exception as k:
    print(f"***Erreur téléchargement fusioninventory : {k} !***")
    sys.exit(7)
else:
    print("***Fusioninventory téléchargé***")
print("***Localisation du fichier: ", filename)
print("***Localisation des entêtes: ", headers)

# Décompression de fusioninventory
print("***Début décompression fusioninventory***")
try:
    my_tar2 = tarfile.open('data["working_folder"]' + 'data["fusinv_archive"]')
    my_tar2.extractall('data["working_folder"]')
except Exception as m:
    print(f"***Erreur décompression fusioninventory : {m} !***")
    sys.exit(8)
else:
    print("***Fusioninventory décompressé***")
my_tar2.close()

# Déplacement de fionsioninventory dans le répertoire /fusioninventory
print("***Début déplacement de fusioninventory dans le répertoire /fusioninventory***")
try:
    shutil.move('data["working_folder"]' + 'data["fusinv_folder"],' + ' data["webroot"]' + 'data["fusinv_working_folder"]')
except Exception as r:
    print(f"***Erreur déplacement fusioninventory : {r} !***")
    sys.exit(9)
else:
    print("***Fusioninventory déplacé***")

# Droits LAMP sur les fichiers glpi
print("***Début attribution des droits au serveur LAMP sur les fichiers de glpi***")
try:
    os.system('chown –R www-data' + 'data["webroot"]' + 'data["glpi_folder"]')
except Exception as w:
    print("**Erreur d'attribution des droits au serveur LAMP sur les fichiers de glpi**")
    sys.exit(10)
else:
    print(f"**Droits attribués au serveur LAMP pour agir sur les fichiers de glpi : {w} !**")

glpi.close()
print("***INSTALLATION GLPI TERMINEE...!!!***")

