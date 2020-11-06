# Design4Green

Voici le repository offciel de la Teaam `Green Society` (équipe 49).  
Le but de ce hackathon était de proposer une solution `Green` à un problèmes posé. Cette année le challenge proposait d'apporter une solution à l'INR (Institut Numérique Responsable) afin de pouvoir présenter les résultats de l'indice de fragilité numérique.

## Installation

Pour installer notre projet en local, nous vous conseillons d'utliser un environement virtuel python.  
Il suffit ensuite d'installer le fichier requirements.txt via la commande:  

```
pip3 install -r requirements.txt
```

Une fois l'installation terninée, vous pouvez lancer le serveur d'accès via la commande:  

```
python3 manage.py runserver
```

Vous pouvez ensuite vous amuser avec notre projet.  


### Conception Technique

Nous avons choisi d’utiliser différents langages de programmation en fonction du traitement et de la rapidité des actions que nous avions à réaliser. Les cours délais de réalisation ont également joué sur la sélection du langage principal.  
Une des autres raisons principales qui nous a motivé à sélectionner ces langages sont que les documentations sont bien fournies et accessibles. Enfin une partie des membres de m’équipe avait déjà eu l’occasion de les utiliser sur d’autres projets.
Nous nous sommes donc tournés vers le python comme langage principal. En effet, ce langage permet la réalisation de POC assez facilement. Celui-ci a été couplé à Django via Django Rest Framework en ce qui concerne le backend de notre application. En ce qui concerne la partie frontend, nous nous sommes orientés vers du VueJS avec ajout également d’HTML et de CSS pour générer des rendus PDF.  
En ce qui concerne la manière dont nous nous sommes organisés pour le développement, nous avons optés pour de l’intégration continue et de la clusterisation. Nous avons donc couplé des technologies telles que Gitlab, Github et Docker. Docker nous permettait de clusteriser l’ensemble de nos applications et de déployer des dockers spécifiques en cas de besoin. Enfin, l’utilisation de pipeline via Gitlab nous permettait de réaliser un certain nombre de tests sur nos branches de développement avant de les merger sur la branche de production. Celle-ci étant également testée lors du merge.  
Enfin, en petit bonus nous avons pu mettre en place un interaction utilisateur via un tchatbot avec la technologie Botfuel. Celle-ci nous permet de répondre à des questions simples des utilisateurs telles que leur expliquer le fonctionnement du site, les principaux critères, etc…  

### Optimisation des requêtes

Les requêtes ont été optimisées de différentes manières.  
Tout d’abord, la création d’une base de données avec diverses tables (une table région, une table département, une table commune et une table quartiers). Ainsi, les accès sont assez limités.
Ensuite, l’utilisation des frameworks cités précédemment, nous permettent d’utiliser des fonctionnalités de cache. Cela nous permet donc également de réduire le temps de calcul et par conséquent la consommation.  
Enfin nous ne proposons à l’utilisateur les recherches qu’à partir de 3 caractères ce qui permet d’éviter une surcharge de requêtes vers la BDD.  
Nous avons également mis en place de la pagination dans la BDD ce qui permet de limiter là encore la consommation nécessaire pour une requête.  

### Conception fonctionnelle

Oui, nous avons décidé de mixer Leaflet et OpenStreetmap ainsi que du GeoJSON pour produire une carte. Cette carte nous permet donc de représenter l’ensemble de nos données de manière visuelle pour l’utilisateur. Cependant, les données dépendent des cartes fournies avec ces différents moyens. Cela nous permet par contre d’obtenir une carte visuelle et interactive ce qui apporte un gros plus pour l’expérience utilisateur.  
Cette carte nous permet lors de la requête utilisateur de pouvoir zoomer sur la zone sur laquelle il porte sa recherche ce qui lui permet de se situer. De plus, cette carte nous permet de faire le lien entre le code IRIS précédemment utilisé dans les sources et une ville. Cela permet à un utilisateur qui ne connais pas le code IRIS de pouvoir quand même effectuer ses recherches.
Nous sommes conscients que l’utilisations d’une carte peut être couteux en ressources, cependant, l’expérience utilisateur doit quand même être bonne et suffisante pour lui donner envie d’utiliser le site. C’est une des raisons de notre choix.  

### Design

En ce qui concerne le design du site, nous avons choisi un style assez épuré mais qui présente sur une seule page l’ensemble des données que l’utilisateur peut obtenir.  
Il y a donc la présence des règles RGPD, il y a une légende qui explique le rôle des différents encarts présent sur le site, le champ de recherche pour l’utilisateur, l’export des résultats au format PDF, les technologies utilisées le chatbot, etc…  

### Accessibilité

Comme dit précédemment l’accessibilité du site a été optimisée afin que l’utilisateur ne soit jamais perdu. Un code couleur avec des légendes a été mis en place, un chatbot avec lequel interagir sur des questions simples/incompréhensions grâce à une intelligence artificielle.  

### Généralités

Notre site est éco-conçu by design. Dès le début et la mise en place du code nous avons optés pour une solution simple et qui puisse être maintenue dans le temps. Nous avons également utilisé les ressources mises à notre disposition telles que les vidéos YouTube et les talks afin de nous sensibiliser à de nouveaux outils afin de tester « le bilan carbone » de notre site.  
L’éco-conception a été prise en compte dès le début du Hackathon et maintenue par la suite.  
