# Design4Green
[![Quality Gate Status](http://vps-2ea52359.vps.ovh.net:9000/api/project_badges/measure?project=d4g&metric=alert_status)](http://vps-2ea52359.vps.ovh.net:9000/dashboard?id=d4g) [![Pipeline status](https://gitlab.com/dadard/Design4Green/badges/master/pipeline.svg)](https://gitlab.com/dadard/Design4Green/-/commits/master)



Voici le repository officiel de la Team `Green Society` (équipe 49).  
Le but de ce hackathon était de proposer une solution `Green` à un problèmes posé. Cette année le challenge proposait d'apporter une solution à l'INR (Institut Numérique Responsable) afin de pouvoir présenter les résultats de l'indice de fragilité numérique.

## Repository
### Github
[https://github.com/Radion94200/Design4Green](https://github.com/Radion94200/Design4Green)
### Gitlab
[https://gitlab.com/dadard/Design4Green](https://gitlab.com/dadard/Design4Green)

## Installation

Pour installer notre projet en local, nous vous conseillons d'utiliser un environnement virtuel python.  
Il suffit ensuite d'installer le fichier requirements.txt via la commande:  

```bash
cd backend
pip3 install -r requirements.txt
```

Une fois l'installation terminée, vous pouvez lancer le serveur d'accès via la commande:  

```bash
python3 manage.py runserver
```

Pour installer le frontend :
```bash
cd frontend
npm install
npm run serve
```

Vous pouvez ensuite vous amuser avec notre projet.  


### Conception Technique

Nous avons choisi d’utiliser différents langages de programmation en fonction du traitement et de la rapidité des actions que nous avions à réaliser. Les cours délais de réalisation ont également joué sur la sélection du langage principal. 
Une des autres raisons principales qui nous a motivés à sélectionner ces langages sont que les documentations sont bien fournies et accessibles. Enfin une partie des membres de l’équipe avait déjà eu l’occasion de les utiliser sur d’autres projets. 
Nous nous sommes donc tournés vers le python comme langage principal. En effet, ce langage permet la réalisation de POC assez facilement. Nous avons utilisé les librairies Django et Django Rest Framework pour réaliser le backend de notre application. En ce qui concerne la partie frontend, nous nous sommes orientés vers du VueJS pour le javascript et le framework Bootstrap pour l’HTML. 
En ce qui concerne la manière dont nous nous sommes organisés pour le développement, nous avons optés pour de l’intégration continue et de la conteneurisation. A chaque mise à jour du code source de notre projet, une pipeline est déclenchée dans Gitlab. Le projet est automatiquement testé, compilé, scanné avec SonarQube et déployé sur le VPS. Le backend et le frontend tournent sur le VPS sous la forme de conteneurs. 

Enfin, en petit bonus nous avons pu mettre en place un interaction utilisateur via un ChatBot avec la technologie Botfuel. Celle-ci nous permet de répondre à des questions simples des utilisateurs telles que leur expliquer le fonctionnement du site, les principaux critères, etc… 

### Optimisation des requêtes

Les requêtes ont été optimisées de différentes manières. 
Tout d’abord, la base de données est stockée dans un fichier unique, directement sur le VPS, dans le conteneur du backend. Cela permet d’éviter des transactions via le réseau pour communiquer avec la base de données, et ainsi d'optimiser les ressources matérielles.
Ensuite, niveau backend, le serveur garde en cache les requêtes qu’il reçoit, pour éviter au maximum les transactions avec la base de données. De plus, seules les recherches pertinentes (à la taille supérieure à 3 caractères) sont envoyées à la base de données. Nous avons également mis en place de la pagination dans l’API ce qui permet de limiter là encore la consommation nécessaire pour une requête. 
Niveau frontend, le serveur Nginx est configuré pour informer le navigateur sur les différents éléments qui peuvent être mis en cache (js, css, png, jpg...). Ce serveur est aussi configuré pour compresser ces éléments. Ainsi, moins de requêtes sont effectuées vers le serveur et les transferts de données sont moindres. 

### Conception fonctionnelle

Oui, nous avons décidé d’utiliser Leaflet et OpenStreetmap ainsi que GeoJSON pour produire une carte. Nous avons remarqué que les données dépendent des cartes fournies avec ces différents moyens. Néanmoins, cela nous permet par contre d’obtenir une carte visuelle et interactive pour représenter l’ensemble de nos données ce qui apporte un gros plus pour l’expérience utilisateur. 
Cette carte nous permet lors de la requête utilisateur de pouvoir zoomer sur la zone sur laquelle il porte sa recherche ce qui lui permet de se situer. De plus, cette carte nous offre la possibilité de faire le lien entre le code IRIS précédemment utilisé dans les sources et une ville. Ainsi un utilisateur qui ne connait pas le code IRIS d’un territoire peut quand même effectuer ses recherches. 
Nous sommes conscients que l’utilisations d’une carte peut être couteux en ressources, cependant, l’expérience utilisateur doit quand même être bonne et suffisante pour lui donner envie d’utiliser le site. C’est une des raisons de notre choix. 
Il est à noter que cette carte fait uniquement le rendu geojson pour une commune, de cette manière le site et fluide et les requêtes (ainsi que les transferts de données) sont limités. 

### Design

En ce qui concerne le design du site, nous avons choisi un style assez épuré mais qui présente sur une seule page l’ensemble des données que l’utilisateur peut obtenir.  
Il y a donc la présence des règles RGPD, il y a une légende qui explique le rôle des différents encarts présent sur le site, le champ de recherche pour l’utilisateur, l’export des résultats au format PDF, les technologies utilisées le chatbot, etc… 

### Accessibilité

Comme dit précédemment l’accessibilité du site a été optimisée afin que l’utilisateur ne soit jamais perdu. Un code couleur avec des légendes a été mis en place ainsi qu’un chatbot avec lequel interagir sur des questions simples/incompréhensions grâce à une intelligence artificielle. 
Le site utilise le framework Bootstrap est par ailleurs responsive et permet donc de s’adapter aux différents affichages (affichage mobile par exemple). 

### Généralités

Notre site est éco-conçu by design. Dès le début et la mise en place du code nous avons opté pour une solution simple et qui puisse être maintenue dans le temps. Nous avons également utilisé les ressources mises à notre disposition telles que les vidéos YouTube et les talks afin de nous sensibiliser à de nouveaux outils afin de tester « le bilan carbone » de notre site. 
L’éco-conception a été prise en compte dès le début du Hackathon et maintenue par la suite. 
Nous avons utilisé les outils recommandés (GTMetrix, Ecoindex, Ecograder) pour garantir que notre site est bien éco-conçu.  
