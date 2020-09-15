#include <stdio.h>

#include "ArbreBinaire.h"

#define max(a,b) ((a)>(b)?(a):(b))

/* Manipulation d'arbres binaires */

Noeud_t arbre1 (void) {
  Noeud_t arbre;
  Noeud_t fils_gauche;
  Noeud_t fils_droit;
  value_t valeur_racine;
  value_t valeur_fils_gauche;
  value_t valeur_fils_droit;

  valeur_racine = 12;
  valeur_fils_gauche = 9;
  valeur_fils_droit = 8;
  arbre = CreerNoeud(valeur_racine);
  fils_gauche = CreerNoeud(valeur_fils_gauche);
  fils_droit = CreerNoeud(valeur_fils_droit);
  AjouterFilsGauche(arbre, fils_gauche);
  AjouterFilsDroit(arbre, fils_droit);
  return arbre;
}

Noeud_t arbre2 (void) {
  Noeud_t arbre, tmp;

  arbre = CreerNoeud(12);
  tmp = CreerNoeud(9);
  AjouterFilsGauche(arbre,tmp);
  AjouterFilsDroit(tmp, CreerNoeud(5));
  tmp = FilsDroit(tmp);
  AjouterFilsGauche(tmp, CreerNoeud(7));

  return arbre;
}

Noeud_t arbre3 (void) {
  Noeud_t arbre, tmp;

  arbre = CreerNoeud(12);
  tmp = CreerNoeud(9);
  AjouterFilsGauche(arbre, tmp);
  AjouterFilsGauche(tmp,CreerNoeud(1));
  AjouterFilsDroit(tmp, CreerNoeud(5));
  tmp = CreerNoeud(8);
  AjouterFilsDroit(arbre,tmp);
  AjouterFilsDroit(tmp, CreerNoeud(4));
  tmp = FilsDroit(tmp);
  AjouterFilsGauche(tmp, CreerNoeud(7));
  AjouterFilsDroit(tmp, CreerNoeud(6));

  return arbre;
}

void imprimer (Noeud_t a) {
  if(!EstVide(a)){
    imprimer(FilsGauche(a));
    printf("%ld ", ValeurDuNoeud(a));
    imprimer(FilsDroit(a));
  }
}

int taille (Noeud_t a) {
  if(EstVide(a)){
    return 0;
  }

  return 1 + taille(FilsDroit(a)) + taille(FilsGauche(a));
}

int hauteur (Noeud_t a) {
  int hg, hd;
  if(EstVide(a)){
    return -1;
  }
  else{
    hg = hauteur(FilsGauche(a));
    hd = hauteur(FilsDroit(a));
    return 1 + max(hg,hd);
  }
}

int nbFeuilles(Noeud_t a) {
  if(EstVide(a)){
    return 0;
  }else if(EstFeuille(a)){
    return 1;
  }
  return  nbFeuilles(FilsGauche(a)) + nbFeuilles(FilsDroit(a));
}


/* Comptage d'arbres */

int nbArbres(int n) {
  int i;
  int res;

  res = 0;
  if(n == 0){
    return 1;
  }

  for(i = 0; i < n; i++){
    res += (nbArbres(i)*nbArbres(n-1-i));
  }

  return res;
}

/* Manipulation d'arbres binaires de recherche */

Noeud_t abr1 (void) {
  Noeud_t arbre, tmp;

  arbre = CreerNoeud(6);
  tmp = CreerNoeud(4);
  AjouterFilsGauche(arbre, tmp);
  AjouterFilsGauche(tmp, CreerNoeud(2));
  AjouterFilsDroit(arbre, CreerNoeud(7));
  AjouterFilsDroit(tmp, CreerNoeud(5));
  tmp = FilsGauche(tmp);
  AjouterFilsGauche(tmp, CreerNoeud(1));

  return arbre;
}

Noeud_t ajouter (value_t v, Noeud_t a) {
  Noeud_t tmp;
  Noeud_t noeud_aj;
  /* a -> the tree root */

  tmp = NULL;
  noeud_aj = CreerNoeud(v);
  while( !EstVide(a)){
    tmp = a;

    if(ValeurDuNoeud(noeud_aj) < ValeurDuNoeud(a))
      a = FilsGauche(a);
    else
      a = FilsDroit(a);
  }
  if(EstVide(tmp))
    a = noeud_aj;
  else if(ValeurDuNoeud(noeud_aj) < ValeurDuNoeud(tmp))
    AjouterFilsGauche(tmp, noeud_aj);
  else
    AjouterFilsDroit(tmp, noeud_aj);

  return a;
}

