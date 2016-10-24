"""Using [script to sort a list and remove negative numbers], create a test suite 
to verify that this script has all if the intended functionality. 

A few things to keep in mind:
	- methods need to be named test_something so that unittest 
		will recognize them as tests.
	- The setup method always runs first and the teardown method always 
		runs last. They are not required but can be useful."""

import unittest

# Script to sort a list and remove negative numbers:
def sort_and_remove(ls):
	# sorts list and removes negative numbers
	ls = sorted(ls) # sort list
	number_negatives = sum(n<0 for n in ls) # find amount of neg nums in list
	del ls[:number_negatives] # remove that amount from beginning of list
	return ls

class Test_sort_and_remove(unittest.TestCase):
	def test_sorted(self):
		self.assertEqual(sort_and_remove([5,4,3,0]),[0,3,4,5])

	def test_remove_negatives(self):
		self.assertEqual(sort_and_remove([-1,-2,3,4]),[3,4])

# run unit test
suite = unittest.TestLoader().loadTestsFromTestCase(Test_sort_and_remove)
unittest.TextTestRunner(verbosity=2).run(suite)