import unittest

from scripts.utils import DocComparator


class MyTestCase(unittest.TestCase):
    def test_is_name_similar(self):
        self.assertTrue(DocComparator.is_name_similar("art's delicatessen", "art's deli"))


if __name__ == '__main__':
    unittest.main()
