import unittest

from scripts.utils import DocCleaner


class MyTestCase(unittest.TestCase):
    def test_fix_address_dots(self):
        self.assertEqual(DocCleaner.fix_address('435 s. la cienega blv.'), '435 s la cienega blv', 'Fix dots')

    def test_fix_address_fixed(self):
        self.assertEqual(DocCleaner.fix_address('9560 dayton way'), '9560 dayton way', 'Fixed address')

    def test_fix_name_quotes(self):
        self.assertEqual(DocCleaner.fix_name("art's delicatessen"), 'art s delicatessen', 'Fix quotes')

    def test_fix_name_parenteses(self):
        self.assertEqual(DocCleaner.fix_name('spago (los angeles)'), 'spago los angeles', 'Fix parenteses')

    def test_fix_name_fixed(self):
        self.assertEqual(DocCleaner.fix_name('cafe bizou'), 'cafe bizou', 'Fixed name')

    def test_fix_phone_slash(self):
        self.assertEqual(DocCleaner.fix_phone('818/762 1221'), '818 762 1221', 'Fix slashs')

    def test_fix_phone_line(self):
        self.assertEqual(DocCleaner.fix_phone('818 762-1221'), '818 762 1221', 'Fix lines')

    def test_fix_phone_fixed(self):
        self.assertEqual(DocCleaner.fix_phone('818 762 1221'), '818 762 1221', 'Fixed phone')

    def test_fix_type_parenteses(self):
        self.assertEqual(DocCleaner.fix_type('french (new)'), 'french new', 'Fix parenteses')

    def test_fix_type_fixed(self):
        self.assertEqual(DocCleaner.fix_type('french new'), 'french new', 'Fixed parenteses')

    def test_fix_city_north(self):
        self.assertEqual(DocCleaner.fix_city('north sea'), 'n sea', 'North city')

    def test_fix_city_north_fixed(self):
        self.assertEqual(DocCleaner.fix_city('n sea'), 'n sea', 'North city fixed')

    def test_fix_city_south(self):
        self.assertEqual(DocCleaner.fix_city('south sea'), 's sea', 'South city')

    def test_fix_city_south_fixed(self):
        self.assertEqual(DocCleaner.fix_city('s sea'), 's sea', 'South city fixed')

    def test_fix_city_west(self):
        self.assertEqual(DocCleaner.fix_city('WeSt sea'), 'w sea', 'West city')

    def test_fix_city_west_fixed(self):
        self.assertEqual(DocCleaner.fix_city('w. sea'), 'w sea', 'West city fixed')

    def test_fix_city_east(self):
        self.assertEqual(DocCleaner.fix_city('east sea'), 'e sea', 'East city')

    def test_fix_city_east_fixed(self):
        self.assertEqual(DocCleaner.fix_city('e sea'), 'e sea', 'East city fixed')

    def test_clean_doc_list(self):
        old_arr = [
            {
                'address': '435 s. la cienega blv.',
                'city': 'los angeles',
                'phone': '310/246-1501',
                'type': 'american',
                'name': "arnie morton's of chicago"
            }
        ]
        new_arr = [
            {
                'address': '435 s la cienega blv',
                'city': 'los angeles',
                'phone': '310 246 1501',
                'type': 'american',
                'name': "arnie morton s of chicago"
            }
        ]
        self.assertEquals(DocCleaner.clean_doc_list(old_arr), new_arr)

        if __name__ == '__main__':
            unittest.main()
