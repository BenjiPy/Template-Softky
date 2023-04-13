# Description du code

Le code présenté ici a été créé par [BenjiPy](https://github.com/BenjiPy). Il est open source et présente les fonctionnalités suivantes :

## Features

- Système de nombre limité de ticket/utilisateurs.
- Simple à implémenter sur votre bot, 2 constantes à changer.
- Commande Rapide (code factorisé)

## Comment l'utiliser

Ce code peut être utilisé pour créer un système de ticket pour contacter l'administration sur votre bot Discord. Il permet de limiter le nombre de tickets par utilisateur et est facile à implémenter. Il suffit de changer deux constantes pour personnaliser le code en fonction de vos besoins. 

## Constantes

Les constantes suivantes peuvent être modifiées :

- `MAX_TICKET_PER_USER` : le nombre maximum de tickets par utilisateur
- `CATEGORY_TICKET_ID` : l'ID de la catégorie où seront créés les tickets

## Utilisation

Une fois les constantes modifiées, la commande `ticket` permet d'ouvrir un nouveau ticket en créant un nouveau canal textuel. Si l'utilisateur a déjà atteint le nombre maximum de tickets, un message lui indique qu'il ne peut pas en créer d'autres.

## Conclusion

Ce code est facile à implémenter et peut être utilisé pour créer un système de ticket simple pour votre bot Discord. Les fonctionnalités de limitation du nombre de tickets par utilisateur et de commande rapide le rendent particulièrement utile pour les communautés de taille moyenne.
