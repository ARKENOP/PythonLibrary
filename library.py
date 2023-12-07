import json

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_available = True
    
    # On convertit l'objet en dictionnaire pour pouvoir le sauvegarder dans un fichier JSON
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "is_available": self.is_available
        }

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    # Pareil que pour la classe Book
    def to_dict(self):
        return {
            "name": self.name,
            "borrowed_books": [book.to_dict() for book in self.borrowed_books]
        }

# LibraryFactory pour créer des livres et des utilisateurs
class LibraryFactory:
    def create_book(self, title, author, category):
        return Book(title, author, category)

    def create_user(self, name):
        return User(name)

# LibraryDatabase pour stocker les livres et les utilisateurs
class LibraryDatabase:
    _instance = None

    # On implémente le pattern Singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialiser la base de données vide
            cls._instance.books = []
            cls._instance.users = []
        return cls._instance

    # On implémente le pattern State pour sauvegarder et charger l'état de la base de données
    def save_state(self):
        data = {
            "books": [book.to_dict() for book in self.books],
            "users": [user.to_dict() for user in self.users]
        }
        # On sauvegarde l'état de la base de données dans un fichier JSON
        with open("library_state.json", "w") as file:
            json.dump(data, file)

    # Il est possible de charger l'état de la base de données à partir d'un fichier JSON
    def load_state(self):
        try:
            with open("library_state.json", "r") as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data["books"]]
                self.users = [User(**user) for user in data["users"]]
        except FileNotFoundError:
            # Créer la base de données si le fichier n'existe pas
            self.books = []
            self.users = []

# BookObserver pour notifier les utilisateurs lorsque des livres deviennent disponibles
class BookObserver:
    def __init__(self, book_title, user):
        self.book_title = book_title
        self.user = user

    def notify(self, book):
        if book.is_available and book.title == self.book_title:
            print(f"{self.user.name}, le livre '{self.book_title}' est maintenant disponible.")

# SearchStrategy pour rechercher des livres par titre, auteur ou catégorie
class SearchStrategy:
    def search(self, library, query):
        pass

class TitleSearchStrategy(SearchStrategy):
    def search(self, library, title):
        return [book for book in library.books if title.lower() in book.title.lower()]

class AuthorSearchStrategy(SearchStrategy):
    def search(self, library, author):
        return [book for book in library.books if author.lower() in book.author.lower()]

class CategorySearchStrategy(SearchStrategy):
    def search(self, library, category):
        return [book for book in library.books if category.lower() in book.category.lower()]

# Library pour gérer les livres et les utilisateurs
class Library:
    def __init__(self, database, factory):
        self.database = database
        self.factory = factory

    def add_book(self, title, author, category):
        book = self.factory.create_book(title, author, category)
        self.database.books.append(book)
        print(f"Livre ajouté : {book.title} par {book.author}")

    def remove_book(self, title):
        for book in self.database.books:
            if book.title == title:
                self.database.books.remove(book)
                print(f"Livre retiré : {book.title} par {book.author}")
                return
        print(f"Livre non trouvé : {title}")

    def search_books(self, strategy, query):
        search_result = strategy.search(self.database, query)
        if search_result:
            for book in search_result:
                print(f"Titre: {book.title}, Auteur: {book.author}, Catégorie: {book.category}")
        else:
            print("Aucun livre trouvé.")

    def register_user(self, name):
        user = self.factory.create_user(name)
        self.database.users.append(user)
        print(f"Utilisateur enregistré : {user.name}")

    def borrow_book(self, user_name, book_title):
        user = next((user for user in self.database.users if user.name == user_name), None)
        if user:
            book = next((book for book in self.database.books if book.title == book_title), None)
            if book and book.is_available:
                book.is_available = False
                user.borrowed_books.append(book)
                print(f"{user_name} a emprunté le livre : {book_title}")
            else:
                print(f"Livre non disponible : {book_title}")
        else:
            print(f"Utilisateur non trouvé : {user_name}")

    def return_book(self, user_name, book_title):
        user = next((user for user in self.database.users if user.name == user_name), None)
        if user:
            for book in user.borrowed_books:
                if book.title == book_title:
                    book.is_available = True
                    user.borrowed_books.remove(book)
                    print(f"{user_name} a retourné le livre : {book_title}")
                    return
            print(f"Livre non emprunté par {user_name} : {book_title}")
        else:
            print(f"Utilisateur non trouvé : {user_name}")

    def who_borrowed(self, book_title):
        for user in self.database.users:
            for book in user.borrowed_books:
                if book.title == book_title:
                    print(f"{book_title} a été emprunté par : {user.name}")
                    return
        print(f"Livre non emprunté : {book_title}")