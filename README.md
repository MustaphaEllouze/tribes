# tribes

![image](./logo.png)
 
Ce module a pour but de simuler la vie au sein d'un groupe de tribus, leurs interactions, le vieillissement et le renouvellement de la population, les changements de territoire, etc.

C'est un projet long-terme, il prendra je l'espère de l'ampleur au fur et à mesure du temps.

## Travail en cours
* Module `persons` : gestion des personnes individuelles.
* Module `utils`   : divers bout de code servant à simplifier le développement des autres modules.

## Description des modules
* Module `persons` : 
    * `Age` : gestion de l'âge, à passer dans une classe abstraite en dehors de `persons`.
    * `Data` : contient l'ensemble des données nécessaires pour le bon fonctionnement, dont définition des races, etc.
    * `Gender` : gestion des sexes biologiques. 
    * `Height` : gestion de la taille, à passer dans une classe abstraite en dehors de `persons`.
    * `Hierarchy` : gestion de la hiérarchie au sein de la tribu.
    * `Job` : gestion des différents métiers.
    * `MedicalCondition` : gestion des maladies et handicaps d'une personne.
    * `Person` : gestion des personnes individuelles. Structure de donnée de plus haut niveau.
    * `Personality` : gestion de la personnalité des individus.
    * `Race` : gestion des races et de leurs caractéristiques.
    * `Skill`  : gestion des aptitudes des personnes.
    * `Weight` : gestion du poids des personnes, à passer dans une classe abstraite en dehors de `persons`.

* Module `utils`:
    * `CappedNumbers` : définition de nombres avec bornes supérieures et/ou inférieures.
    * `random` : gère la génération de nombres aléatoires selon certaines lois.

## Ce qu'il faudrait faire 
* Module `persons`: commentaires et documentation 
* Module `utils`  : commentaires et documentation 

## TODO list détaillée