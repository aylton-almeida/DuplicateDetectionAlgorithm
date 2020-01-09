import unittest

from scripts.database.CitysDict import get_city_key


class MyTestCase(unittest.TestCase):
    def test_get_key(self):
        self.assertEqual(get_city_key('santa monica'), 'los angeles')

    def test_no_key_found(self):
        self.assertEquals(get_city_key('regensburg'), 'City not found')


if __name__ == '__main__':
    unittest.main()
