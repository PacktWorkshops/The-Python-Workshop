import unittest
import import_ipynb
import datetime
from my_module import compute

class TestLesson03(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import examples_and_exercises
        self.exercises = examples_and_exercises

    def test_compute_function(self):
        result = compute([5, 7, 11])
        self.assertEqual(result, 39921960)
        
    def test_docstring(self):
        import my_module
        self.assertEqual(my_module.__doc__, 'This script computes the sum of the factorial of a list of numbers')
       
    def test_sum_to_10(self):
        from sum_to_10 import result
        self.assertEqual(result, 55)
        
    def test_maximum(self):
        self.assertEqual(self.exercises.maximum, 7)
       
    def test_search_algorithm_result(self):
        self.assertEqual(self.exercises.location, 4)
    
    def test_add_up(self):
        self.assertEqual(self.exercises.add_up(1, 3), 4)
        
    def test_get_second_element(self):
        self.assertEqual(self.exercises.get_second_element([1, 2, 3]), 2)
    
    def test_get_second_element_failing(self):
        self.assertEqual(self.exercises.get_second_element([1]), 'List was too small')
        
    def test_list_product(self):
        self.assertEqual(self.exercises.list_product([2, 10, 15]), 300)
    
    def test_get_the_time(self):
        self.assertAlmostEqual(self.exercises.get_the_time(), datetime.datetime.now())
        
    def test_add_suffix(self):
        self.assertEqual(self.exercises.add_suffix('.co.uk'), 'google.co.uk')
    
    def test_currency_conversion(self):
        self.assertAlmostEqual(self.exercises.convert_usd_to_aud(100, rate=0.78), 128.2051282051282)
    
    def test_convert_and_sum_list_kwargs(self):
        self.assertEqual(self.exercises.convert_and_sum_list_kwargs([1, 3], rate=0.8), 5.0)
        
    def test_sum_first_n(self):
        self.assertEqual(self.exercises.sum_first_n(100), 5050)
        
    def test_is_prime(self):
        self.assertEqual(self.exercises.is_prime(1000), False)
        self.assertEqual(self.exercises.is_prime(7), True)
    
    def test_print_the_next_number(self):
        self.assertEqual(self.exercises.print_the_next_number(5), "I'm bored")
        
    def test_factorial_functions(self):
        self.assertEqual(self.exercises.factorial_iterative(5), 120)
        self.assertEqual(self.exercises.factorial_recursive(5), 120)
        
    def test_compute_usd_total(self):
        self.assertEqual(self.exercises.compute_usd_total(amount_in_gbp=10), 13.029)
    
    def test_first_item(self):
        self.assertEqual(self.exercises.first_item([1, 2, 3]), 1)
        
    def test_sorted_names(self):
        self.assertEqual(sorted(self.exercises.names, key=lambda x : len(x)),
                               ['Ming', 'Boris', 'Andrew', 'Jennifer'])
        
if __name__ == '__main__':
    unittest.main()