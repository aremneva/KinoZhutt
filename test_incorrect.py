import unittest
import re
import myform

class Test_test_incorrect(unittest.TestCase):
    def test_A(self):
        d_test =myform.my_form()
        self.assertFalse(d_test['incor'])
if __name__ == '__main__':
    unittest.main()
