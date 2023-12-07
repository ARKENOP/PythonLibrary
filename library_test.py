from library import Library, LibraryDatabase, LibraryFactory, TitleSearchStrategy, AuthorSearchStrategy, CategorySearchStrategy

library_db = LibraryDatabase()
library_factory = LibraryFactory()

library = Library(library_db, library_factory)

# Ajout des livres
library.add_book("Le Petit Prince", "Antoine de Saint-Exupéry", "Conte")
library.add_book("Hunger Games", "Suzanne Collins", "Science-fiction")
library.add_book("Le Petit Chaperon Rouge", "Charles Perrault", "Conte")

# Recherche de livres par titre
print("\nRecherche de livres par titre :")
library.search_books(TitleSearchStrategy(), "Hunger Games")
library.search_books(TitleSearchStrategy(), "Le Petit")

# Recherche de livres par auteur
print("\nRecherche de livres par auteur :")
library.search_books(AuthorSearchStrategy(), "Charles Perrault")
library.search_books(AuthorSearchStrategy(), "Antoine")

# Recherche de livres par catégorie
print("\nRecherche de livres par catégorie :")
library.search_books(CategorySearchStrategy(), "Conte")
library.search_books(CategorySearchStrategy(), "Science")

# Enregistrer un utilisateur
library.register_user("Paul")

# Emprunter un livre
library.borrow_book("Paul", "Le Petit Prince")

# Retourner un livre
library.return_book("Paul", "Le Petit Prince")

# Sauvegarder l'état de la bibliothèque
library_db.save_state()