Noeud_t abr2 (void) {
  Noeud_t a;
  a = CreerNoeud(5);

  ajouter(4, a);
  ajouter(2, a);
  ajouter(7, a);
  ajouter(6, a);
  ajouter(1, a);
  return a;
}

Noeud_t abr3 (void){
  Noeud_t a;
  a = CreerNoeud(7);

  ajouter(1, a);
  ajouter(4, a);
  ajouter(5, a);
  ajouter(6, a);
  ajouter(2, a);
  return a;
}

int appartient (value_t v, Noeud_t a) {
  value_t value;

  if(EstVide(a))
    return 0;
  else{
    value = ValeurDuNoeud(a);
    if(value == v)
      return 1;
    else{
      if(v <= value)
  return appartient(v, FilsGauche(a));
      else
  return appartient(v, FilsDroit(a));
    }
  }

  return 0;
}

int valeur_minimale (Noeud_t abr) {
  if(EstVide(FilsGauche(abr)))
    return ValeurDuNoeud(abr);
  else
    return valeur_minimale(FilsGauche(abr));
}


int valeur_maximale (Noeud_t abr) {
  if(EstVide(FilsDroit(abr)))
    return ValeurDuNoeud(abr);
  else
    return valeur_maximale(FilsDroit(abr));
}

/* Entier mysterieux */

Noeud_t construitArbreEntierMysterieux (value_t i, value_t j) {
  if( i == j)
    return CreerNoeud(i);
  else
    return ajouter(j, construitArbreEntierMysterieux(i, j-1));

}

 /* Jeu de l'entier mystérieux */

void jouer (int n) {

  /*Initialisation*/
  Noeud_t arbre; /*ABR de 0 à n*/
  Noeud_t tmp; /*Parcours de l'arbre*/
  int robot; /*Recherche dichotomique de l'entier à deviner*/
  char reponse; /*Input*/
  arbre = construitArbreEntierMysterieux(0,n);
  robot = ValeurDuNoeud(arbre);
  printf("Jeu de l'entier mystérieux, appuyez sur Entrée");
  getchar(); /*Pause*/
  printf("Choisissez un entier à faire deviner, et appuyez sur Entrée");
  getchar(); /*Pause*/
  while (reponse != 'O') /*Tant que l'entier mystérieux n'a pas été trouvé */
  {
    printf("Est-ce que %d est la bonne réponse ? Entrez \'O\' pour oui \n",robot);
    if ((reponse = getchar()) != 'O') /*Mauvaise reponse*/
    {
      printf("Est-ce que c'est + ou - ? Entrez \'+\' ou \'-\'");
      if ((reponse = getchar()) == '+')
      {
        tmp = FilsDroit(arbre); /* On part à droite */
        arbre = tmp;
        robot = ValeurDuNoeud(arbre);
      }
      else if ((reponse = getchar()) == '-')
      {
        tmp = FilsGauche(arbre); /* On part à gauche */
        arbre = tmp;
        robot = ValeurDuNoeud(arbre);
      }

    }
  }
  printf("Trouvé !");
}

/* Tests sur les arbres binaires */

void testArbreBinaire(Noeud_t a) {
   imprimer(a); printf("\n");
   printf("Taille     = %d\n",(taille(a)));
   printf("Hauteur    = %d\n",(hauteur(a)));
   printf("nbFeuilles = %d\n",(nbFeuilles(a)));
}

/* Tests sur les arbres binaires de recherche */
void testABR (Noeud_t a) {
   int i;
   imprimer(a); printf("\n");
   printf("Taille     = %d\n",(taille(a)));
   printf("Hauteur    = %d\n",(hauteur(a)));
   printf("nbFeuilles = %d\n",(nbFeuilles(a)));
   printf("Valeurs présentes dans l'arbre : ");


   for (i = 1; i <= 10; i++) {
      if (appartient(i,a)) {
         printf("%d ",i);
      }
   }
   printf("\n");

   printf("La valeur maximale est: %d\n",(valeur_maximale(a)));
   printf("La valeur minimale est: %d\n",(valeur_minimale(a)));

   printf("\n");

}

/* Programme principal */
int main (int argc, char **argv) {

   int i;

   testArbreBinaire(arbre1());
   testArbreBinaire(arbre2());
   testArbreBinaire(arbre3());

   for (i = 0; i <= 19; i++) {
      printf("Le nombre d'arbres à %d noeuds est %d\n",i,(nbArbres(i)));
   }

   testABR(abr1());
   testABR(abr2());
   testABR(abr3());

   printf("Arbre mysterieux entre 12 et 24:\n");
   imprimer(construitArbreEntierMysterieux(12,24));
   printf("\n");

   jouer(100);

   return 0;

}
