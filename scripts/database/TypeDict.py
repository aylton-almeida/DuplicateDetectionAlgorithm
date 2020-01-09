from scripts.helpers import DocCleaner
from scripts.helpers.FileHelper import FileHelper

typeDict = {
    'american': [
        'american',
        'american new',
        'american traditional',
        'steakhouses',
        'californian',
        'american traditional',
        'southwestern',
        'bbq',
        'barbeque',
        'steak houses',
        'dive american',
        'barbecue',
        'only in las vegas',
        'old san francisco',
        'fast food',
        'hamburger'
        'hamburgers',
        'hot dogs',
        'sandwiches',
        'tex-mex',
        'pacific new wave'
    ],
    'french': [
        'french',
        'french bistro',
        'french new',
        'french classic',
    ],
    'asian': [
        'asian',
        'japanese',
        'chinese',
        'indian',
        'thai',
        'cambodian',
        'middle eastern',
        'delis',
        'delicatessen'
    ],
    'italian': [
        'italian',
        'nuova cucina italian',
        'noodle shops',
        'pizza'
    ],
    'seafood': [
        'seafood',
        'pacific rim'
    ],
    'continental': [
        'continental',
        'scandinavian'
    ],
    'coffee bar': [
        'coffee bar',
        'coffeehouses',
        'cafeteria',
        'cafeterias',
        'coffee shops'
    ],
    'caribbean': [
        'caribbean',
    ],
    'mexican': [
        'mexican'
    ],
    'russian': [
        'russian'
    ],
    'mediterranean': [
        'mediterranean',
        'greek'
    ],
    'international': [
        'international',
        'fusion'
    ],
    'ecletic': [
        'ecletic'
    ],
    'southern': [
        'southern',
        'southern soul'
    ],
    'health food': [
        'health food'
    ],
    'cajun': [
        'cajun'
    ],
    'eclectic': [
        'eclectic'
    ],
    'cuban': [
        'cuban'
    ],
    'latin': [
        'latin american'
    ],
    'european': [
        'east european',
        'eastern european'
    ],
    'buffets': [
        'buffets'
    ],
    'diners': [
        'diners'
    ],
    'vegetarian': [
        'vegetarian'
    ],
    'indonesian': [
        'indonesian'
    ],
    'vietnamese': [
        'vietnamese'
    ],
    'afghan': [
        'afghan'
    ],
    'ukrainian': [
        'ukrainian'
    ],
    'desserts': [
        'desserts'
    ],
    'polish': [
        'polish'
    ],
    'spanish': [
        'spanish'
    ],
    'chicken': [
        'chicken'
    ],
}

file = '../restaurants.tsv'


def get_type_key(string: str):
    for key in typeDict:
        for t in typeDict[key]:
            if t in string:
                return key
    return 'Type not found'


# Testing if every type from the document is in the dictionary
def test_dict():
    file_helper = FileHelper(file, '\t')
    file_list = list(file_helper.read_file())
    for item in file_list:
        is_type = False
        for key in typeDict:
            for t in typeDict[key]:
                if t in DocCleaner.fix_type(item['type']):
                    is_type = True
        if not is_type:
            print(item['type'])
