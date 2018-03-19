VizTransfert
Le projet
Ce répertoire permet à partir d'une base de données d'images contenant 3 classes différentes d'entraîner un modèle de réseaux de GAN et de générer les images sur la base de la même style par le modèle entraînée.
À partir d'une base de données contenant 3 classes d'images de tailles et de formats quelconques, on redimensionne chaque image à la taille 256x256 et on convertit en JPG. Et puis, on extrait les contours sous forme de image noir et blanc. En fin, on les combine comme le jeu de données d’entraîner et du test.
On a mis 4 dossiers dans ce répertoire :
• /google_pictures contient 3 types de images obtenu par google-scrapper.
• /data contient 3 dossiers de images de bar chart, pour entraîner le réseau de GAN, et puis tester le modèle finale.
• /pix2pix-master est ce que git pix2pix contient.
• /résultat contient le premier résultat obtenu à la base du jeu de donnée dans /data (entraîné par git pix2pix-master en batch_size=1 sur 6 images Err_G: 1.1576  Err_D: 0.5484  ErrL1: 0.0752)
À partir du dossier /data, on répartir nos images. Celui-ci sera lu pour entraîner le réseau de neurones. À la fin de l'entraînement, qui peut être plus ou moins long suivant les paramètres que vous avez choisi, le modèle est enregistré.
Il est ensuite utilisé automatiquement sur le dossier /test crée ultérieurement et en créeant un dossier results. Dans son sous-dossier latest_net_G_val, vous pouvez voir les résultats dans le web index.html.
Comme chaque variable intermédiaire est enregistrée (modèle GAN entraîné), il est possible de les réutiliser à génerer des images sans réaliser toutes les étapes.
Lancement
Afin d'installer l'ensemble des packages nécessaires au fonctionnement du script, exécuter resize.cpp pour changer la taille des images. Et puis exécuter findcontour.cpp pour extraire les contours sous forme d’image blanc et noir. Dans le terminal, créér un dossier /path/to/data avec sous-dossiers A et B. A et B doit contenir ses propres sous-dossiers train, val, test, etc. Mettre les images du style A dans /path/to/data/A/train. Mettre les images du style B dans /path/to/data/B/train. Répéter pour les autres (val, test, etc). Et puis executer la commande ci-dessous:

python combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data

Après l'exécution du script, 3 fichiers "test", “train” et “val” sont créés. Celui-ci contient le jeu de donnée pour être entraîné et testé.
En fin, on suit le lancement de git pix2pix à obtenir le résultat.
Scrapping
Nous utiliserons le script issu du git image-scrapers afin de peupler notre base de données. Celui-ci permet de récupérer des images issues de google.
Traitement d'image
Les 3 fichiers resize.cpp, findcontour.cpp et combine_A_and_B.py permettent d'effectuer un traitement préliminaire sur la base de données, ce qui nous permet d'avoir un ensemble d'images au bon format pour notre réseau de neurones. Les deux premiers peut être utilisé directement ou en changant les paramètres dans le code. Le dernier doît être utilisé selon l’implémentation au-dessus.
Auteurs
LIU Xiang
He Yitong

