# Calculate the precion and recall, returning a tuple containing false positives and false negatives lists
def calculate_precision_recall(true_positives: list, classifier_duplicates: list) -> tuple:
    false_positives = []
    false_negatives = []
    for item in classifier_duplicates:
        if not any(
                int(item['keyPair'][0]) == int(elem['id1']) and int(item['keyPair'][1]) == int(elem['id2']) for elem in
                true_positives):
            false_positives.append(item)
    for item in true_positives:
        if not any(
                int(elem['keyPair'][0]) == int(item['id1']) and int(elem['keyPair'][1]) == int(item['id2']) for elem in
                classifier_duplicates):
            false_negatives.append(item)
    print('precision: {}'.format(len(true_positives) / (len(true_positives) + len(false_positives))))
    print('recall: {}'.format(len(true_positives) / (len(true_positives) + len(false_negatives))))
    return false_positives, false_negatives
