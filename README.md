# Système de Gestion de Bibliothèque Simplifié

Ce script Python implémente un système de gestion de bibliothèque simple avec les fonctionnalités suivantes :
- Ajout et retrait de livres
- Recherche de livres par titre, auteur ou catégorie
- Enregistrement de nouveaux utilisateurs de la bibliothèque
- Emprunt et retour de livres
- Sauvegarde de l'état de la bibliothèque dans un fichier JSON

## Prérequis

- Python 3.x

## Utilisation

1. Clonez ce dépôt sur votre machine :

    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
    ```

2. Exécutez le script de test :

    ```bash
    python test_library.py
    ```

    Assurez-vous que les fichiers `library.py` et `test_library.py` sont dans le même répertoire.

## Fonctionnalités

### Ajout de livres

Utilisez la méthode `add_book` pour ajouter un livre à la bibliothèque. Par exemple :

```python
library.add_book("Titre du Livre", "Auteur du Livre", "Catégorie du Livre")
```

### Recherche de livres

Utilisez la méthode `search_books` avec une stratégie spécifique pour rechercher des livres. Par exemple, pour rechercher par titre :

```python
library.search_books(TitleSearchStrategy(), "Titre du Livre")
```

### Enregistrement d'utilisateurs

Utilisez la méthode `register_user` pour enregistrer de nouveaux utilisateurs. Par exemple :

```python
library.register_user("Nom de l'Utilisateur")
```

### Emprunt de livres

Utilisez la méthode `borrow_book` pour emprunter un livre à un utilisateur. Par exemple :

```python
library.borrow_book("Nom de l'Utilisateur", "Titre du Livre")
```

### Retour de livres

Utilisez la méthode `return_book` pour retourner un livre emprunté par un utilisateur. Par exemple :

```python
library.return_book("Nom de l'Utilisateur", "Titre du Livre")
```

### Vérification de qui détient un livre

Utilisez la méthode `who_borrowed` pour vérifier qui détient actuellement un livre. Par exemple :

```python
library.who_borrowed("Titre du Livre")
```

### Sauvegarde de l'état

L'état de la bibliothèque est sauvegardé dans un fichier JSON. Vous pouvez sauvegarder manuellement l'état en appelant la méthode `save_state` de LibraryDatabase.
