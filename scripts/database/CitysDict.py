# Dictionary containing a mapping of all regions and citys
from scripts.helpers import DocCleaner
from scripts.helpers.FileHelper import FileHelper

cityMap = dict(west={
    'los angeles': [
        'w la',
        'n la',
        'e la',
        's la',
        'la',
        'w los angeles',
        'n los angeles',
        'e los angeles',
        's los angeles',
        'los angeles',
        'studio city',
        'bel air',
        'sherman oaks',
        'santa monica',
        'w hollywood',
        'n hollywood',
        'e hollywood',
        's hollywood',
        'hollywood',
        'beverly hills',
        'los feliz',
        'chinatown',
        'pacific palisades',
        'toluca lake',
        'northridge',
        'mar vista',
        'venice',
        'century city',
        'st boyle hts',
        'rancho park',
        'marina del rey',
        'long beach',
        'encino',
        'monterey park',
        'burbank',
        'manhattan beach',
        'glendale',
        'pasadena'
    ],
    'culver city': ['culver city'],
    'redondo beach': ['redondo beach'],
    'westlake village': ['westlake village'],
    'malibu': ['malibu'],
    'las vegas': ['las vegas'],
    'san francisco': ['san francisco'],
    'hermosa beach': [
        'hermosa beach',
        'st hermosa beach',
    ],
    'westwood': ['westwood'],
    'seal beach': ['seal beach'],
    'brentwood': ['brentwood'],
    'roswell': ['roswell'],
}, east={
    'new york': [
        'new york',
        'new york city',
        'brooklyn',
        'queens'
    ],
    'atlanta': ['atlanta'],
    'college park': ['college park'],
    'decatur': ['decatur'],
    'duluth': ['duluth'],
    'smyrna': ['smyrna'],
    'marietta': ['marietta']
})

file = '../restaurants.tsv'


# Get string key from dict
def get_city_key(city: str):
    for regionKey in cityMap:
        for cityKey in cityMap[regionKey]:
            for local in cityMap[regionKey][cityKey]:
                if city == local:
                    return cityKey
    return 'City not found'


# Testing if every location from the document is in the dictionary
def test_dict():
    file_helper = FileHelper(file, '\t')
    file_list = list(file_helper.read_file())
    for item in file_list:
        is_city = False
        for regionKey in cityMap:
            for cityKey in cityMap[regionKey]:
                for local in cityMap[regionKey][cityKey]:
                    if DocCleaner.fix_city(item['city']) == local:
                        is_city = True
        if not is_city:
            print(item['city'])
