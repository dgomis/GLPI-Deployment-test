
![python](https://user-images.githubusercontent.com/65951138/83819422-17231080-a6ca-11ea-8c67-e5baf8268ac7.jpg)


## PROJET6

				AUTOMATISER L'INSTALLATION DE GLPI AVEC PYTHON

Dans ce projet6, il nous est demandé de créer un script permettant d’automatiser des tâches 
d’administration et de partager notre code avec la communauté sur notre répertoire personnel GitHub.

---

![git](https://user-images.githubusercontent.com/65951138/83818858-a5969280-a6c8-11ea-8679-694808d5080b.png)


GIT est un outil de gestion de versions de code dont les développeurs peuvent se servir 
afin de retrouver toutes leurs anciennes "versions". Mais Git ne permet pas uniquement cela, 
il couvre de nombreuses autres possibilités.

Il permet notamment de paralléliser plusieurs versions du même projet, par exemple, lorsqu’un 
développeur travaille sur une nouvelle fonctionnalité, mais que celle-ci ne doit pas encore être 
intégrée au logiciel/application final(e).

Git sert également de documentation complète. En effet, chaque nouvelle modification de code est 
accompagnée d’un message avec une date de modification. Au bout de plusieurs années, ces messages 
peuvent se compter en milliers et devenir des documentations très intéressantes indiquant le contexte 
dans lequel les modifications ont été effectuées. Ainsi, il est également possible de retrouver facilement 
une modification apportée ainsi que sa date.

---

![github](https://user-images.githubusercontent.com/65951138/83818666-31f48580-a6c8-11ea-8584-cc9d2a6e2fa0.png)


Pour comprendre ce qu'est GitHub et comment il fonctionne, vous devez d'abord comprendre ce qu'est Git, 
le cœur de la plate-forme Web. 

Créé par Linux dude Linus Torvalds, Git est un logiciel de contrôle de version, ce qui signifie qu'il contrôle et gère 
les mises à jour d'un projet sans écraser aucune partie du projet lui-même. 

Il a été créé par Torvalds et ses collaborateurs lors du développement du noyau Linux: si une mise à jour n'a pas 
donné les effets escomptés, vous pouvez toujours revenir en arrière et récupérer la version en cours d'exécution sans 
trop de problèmes. Dans GitHub, ces concepts et pratiques ont été poussés à l'extrême, en les appliquant à un échantillon 
beaucoup plus large et dans des environnements plus diversifiés. 

Grâce à Git, les utilisateurs de plateformes sociales créés par Tom Preston-Werner, Chris Wanstrath et PJ Hyett pourront 
travailler simultanément sur la même version du même projet sans craindre d'apporter des modifications substantielles. 
Toutes les anciennes versions seront stockées dans votre repository afin que vous puissiez les récupérer en cas de besoin. 
De plus, pour chaque utilisateur au travail, une version différente du projet sera créée afin de ne pas créer de superpositions 
ou d'écrasements gênants.

## COMMENT UTILISER GITHUB?

	CRÉER UN REPOSITORY

Un repository est généralement utilisé pour organiser un projet. Les repositorys peuvent 
contenir des dossiers et des fichiers, des images, des vidéos, des feuilles de calcul et des 
ensembles de données - tout ce qui est nécessaire pour votre projet. Il est recommandé de 
toujours inclure un fichier README ou un fichier contenant des informations sur le projet. 
Github facilite la création d'un au moment où vous créez des repositorys. Il vous offre d'autres 
options telles que l'insertion d'un fichier de licence.

	POUR CRÉER UN NOUVEAU REPOSITORY:

- En haut à droite, après vous être connecté, cliquez sur + puis sélectionnez Nouveau repository.
- Appelez votre repository XXXX.
- Rédigez une brève description.


	CRÉER UNE BRANCHE

Créer une branche est une façon de travailler sur plusieurs versions d'un projet à la fois. 
Par défaut, votre repository a une branche nommée master qui est considérée comme la dernière branche. 
Nous utilisons les branches pour expérimenter et apporter des modifications avant de les insérer dans 
la branche principale. Lorsque vous créez une branche sur le master, vous copiez ou créez une copie 
master du master. Si quelqu'un d'autre modifie le master pendant que vous travaillez sur votre branche, 
vous pouvez récupérer vos mises à jour. Les développeurs, rédacteurs et concepteurs de GITHub utilisent 
des branches pour suivre les corrections de bugs et les fonctionnalités distinctes de la production principale. 
Lorsqu'une modification est prête, ils fusionnent à partir de leur branche dans le master.

	POUR CRÉER UNE NOUVELLE BRANCHE:

- Accédez à votre nouveau repository XXXX,
- Cliquez sur le menu en haut de la liste des fichiers où vous pouvez trouver le titre: master,
- Écrivez un nom de branche, par exemple "GLPI", dans la zone de texte,
- Sélectionnez la case Créer ou appuyez sur Entrée sur le clavier.

	APPORTER DES MODIFICATIONS (commit)

Sur Github, les modifications enregistrées sont appelées commit. Chaque validation a un message de validation, 
qui est une description expliquant pourquoi une modification particulière a été apportée. 
Les messages d'engagement suivent l'historique des changements, afin que les autres contributeurs 
puissent comprendre ce que vous avez fait et pourquoi.

- Cliquez sur README.md.
- Cliquez sur l'icône en forme de crayon en haut à droite de la vue du fichier pour effectuer une modification.
- Dans l'éditeur, j'écris quelques choses.
- Écrivez un message de validation décrivant votre changement
- Cliquez sur le bouton Valider les modifications

	OUVRIR UN PULL REQUEST (extractions)

L’onglet Pull requests permet de réaliser des demandes de pull. Les demandes de pull (extractions) vous permettent 
d'informer les autres sur les modifications que vous avez appliquées à une branche d'un référentiel sur GitHub. 
Une fois qu'une demande d'extraction est ouverte, vous pouvez discuter et examiner les modifications éventuelles avec 
les collaborateurs, et ajouter des validations de suivi avant que vos modifications ne soient fusionnées dans la branche de base.
Une fois votre message rédigé, cliquez sur Create pull request!

La commande Git pull permet de télécharger les modifications qui ont eu lieu sur le dépôt distant, dans le but de les rapatrier 
sur le dépôt local. Git pull est en réalité la fusion de deux commandes Git : git merge et git fetch. Git pull va créer un nouveau 
commit de fusion comme le fait  git merge. La commande  git pull exécute d'abord git fetch qui télécharge le contenu du référentiel 
distant spécifié. Ensuite, un git merge est exécuté pour fusionner les modifications du dépôt distant et créer un nouveau commit de merge en local. 

DANS CETTE DERNIÈRE ÉTAPE, il est temps d'apporter vos modifications en les fusionnant à partir de vos 
branches dans la branche de production principale.

- Cliquez sur le bouton vert de pull request pour fusionner (merge)les modifications avec la branche principale
- Cliquez sur Confirm merge
- Continuez et supprimez la branche, après que vos modifications aient été intégrées, avec le bouton "Delete branch" en violet.

---

![glpi](https://user-images.githubusercontent.com/65951138/83818633-26a15a00-a6c8-11ea-81a1-be26d9f7815c.png)

	
	À PROPOS DE GLPI

GLPI (gestionnaire libre de parc informatique) est un logiciel qui, comme son nom l’indique, 
permet de gérer des parcs informatiques. 
GLPI est une application full-web. Cela signifie qu’elle ne s’utilise qu’au travers 
d’un navigateur web. Pour afficher le contenu de l’application dans ce navigateur, il faudra donc installer 
un serveur de pages web en charge de générer les éléments à afficher.
GLPI gère des données, celles-ci sont stockées dans une base de données. C’est le serveur web qui se charge 
d’aller lire ces données dans la base de données, de les mettre en forme et de les envoyer sur le navigateur 
de l’utilisateur. C’est également le serveur web qui récupère les données saisies par l’utilisateur dans 
les différents formulaires de l’application et qui se charge de les écrire dans la base de données.

GLPI stocke enfin dans son arborescence les fichiers que vous associez à des éléments d’inventaire ou du helpdesk. 
Là encore, l’application se charge de gérer le téléchargement des fichiers sur le serveur.
Le projet GLPI a été réalisé par l’association Indepnet. 
Ce logiciel est open-source, ce qui permet d’exécuter, modifier ou développer le code.

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

## LES VERSIONS REQUISES POUR L'INSTALLATION DE GLPI

	GLPI est une application web qui nécessite :

- Pour le serveur web (Apache/2.4.38);
- Le serveur web devra supporter PHP (version: PHP 7.3.14-1);
- Pour la base de données (MariaDB --> version: 10.3.22-MariaDB).

## EXTENSIONS PHP OBLIGATOIRES:

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

## EXTENSIONS PHP OPTIONNELLES

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

- Pour télécharger glpi, cliquez [ici](https://github.com/glpi-project/glpi/releases/download/9.4.5/glpi-9.4.5.tgz)

- Pour télécharger FusionInventory, cliquez [ici](https://github.com/fusioninventory/fusioninventory-for-glpi/archive/glpi9.4+2.4.tar.gz)

- Pour télécharger git, cliquez [ici](https://git-scm.com/download/win)
	
- Pour créer un compte sur github, cliquez [ici](https://github.com/)
	
---

## DOCUMENTATION

- Plate-forme de support pour l'installation et la configuration de glpi, git et github. Suivre cette flèche [-->](https://openclassrooms.com/fr)

- Pour obtenir la Licence MIT pour github, suivre ce [lien](https://choosealicense.com/)

---

## CONTRIBUTEURS

- Dacky GOMIS <yes@darillgomis.ca>
- Antony USÉ <hacking@tonyuse.com>

---

## LICENSE & COPYRIGHT

Dacky GOMIS, étudiant Openclassrooms

Sous licence [MIT License](LICENCE). Juin 2020

---