from fuzzywuzzy import fuzz

from scripts.helpers.FileHelper import FileHelper


# Tests realized between: ratio(), partial_ratio(), token_set_ratio(), token_sort_ratio(), partial_token_set_ratio(),
# partial_token_sort_ratio()


def is_name_similar(name1: str, name2: str) -> int:
    if name1 in name2 or name2 in name1:
        return 100
    return fuzz.token_set_ratio(name1, name2)


# The address can be completely different, since the restaurant can have changed location
def is_address_similar(address1: str, address2: str) -> int:
    return fuzz.token_set_ratio(address1, address2)


# The citys can be different
# Receive the key for the city
def is_city_similar(city1: str, city2: str) -> int:
    if city1 == city2:
        return 100
    else:
        return 0


# The phone can be completely differente
def is_phone_similar(phone1: str, phone2: str) -> int:
    return fuzz.ratio(phone1, phone2)


# The type can be different
# Receive the key for the type
def is_type_similar(t1: str, t2: str) -> int:
    if t1 == t2:
        return 100
    else:
        return 0


# Compare docs based on a weight system

nameWeight = 5
cityWeight = 4
phoneWeight = 3
addressWeight = 2
typeWeight = 1


def is_doc_similar(doc1: dict, doc2: dict) -> int:
    result_name = is_name_similar(doc1['name'], doc2['name'])
    result_city = is_city_similar(doc1['cityKey'], doc2['cityKey'])
    result_phone = is_phone_similar(doc1['phone'], doc2['phone'])
    result_address = is_address_similar(doc1['address'], doc2['address'])
    result_type = is_type_similar(doc1['typeKey'], doc2['typeKey'])
    total = (result_name * nameWeight) + (result_city * cityWeight) + (result_phone * phoneWeight) + (
            result_address * addressWeight) + (result_type * typeWeight)
    return total


# Find adequate method to compare two strings
def find_adequate_method(category: str, comparator_method: staticmethod, cleaner_method: staticmethod):
    file = '../restaurants.tsv'
    golden_standart = '../golden_standart.tsv'

    file_helper = FileHelper(file, '\t')
    file_list = list(filter(lambda r: int(r['id']) <= 224, file_helper.read_file()))
    file_helper = FileHelper(golden_standart, '\t')
    golden_list = file_helper.read_file()
    res = []
    for standart in golden_list:
        id1 = int(standart['id1']) - 1
        id2 = int(standart['id2']) - 1
        item1 = cleaner_method(file_list[id1][category])
        item2 = cleaner_method(file_list[id2][category])
        result = comparator_method(item1, item2)
        if result != 100:
            res.append('{}|{}:{}'.format(id1, id2, result))
    print(res)
