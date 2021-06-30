# Cool snippets to use for later

_______________________________________________________________________________
Comment highlighting

#todo sdfsdf
#! important
#? question
#* special?
# the strike through below is # followed by --
#-- strikethrough
# default
_______________________________________________________________________________
#Find current cursor position

import win32api

win32api.GetCursorPos()
#returns int, int of cursor position

win32api.SetCursorPos((x,y))
# sets cursor to position defined
# Need to set coordinates as a tuple
# E.G.   x,y = (x,y)   win32api.SetCursorPos((x,y))

_______________________________________________________________________________
# use to select file or directory with a graphical interface
from tkinter import filedialog
from tkinter import *
root = Tk()
filedialog.askdirectory(initialdir = "/", title = "Please select a directory")
filedialog.askopenfilename(initialdir = "/", title = "Please select a file")
root.destroy()

_______________________________________________________________________________
timeit example

# importing the required modules 
import timeit 
  
# binary search function 
def binary_search(mylist, find): 
    while len(mylist) > 0: 
        mid = (len(mylist))//2
        if mylist[mid] == find: 
            return True
        elif mylist[mid] < find: 
            mylist = mylist[:mid] 
        else: 
            mylist = mylist[mid + 1:] 
    return False
  
  
# linear search function 
def linear_search(mylist, find): 
    for x in mylist: 
        if x == find: 
            return True
    return False
  
  
# compute binary search time 
def binary_time(): 
    SETUP_CODE = ''' 
from __main__ import binary_search 
from random import randint'''
  
    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
binary_search(mylist, find)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # printing minimum exec. time 
    print('Binary search time: {}'.format(min(times)))         
  
  
# compute linear search time 
def linear_time(): 
    SETUP_CODE = ''' 
from __main__ import linear_search 
from random import randint'''
      
    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
linear_search(mylist, find) 
    '''
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('Linear search time: {}'.format(min(times)))   
  
if __name__ == "__main__": 
    linear_time() 
    binary_time() 
_______________________________________________________________________________

import logging

# console and file handler
#0 setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#console handler and file handler
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('***************')
#setting level for logging
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.DEBUG)
#setting format for logs
c_format = logging.Formatter('%(name)s | %(lineno)d | %(levelname)s | %(message)s')
f_format = logging.Formatter('%(asctime)s | %(name)s | %(lineno)d | %(levelname)s | %(message)s')
#add format to handlers
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)
#add handlers
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# console logger
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter('%(name)s | %(lineno)d | %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)

# file logger
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f_handler = logging.FileHandler('log.txt')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s | %(name)s | %(lineno)d | %(levelname)s | %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)



from logging.handlers import RotatingFileHandler
logging.basicConfig(filename="****", level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = RotatingFileHandler("my_log.log", maxBytes=2000, backupCount=10)
# add mode to handler for append or write 'a' / 'w'
_______________________________________________________________________________

#Unit test framework

# need to append the location of the script to test here
import sys
sys.path.append(
                'file location of script to test'
				)

import unittest

from specific_script.py import some_module_or_function

class TestSpecificFunction(unittest.TestCase):
	def test_some_function_for_some_case(self):
		"""
		Description of test for specific function.
		"""
		self.assertEqual(a, b)
		self.assertNotEqual(a, b)
		self.assertTrue(x)
		self.assertFalse(x)
		self.assertIs(a, b)
		self.assertIsNot(a, b)
		self.assertIsNone(x)
		self.assertIsNotNone(x)
		self.assertIn(a, b)
		self.assertNotIn(a, b)
		self.assertIsInstance(a, b)
		self.isinstance(a, b)
		self.assertNotIsInstance(a, b)
		#* check for exception like string instead of int
		with self.assertRaises(Exception):
			sdfsdsdf

	def test_some_function_for_some_other_case(self):
		assertEqual(a,b)

if __name__ == '__main__':
	unittest.main()


_______________________________________________________________________________

#decorator boiler plat for decorating / modifying functions

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


_______________________________________________________________________________

#function timer example
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def func()
_______________________________________________________________________________

#! font collection

    "editor.fontFamily": "Office Code Pro D",
    "editor.fontFamily": "Monoid",    
    "editor.fontFamily": "Hack",
    "editor.fontFamily": "Fira Code",

_______________________________________________________________________________
#* Example of Google docstring format
def test_func(argument):
	"""[summary]
	
	Args:
		argument ([type]): [description]
	
	Raises:
		Exception: [description]
	
	Returns:
		[type]: [description]
	"""
	raise Exception
	return argument


_______________________________________________________________________________
#* creating packages in current environment

from pip._internal.operations.freeze import freeze
for requirement in freeze(local_only=True):
    print(requirement)















