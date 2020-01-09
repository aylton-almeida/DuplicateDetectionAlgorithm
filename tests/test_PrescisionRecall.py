import unittest

from scripts.helpers import PrecisionRecall


class MyTestCase(unittest.TestCase):
    def test_calculate_precision_recall(self):
        true_positives = [
            {'id1': 1, 'id2': 2},
            {'id1': 3, 'id2': 4},
            {'id1': 5, 'id2': 6},
        ]

        classiefer_duplicates = [
            {'keyPair': (1, 2)},
            {'keyPair': (3, 4)},
            {'keyPair': (6, 5)},
            {'keyPair': (6, 7)},
        ]

        false_positives, false_negatives = PrecisionRecall.calculate_precision_recall(true_positives,
                                                                                      classiefer_duplicates)

        self.assertEqual([{'keyPair': (6, 5)}, {'keyPair': (6, 7)}], false_positives)
        self.assertEqual([{'id1': 5, 'id2': 6}], false_negatives)


if __name__ == '__main__':
    unittest.main()
