# Description de la commande

La commande `ping` permet de mesurer le temps de latence entre le bot et le serveur Discord. Elle a été créée pour le bot Discord de [votre nom ou nom de votre serveur].

## Auteur

Cette commande a été créée par moi même.
[@BenjiPy](https://github.com/BenjiPy). 
Le code est open source et peut être utilisé gratuitement sans en faire un usage de type lucratif.

## Utilisation

Pour utiliser cette commande, il suffit d'entrer la commande `/ping` dans le chat Discord. Le bot répondra avec un message "Pong !" suivi du temps de latence en millisecondes.

## Fonctionnalités

La commande `ping` dispose des fonctionnalités suivantes :

- Mesure le temps de latence entre le bot et le serveur Discord
- Envoie un message de réponse avec le temps de latence en millisecondes

## Comment ça fonctionne

La commande `ping` utilise la méthode `latency` de l'objet `bot` pour mesurer le temps de latence entre le bot et le serveur Discord. Cette méthode renvoie le temps de latence en secondes, donc nous multiplions par 1000 pour obtenir le temps en millisecondes. Le message de réponse est alors envoyé à l'utilisateur avec le temps de latence calculé.

## Conclusion

La commande `ping` est simple mais utile pour mesurer le temps de latence entre le bot et le serveur Discord. Elle peut être utilisée pour diagnostiquer les problèmes de performance ou simplement pour s'amuser avec les membres de la communauté. La commande est facile à implémenter sur votre propre bot Discord en utilisant le code open source disponible sur mon dépôt GitHub.
