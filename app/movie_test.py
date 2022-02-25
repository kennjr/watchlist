import unittest

from app.model.movie import Movie



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def setUp(self) -> None:
        """
        Set up method that will run before every Test
        """
        self.new_movie = Movie(1234, 'Python Must Be Crazy', 'A thrilling new Python Series',
                               'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))

if __name__ == '__main__':
    unittest.main()
