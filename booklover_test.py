import pandas as pd
import numpy as np
from booklover import BookLover

import unittest

import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        person1 = BookLover('John', 'john@gmail.com', 'fiction')
        person1.add_book('hi',4)
        person1.add_book('Rangers Apprentice', 5)
        
        assert 'Rangers Apprentice' in person1.book_list['book_name'].values, 'Book not in list'
        self.assertIn('Rangers Apprentice', person1.book_list['book_name'].values.tolist(), msg = 'book already in list')
        
    def test_2_add_book(self):
        person2 = BookLover('Bob', 'bob@gmail.com', 'action')
        
        person2.add_book('Lay Bare the Heart', 5)
        person2.add_book('Lay Bare the Heart', 5)
        
        self.assertEqual(len(person2.book_list['book_name'].unique()),len(person2.book_list['book_name']), "Error: duplicate book names")
                                                                            
    def test_3_has_read(self):
        person3 = BookLover('Robert', 'robert@gmail.com', 'romance')
        person3.add_book('Treehouse', 4)
        
        self.assertTrue(person3.has_read('Treehouse'), 'Error: Book not present')
        
    def test_4_has_read(self): 
        person4 = BookLover('Rohan', 'rohan@gmail.com', 'history')
        person4.add_book('To Kill a Mockingbird', 4)
        
        self.assertFalse(person4.has_read('Treehouse'), 'Error: Book present')
        
    def test_5_num_books_read(self):
        person5 = BookLover('Alberto', 'alberto@gmail.com', 'fiction')
        person5.add_book('To Kill a Mockingbird', 4)
        person5.add_book('Hi', 4)
        person5.add_book('Curious George', 4)
        
        self.assertEqual(len(person5.book_list['book_name']), person5.num_books, "Error: Number of books does not match")

    def test_6_fav_books(self):
        person6 = BookLover('Tom', 'tom@gmail.com', 'fiction')
        person6.add_book('To Kill a Mockingbird', 2)
        person6.add_book('Hi', 4)
        person6.add_book('Curious George', 5)
        
        fb = person6.fav_books()
        self.assertTrue(np.min(fb.book_rating.values) > 3, "Error: Incorrect book ratings")

# Test 1
thing = BookLoverTestSuite()
thing.test_1_add_book()

# Test 2
thing1 = BookLoverTestSuite()
thing1.test_2_add_book()

# Test 3
thing2 = BookLoverTestSuite()
thing2.test_3_has_read()

# Test 4
thing3 = BookLoverTestSuite()
thing3.test_4_has_read()

# Test 5
thing4 = BookLoverTestSuite()
thing4.test_5_num_books_read()

# Test 6
thing5 = BookLoverTestSuite()
thing5.test_6_fav_books()

                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
