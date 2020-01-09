from scripts.database.CitysDict import get_city_key
from scripts.database.TypeDict import get_type_key
from scripts.helpers import DocCleaner, DocComparator
from scripts.helpers.FileHelper import FileHelper
import pprint

from scripts.helpers.PrecisionRecall import calculate_precision_recall

file = '../restaurants.tsv'
golden_standart_file = '../golden_standart.tsv'


def main():
    print('Detection started')
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

    # Compare to golden standart (Tuple list)
    results = calculate_precision_recall(golden_list, final_list)
    print('False Positives')
    pprint.pprint(results[0])
    print()
    print('False Negatives')
    pprint.pprint(results[1])


if __name__ == '__main__':
    main()

    #     Useful section
    #     DocComparator.find_adequate_method('name', DocComparator.is_name_similar, DocCleaner.fix_name)

    # duplicates_list = []
    # for i in list_with_keys:
    #     if list_with_keys.index(i) != 2:
    #         duplicates_list.append((list_with_keys.index(i), DocComparator.is_doc_similar(i, list_with_keys[2])))
    # pprint.pprint(sorted(duplicates_list, key=lambda j: j[1]))

    # results = []
    # for item in golden_list:
    #     results.append(
    #         (item,
    #          DocComparator.is_doc_similar(list_with_keys[int(item['id1']) - 1], list_with_keys[int(item['id2']) - 1])))
    # pprint.pprint(sorted(results, key=lambda i: i[1], reverse=False))
