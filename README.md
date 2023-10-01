# tribes

![image](./logo.png)
 
Ce module a pour but de simuler la vie au sein d'un groupe de tribus, leurs interactions, le vieillissement et le renouvellement de la population, les changements de territoire, etc.

C'est un projet long-terme, il prendra je l'espère de l'ampleur au fur et à mesure du temps.

## Travail en cours
* Module `persons` : gestion des personnes individuelles.
* Module `utils`   : divers bout de code servant à simplifier le développement des autres modules.

## Description des modules
* Module `persons` : 
    * `Data` : contient l'ensemble des données nécessaires pour le bon fonctionnement, dont définition des races, etc.
    * `Gender` : gestion des sexes biologiques. 
    * `Hierarchy` : gestion de la hiérarchie au sein de la tribu.
    * `Job` : gestion des différents métiers.
    * `MedicalCondition` : gestion des maladies et handicaps d'une personne.
    * `Person` : gestion des personnes individuelles. Structure de donnée de plus haut niveau.
    * `Personality` : gestion de la personnalité des individus.
    * `Race` : gestion des races et de leurs caractéristiques.
    * `Skill`  : gestion des aptitudes des personnes.

* Module `utils`:
    * `CappedNumbers` : définition de nombres avec bornes supérieures et/ou 
    * `Age` : gestion de l'âge.
    * `Time` : gestion du temps
    * `random` : gère la génération de nombres aléatoires selon certaines lois.
    * `Weight` : gestion du poids des personnes
    * `Height` : gestion de la taille

## Ce qu'il faudrait faire 
* Module `persons`: 
    * commentaires et documentation 
    * proposer un assemblage de `hierarchy` et `job` pour distinguer la position hiérarchique et la position sociétale.
    * proposer une manière de gérer la réputation d'une personne vis-à-vis d'une autre personne
    * dans `personality`, faire en sorte qu'on ne puisse pas toucher aux valeurs des attributs du dictionnaire, accès via fonctions.
    * dans `race`, il faudrait grouper les tailles, poids (etc.) cible ensemble et laisser `gender` définir les genres toute seule.
* Module `utils`  : 
    * commentaires et documentation 
    * définir des distributions, et des randint dans ces distributions

## TODO list détaillée
* Module `persons` : 
* Module `utils`   : 