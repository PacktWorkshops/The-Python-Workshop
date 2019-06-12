import unittest
import import_ipynb
import datetime

class TestExamples(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import examples_and_exercises
        self.exercises = examples_and_exercises

    def test_Australian(self):
        self.assertTrue(self.exercises.ming.is_human)
        self.assertTrue(self.exercises.ming.enjoys_sport)

    def test_dogcat(self):
        # simply tests we don't hit any exceptions, as this function doesnt return anything
        self.exercises.my_pet.make_sound()
        
    def test_organized_baby(self):
        # simply tests we don't hit any exceptions, as this function doesnt return anything
        self.exercises.boris.book_appointment(datetime.date(2018,1,1))
        
    def test_custom_diary(self):
        self.assertEqual(self.exercises.first_diary.show_birthday(), '01-Jan-2018')
        self.assertEqual(self.exercises.second_diary.show_christmas(), '03/03/2018')
        
    def test_talkative_person(self):
        self.assertEqual(self.exercises.john.first_name, 'John')
    
    def test_better_person(self):
        self.assertEqual(self.exercises.my_person.full_name, 'Mary Anne Smith')
        
    def test_my_int(self):
        self.assertFalse(self.exercises.MyInt(11).is_divisible_by(5))
        self.assertTrue(self.exercises.MyInt(12).is_divisible_by(3))
        
    def test_my_cat(self):
        self.assertEqual(self.exercises.my_cat.name, 'Kibbles')
        
    def test_temp(self):
        self.assertEqual(self.exercises.Temperature(0).fahrenheit, 32)
        
    def test_customer(self):
        self.assertEqual(self.exercises.customer.full_name, 'Mary Schmidt')
        
    def test_mexico_size(self):
        self.assertAlmostEqual(self.exercises.mexico.size_kmsq, 1968392.1818017708)
        
    def test_algeria_size(self):
        self.assertAlmostEqual(self.exercises.algeria.size_miles_sq(conversion_rate=0.6), 857520.0)
        
    def test_chat(self):
        self.assertEqual(self.exercises.chad.population, 100)
        
    def test_bowser(self):
        self.assertTrue(self.exercises.bowser.is_tall(20))
        
    def test_circle_area(self):
        self.assertAlmostEqual(self.exercises.circle.area(), 12.566370614359172)
        
    def test_circle_color(self):
        self.assertEqual(self.exercises.my_circle.color, 'red')
        

if __name__ == '__main__':
    unittest.main()