---------
Quicksort
---------
Salah Zakaria OUAICHOUCHE Groupe 3
.. toctree::
   :maxdepth: 1

   modules.rst

~~~~~~~~~~
Etat du TP
~~~~~~~~~~


Décrivez ici l'état d'avancement du TP.

~~~~~~~~~~~~~~~~~~~~~~
Réponses aux questions
~~~~~~~~~~~~~~~~~~~~~~

------------------------------
2.2. Rappels sur le tri rapide
-------------------------------

Question 2.2.1
--------------

D'autres tris sur place seraient par exemple 
- le tri a bulles 
- le tri fusion  
- le tri par insertion
lorsqu'on echange deux valeurs.

Question 2.2.2
--------------
Pour partitionner un tableau sans avoir à utiliser de l'espace mémoire supplémentaire, il faut faire des échanges d'éléments.

Question 2.2.3
--------------
Afin de déterminer que le partitionnement est correctement réalisé, il faut :

1) Que la longueur des deux partitions soit égale à celle du tableau (initial) passé en paramètre.

2) Que le premier élément (le pivot) de le deuxième tableau partitionné soit strictement supérieur à tous ceux de la première tableau, mais aussi inférieur ou égal aux éléments de second.

Question 2.2.8
--------------
En prenant chaque initialisation de variable, pour la partition on a 6 unités de mémoire.On utilise donc 6 unités de mémoire pour le tri rapide.
donc on peut dire que il n'y a pas d'espace mémoire supplémentaire utilisé c'est vraiment negligable a mon avis.

-----------------------
2.3. Sélection du pivot
-----------------------
Question 2.3.1.4
--------------
On a 277 comparaisons en moyenne avec un pivot aléatoire, et 321 comparaions en moyenne quand on prend le premier élèment comme pivot.
Il est donc plus efficace de chosir un pivot aléatoire.

Question 2.3.1.5
----------------
Le nombre de comparaisons des deux choix est presque le même,
on est à une ou deux comparaisons près en moyenne.
Si n = 1, on fait 0 comparaisons
sinon
On est donc en O(n²) dans le pire des cas si on prend toujours un pivot minimum
ou maximum ce qui nous donnerait  C(n) = 1 + C(0) + C(n-1)
Dans ce cas le tri est équivalent à un tri à bulle et sa compléxité est en Θ(n²).


Question 2.3.2.1
----------------
Théoriquement, le pivot optimal est celui dont il y a autant de valeurs supérieures que de valeurs inférieures dans le tableau (à une près)

Question 2.3.2.4
----------------

.. image:: ./images/tp21.png

Voici les deux premières façons de choisir le pivot.
Le graphique suivant nous montre les 3 façons mais il y a un problème avec la
3e façon, les données devraient être en dessous des autres courbes.

.. image:: ./images/tp22.png

Le tri avec le pivot optimal est le plus efficaces en termes de comparaisons d'éléments.

Question 2.3.2.5
----------------
soit n la taille du tableau à trier
c(n) = 0 si n=1
C(n) = 1 + C(n/2) + C((n-1)/2)
La complexité en temps est O(nlog n).


Question 2.3.2.1.1
------------------
En comptant le nombre de comparaisons du choix du pivot, il vaut mieux choisir
aléatoirement le pivot (ou prendre le premier de la liste).
le tri avec ce pivot optimal n'est plus le plus efficace.