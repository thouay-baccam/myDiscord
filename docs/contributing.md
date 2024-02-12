# Comment contribuer
* Destiné à l'équipe, c'est-à-dire:
    * Raphaël ATTIAS
    * Théo BACCAM
    * Thouay BACCAM

* Ce document existe pour rappeller à l'équipe les conventions qu'on a mis en place pour les branches et les commits
* Basé sur:
    * https://dev.to/varbsan/a-simplified-convention-for-naming-branches-and-commits-in-git-il4
    * https://www.conventionalcommits.org/fr/v1.0.0/

## Conventions branches

### Branches permanentes
* main:
    * On merge sur main que si on est sûr à 100% que c'est 100% stable et fini
* dev:
    * On merge sur ça avant d'aller sur main

### Noms de Branches temporaires
* categorie/description-en-francais
* categories de branches:
    * feature: ajouter, refactor ou supprimer une feature
    * bugfix: pour fix un bug, évidemment
    * hotfix: un fix temporaire un peu scuffed (en cas d'urgences)
    * test: experimentations
    * docs: documentation
* feature/chat-vocal

## Conventions commits
* type(scope optionel): description courte en français
* types:
    * fix: corriger un bug
    * feat: introduire une nouvelle fonctionalité
    * refactor: petit changement du code sans changer son comportement
    * style: rendre le code plus lisible
    * docs: documentation
* le scope est la portée des modifications effectués dans un commit
* exemples:
    * fix(chat-ui): empêché texte qui déborde
    * feat: voice-chat entre deux users
    * refactor(connect): simplifié vérification
    * style(sign-up): conditions plus cleans

## Conclusion
* Une branche est comme un objectif
* Un commit est une étape vers cette objectif
* Un commit doit être le plus petit possible tant que ça soit raisonnable