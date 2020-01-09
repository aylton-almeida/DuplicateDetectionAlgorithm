import unittest

from scripts.database.TypeDict import get_type_key


class MyTestCase(unittest.TestCase):
    def test_get_key(self):
        self.assertEqual(get_type_key('pizza'), 'american')

    def test_no_key_found(self):
        self.assertEquals(get_type_key('potato'), 'Type not found')


if __name__ == '__main__':
    unittest.main()
