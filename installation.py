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
subprocess.run(data["compte"])

try:
    data["db_name"] = mysql.connector.connect(
        host="data["db_host"]",
        port="3306",
        user="data["db_user"]",
        password="data["db_userPwd"]")

    mycursor = data["db_name"].cursor()
    mycursor.execute("CREATE DATABASE data["db_name"]")

    for db in mycursor:
        os.system("db")

except mysql.Error as ErrMysql:
    print(ErrMysql)
else:
	print("Le résultat obtenu est: ", data["db_name"])
	
data["db_name"].close()

print("Connexion mysql close")

# Téléchargement de GLPI)
print("***Début téléchargement glpi***")
try:
	url = (data["url_glpi")
	filename, headers = urllib.request.urlretrieve(url, filename=data["dossier_glpi"])
except:
	print("Erreur de téléchargement glpi")
else:
	print("GLPI téléchargé")
print("Localisation des fichiers, filename")
print("Localisation des entêtes, headers")

# Décompression de glpi
print("***Début de décompression de glpi***")
try:
	my_tar1 = tarfile.open(data["dossier_glpi"])
	my_tar1.extractall(data["glpi_extr"])
except:
	print("Erreur décompression glpi")
else:
	print("Décompression terminée")
my_tar1.close()

# Déplacement de glpi dans le répertoire /html
print("***Début de déplacement de glpi dans le répertoire /html***")
try:
	shutil.move(data["glpi_mov"])
except:
	print("Erreur déplacement glpi")
else:
	print("GLPI déplacé")
print("Fin décompression de glpi")

# Droits LAMP sur les fichiers glpi
print("***Début attribution des droits au serveur LAMP sur les fichiers de glpi***")
try:
	os.system(data["chown_glpi"])
except:
	print("Erreur d'attribution des droits au serveur LAMP sur les fichiers de glpi")
else:
	print("Droits attribués au serveur LAMP pour agir sur les fichiers de glpi")

# On crée la base de donnée et le compte dans la console
print("***Début de création de la base de donnée et du compte dans la console***")
try:
	os.chdir(data["rep_console"])
	os.system(data["cmd_console"])
except:
	print("Erreur de création du compte et de la base de donnée dans la console")
else:
	print("Compte et base de donnée créés dans la console")

# Téléchargement de fusioninventory
print("***Début téléchargement fusioninventory!***")
try:
	url = (data["url_fusinv"])
	filename, headers = urllib.request.urlretrieve(url, filename=data["dossier_fusinv"])
except:
	print("Erreur téléchargement fusioninventory")
else:
	print("Fusioninventory téléchargé")
print("Localisation du fichier: ", filename)
print("Localisation des entêtes: ", headers)

# Décompression de fusioninventory
print("***Début décompression fusioninventory***")
try:
	my_tar2 = tarfile.open(data["dossier_fusinv"])
	my_tar2.extractall(data["fusinv_extr"])
except:
	print("erreur décompression fusioninventory")
else:
	print("fusioninventory décompressé")
my_tar2.close()

# Déplacement de fionsioninventory dans le répertoire /fusioninventory
print("***Début déplacement de fusioninventory dans le répertoire /fusioninventory***")
try:
	shutil.move(data["fusinv_mov"])
except:
	print("Erreur déplacement fusioninventory")
else:
	print("fusioninventory déplacé")

# Attribution des droits d'accès au serveur web sur les plugins
print("***Début d'attribution des droits d'accès au serveur web sur les plugins***")
try:
	os.system(data["chown_plugins"])
except:
	print("Erreur d'attribution des droits d'accès au serveur web sur les plugins")
else:
	print("Droits d'accès attribués au serveur web sur les plugins")
	
glpi.close()
print("***INSTALLATION GLPI TERMINEE...!!!***")