import unittest
from main import Collection

class TestCollection(unittest.TestCase):
    def test_add_element(self):
        collection = Collection()
        collection.add_element(1)
        self.assertEqual(collection.get_length(), 1)
        collection.add_element(2)
        self.assertEqual(collection.get_length(), 2)
        collection.add_element(3)
        self.assertEqual(collection.get_length(), 3)

    def test_remove_element(self):
        collection = Collection()
        collection.add_element(1)
        collection.add_element(2)
        collection.add_element(3)
        collection.remove_element(2)
        self.assertEqual(collection.get_length(), 2)
        with self.assertRaises(ValueError):
            collection.remove_element(4)

    def test_get_element_index(self):
        collection = Collection()
        collection.add_element(1)
        collection.add_element(2)
        collection.add_element(3)
        self.assertEqual(collection.get_element_index(2), 1)
        self.assertEqual(collection.get_element_index(4), -1)

if __name__ == '__main__':
    unittest.main()
