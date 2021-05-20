import unittest
import re
import myform
import date_test

class Test_test_incorrect(unittest.TestCase):
    def test_A(self):   #Тест на некорректные даты
          regex_data ="^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$"
          list_date_incor=["0.08.2020","14.12.200","34.02.2015","3.44.2021","31.13.2020","04..10.2004","07.2013","5.0.212","12.05./2021"]
          for i in list_date_incor:
              self.assertFalse(date_test.date_cor(i)) #Проверка даты из списка
           
if __name__ == '__main__':
    unittest.main()
