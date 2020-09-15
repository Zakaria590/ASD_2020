
---------------
Experimentateur
---------------
Salah Zakaria OUAICHOUCHE Groupe 3

.. toctree::
   :maxdepth: 1

   experience.rst
   marker.rst
   
~~~~~~~~~~
Etat du TP
~~~~~~~~~~

Toutes les questions sont bien traités.
~~~~~~~~~~~~~~~~~~~~~~
Réponses aux questions
~~~~~~~~~~~~~~~~~~~~~~

Question 1.2.2
--------------

Pour étudier la complexité de cet algorithme, on propose de compter le nombre de comparaison effectuer pour vérifié l'existence des elements de marker dans la liste des markers positifs tel que
OP : marker.cmp(positive[position]) == 0:. avec marker c'est les elements de marker
la somme de comparaisons pour les markers positifs sera toujours 1+2+...+p. Quelque soit la répartition des markers dans les deux listes.
Question 1.2.3
--------------

Pour cette Stratigie le pire des cas et le meilleur des cas sont confondus (toujours le même nombre d'opérations OP).
On fixe la taille des tableaux "markers" et "positive". Alors il y a toujours le même nombre de marqueurs positifs et de marqueurs négatifs.
Il n'y a qu'un cas général ici.

Question 1.2.4
--------------

C1(m,p)= nombre d'opérations pour les marqueurs negatifs + nombre d'opérations pour les marqueurs positifs.

.. math:: c_{1}(m,p) = (1+2+.....+p) + (m-p)*p
>> (1+2+.....+p): correspond au nombre total de comparaisons faites pour les markers positifs.
>> (m-p)*p: correspond au nombre total de comparaisons faites pour les markers négatifs.


Question 1.3.2
--------------

Pour n et p fixés, il n'existe pas de pire de cas. Le nombre de comparaisons effectuées pour chaque marker négatif est

.. math:: \lceil \log_{2}(p)\rceil +1

Le nombre de comparaisons pour tout les markers positifs ne change pas 
quelque soit la répartition.

On peut donner la borne supérieure suivante:

.. math:: c_{2}(m,p) <= m( \lceil \log_{2}(p)\rceil +1 ) + p \log_{2}(p)

>> p \log_{2}(p): correspond au nombre total de comparaison lors du tri fusion des markers positives.
>> m( \lceil \log_{2}(p)\rceil +1 ): correspond au nombre de comparaisons effectuées pour chaque marker négatif

Question 1.4.1
--------------

La solution ici s'agit de parcourir les deux listes en parallèle (comme au tri fusion)

Question 1.4.2
--------------

Oui, le pire des cas c'est celui où les valeurs positives sont comme dans l'exemple 1. La fonction devra parcourir les deux listes.
En revanche, le meilleur des cas c'est quand les positifs sont les premiers éléments de markers(Exemple 2).

Exemple 1:
markers -> [1,2,3,4,5,6,7,...]
positifs-> [2,4,6,8,..]
--------------------------------
Exemple 2:
markers -> [1,2,3,4,5,6,7,...]
positifs-> [1,2,3,..]

La borne supérieur peut s'écrire comme:
.. math:: c_{3}(m,p) <= m+p+ p \log_{2}(p) + m \log_{2}(m)
>> m \log_{2}(m): correspond au nombre total de comparaison lors du tri fusion des markers.
>> p \log_{2}(p): correspond au nombre total de comparaison lors du tri fusion des markers positive.
>> m+p: correspond au nombre total des comparaisons(de la boucle while) dans le pire des cas(comme dans l'exemple 1)

Question 1.5.2
--------------

* Pour m=100 et p=2, la stratégie 1 est la plus performante (avec 199 comparaisons)

* Pour m=100 et p=50, la stratégie 2 est la plus performante (avec 800 comparaisons)

* La stratégie 3 est toujours moins performante que la stratégie 2 et pas toujours plus performante que la stratégie 1.

ce qui donne OP1>=OP2>=OP3


Question 1.5.6
--------------
.. image:: ../src/dix-fichiers/tp1-10.png
   :scale: 50 %
   :align: center

on remarque que lorsque la donnée m est petit, la stratégie 1 est plus performante que les autres. En revanche, quand m devient plus grand (par exemple m=100) la stratégie 3 devient plus performante, suivie de la strategie 2, enfin la strategie 1.
On peut en tirer que les comportements sont sensiblement les mêmes, pour une grande taille de donees que
v3>v2>v1 en terme d'optimalité.
