import unittest
from word_counter import count_words, common_occurance

class TestWordCounter(unittest.TestCase):
    words = [u'const.', u'daniel', u'montsion\u2019s', u'defence', u'team', u'has', u'formally', u'asked', u'for', u'a', u'stay', u'on', u'all', u'charges', u'after', u'serving', u'court', u'with', u'a', u'charter', u'application', u'alleging', u'evidence', u'was', u'\u201clost', u'or', u'destroyed\u201d', u'and', u'alleging', u'\u201cabuse', u'of', u'process\u201d', u'in', u'the', u'mishandling', u'of', u'critical', u'video', u'evidence', u'showing', u'the', u'fatal', u'arrest', u'of', u'abdirahman', u'abdi.', u'the', u'defence', u'team', u'of', u'michael', u'edelson', u'and', u'solomon', u'friedman', u'on', u'wednesday', u'served', u'court', u'with', u'the', u'application,', u'one', u'of', u'three', u'potential', u'charter', u'motions', u'the', u'defence', u'told', u'the', u'judge', u'it', u'was', u'considering', u'back', u'in', u'the', u'opening', u'days', u'of', u'the', u'trial.', u'that', u'notice', u'followed', u'the', u'\u201cbombshell\u201d', u'disclosure', u'of', u'alternate', u'versions', u'of', u'cctv', u'video', u'footage,', u'which', u'was', u'used', u'by', u'special', u'investigations', u'unit', u'investigators,',
u'and', u'has', u'been', u'acknowledged', u'by', u'all', u'parties', u'as', u'a', u'\u201ccentrepiece\u201d', u'of', u'the', u'manslaughter', u'and', u'assault',
u'case', u'against', u'montsion.', u'he', u'has', u'pleaded', u'not', u'guilty', u'to', u'all', u'charges,', u'and', u'his', u'defence', u'team', u'is', u'now', u'asking', u'ontario', u'court', u'justice', u'robert', u'kelly', u'to', u'bring', u'about', u'a', u'swift', u'end', u'to', u'the', u'ottawa', u'officer\u2019s', u'trial.']
    def test_count_words(self):
        count = 154
        result = count_words(self.words)
        self.assertEqual(result, count)

    def test_common_occurance(self):
        data = [(u'the', 11), (u'of', 9), (u'and', 5), (u'defence', 4), (u'a', 4), (u'all', 3), (u'team', 3), (u'to', 3), (u'was', 3), (u'has', 3)]
        result = common_occurance(self.words)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()