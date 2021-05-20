import unittest
import re
import myform
import date_test

class Test_test_3(unittest.TestCase):
    def test_A(self): #Тест на корректные даты
        regex_data ="^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.][0-9]{4}\d\d$"
        list_date_cor=["03.08.2020","20.05.2021","12.12.2021","03-05-2020","06/10/2019","31/05/2021"]
        for i in list_date_cor:
            self.assertTrue(date_test.date_cor(i)) #Проверка даты из списка
            
if __name__ == '__main__':
    unittest.main()
