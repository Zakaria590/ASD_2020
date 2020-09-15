---------------
 tp-iterateurs
---------------
Salah Zakaria OUAICHOUCHE Groupe 3

.. toctree::
   :maxdepth: 1

   listiterator.rst

~~~~~~~~~~
Etat du TP
~~~~~~~~~~

J'ai fait tout le tp sauf la derniere question.

~~~~~~~~~~~~~~~~~~~~~~
Réponses aux questions
~~~~~~~~~~~~~~~~~~~~~~

Question 3.2.1
--------------

Les dictionnaires semblent être une réponse appropriée au problème car mutables et facilité de parcours (Et accessoirement parce que c'est déjà marqué dans le rtype des doctests).

Question 3.2.2
----------------
c'est l'ajout le 0 en tete (avant le premier element),
 print_with_iterator(l)
1
2
23
3
4
45
 print_with_iterator_reverse(l)
45
4
3
23
2
1
0
 print_with_iterator(l)
1
2
23
3
4
45
on peut remarquer la si on fait l'ajout en tete en on ne redonne pas la liste en parametre quand on fait le print_with_iterator(l) on ne peut pas voir la nouvelle tete de la liste par contre quand on fait le print_with_iterator_reverse(l) on le voit.(c'est juste une opservation de mapart).

Question 3.2.2.4
----------------

Tout dépend de comment la fonction add a été pensée initialement. Cependant, il faut prendre en compte que l'ajout à la fin, tout comme au début, ne modifie pas la tête et la queue de
Liste avec laquelle l'itérateur a été créé, entraînant des problèmes lors de l'exécution des tests (les fonctions d'impression ont pour paramètre l, qui n'est du coup plus à jour).
Pour palier à ce problème, une fonction annexe, nommée set_head_tail, a été créée, et permet de mettre à jour la liste lorsqu'un élément est ajouté en début ou fin de liste.
Cette fonction est coûteuse, mais bon.

Question 3.2.3.1
----------------

Oui, cela est compatible. Mais cette fonction n'est pas la réelle réciproque de la fonction add (add puis remove ne revient pas à la situation initiale),
et donc par conséquent supprimer l'élement qui a été retourné par l'appel à next.
L'itérateur ne change pas de position, il renvoie toujours le même précédent, mais désormais il pointe aussi vers le suivant du suivant supprimé (Ou None lorsque l'élement en queue est supprimé).
                                                                                                         
Question 3.2.4
--------------

Lors d'appels successifs à la fonction remove, tous les éléments situés à la position next de l'itérateur sont supprimés successivement. L'itérateur ne bouge pas.



