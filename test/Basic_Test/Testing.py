import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal 


class Testing(unittest.TestCase):
    def setUp(self):
        """ Your setUp """
        TEST_INPUT_DIR = 'output/'
        test_file_name =  'testdata.csv'
        try:
            data = pd.read_csv("")
        except IOError:
            print("cannot open file")
        self.fixture = data

    def test_over_weight_count(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_dataFrame_constructedAsExpected(self):
        """ Test that the dataframe read in equals what you expect"""
        foo = pd.DataFrame()
        assert_frame_equal(self.fixture, foo)

if __name__ == '__main__':
    unittest.main()