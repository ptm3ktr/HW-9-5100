import pandas as pd

class BookLover:
    def __init__(self, name: str, email: str, fav_genre: str, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        # I was running into errors when I set the book_list=pd.DataFrame({'book_name': [], 'book_rating': []}) in the __init__ function. I searched online and I found as to why I was running into the error and suggested to use an if is None (https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil)
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        else:
            self.book_list = book_list

    def add_book(self, book_name, rating):
        # Check if the book already exists in the book list
        if book_name in self.book_list['book_name'].values:
            print(f"The book '{book_name}' has already been added.")
        else:
            # Create a new book DataFrame
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
         
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    