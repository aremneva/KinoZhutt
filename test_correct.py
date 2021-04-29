import unittest
import re
import myform

class Test_test_3(unittest.TestCase):
    def test_A(self):
         d_test =myform.my_form()
         self.assertTrue(d_test['cor'])
if __name__ == '__main__':
    unittest.main()
