import pymongo

from scripts.api.MongoDBCreadentials import mongo_credentials
from scripts.database.CitysDict import get_city_key
from scripts.database.TypeDict import get_type_key
from scripts.utils import DocComparator, DocCleaner
from scripts.helpers.FileHelper import FileHelper
import pprint

from scripts.utils.PrecisionRecall import calculate_precision_recall

file = '../restaurants.tsv'
golden_standart_file = '../golden_standart.tsv'


def main():
    print('Detection started')

    # Read files
    file_helper = FileHelper(file, '\t')
    file_list = file_helper.read_file()

    file_helper = FileHelper(golden_standart_file, '\t')
    golden_list = file_helper.read_file()

    # Clean attributes
    cleaned_items = DocCleaner.clean_doc_list(file_list)

    # Create anthology key for city and type
    list_with_keys = []
    for item in cleaned_items:
        new_item = item.copy()
        new_item['cityKey'] = get_city_key(new_item['city'])
        new_item['typeKey'] = get_type_key(new_item['type'])
        list_with_keys.append(new_item)

    # Compare docs and identify duplicates
    final_list = []
    for i in list_with_keys:
        duplicates_list = []
        for j in list_with_keys:
            if list_with_keys.index(i) != list_with_keys.index(j):
                result = DocComparator.is_doc_similar(i, j)
                if result > 1280:
                    duplicates_list.append(
                        {'keyPair': (list_with_keys.index(i) + 1, list_with_keys.index(j) + 1), 'result': result})
        if len(duplicates_list) > 0:
            for item in duplicates_list:
                if not any(elem['keyPair'] == (item['keyPair'][1], item['keyPair'][0]) for elem in final_list):
                    final_list.append(item)

    # Compare to golden standart (Tuple list) and print results
    results = calculate_precision_recall(golden_list, final_list)
    print('False Positives')
    pprint.pprint(results[0])
    print()
    print('False Negatives')
    pprint.pprint(results[1])

    # Upload results to mongoDB
    client = pymongo.MongoClient(mongo_credentials['connection'])
    db = client[mongo_credentials['database']][mongo_credentials['collection']]

    for item in final_list:
        db.insert_one({'id1': item['keyPair'][0], 'id2': item['keyPair'][1]})


if __name__ == '__main__':
    main()
