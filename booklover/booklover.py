import pandas as pd
import numpy as np
import unittest
    
class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, book_rating):
        
        if (book_name not in self.book_list['book_name'].tolist()) and (0 <= book_rating <= 5) and (isinstance(book_name,str)):
    
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
            self.num_books += 1
            
        else: 
            print('This book is in your list already, invalid rating (0-5), or not string')
        
    def has_read(self, book_name):
        
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    
    def num_books_read(self):
        print('Total # of books read =', self.num_books)
        
    def fav_books(self):
        
        return self.book_list.loc[self.book_list['book_rating'] > 3]
             
# if __name__ == '__main__':
    
#     test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
#     test_object.add_book("War of the Worlds", 4)
#     # And so forth