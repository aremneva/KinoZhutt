import unittest, checks

class Assert_incorrect_date(unittest.TestCase):
    def test_incorrectDates(self):
        incorrect_dates_list = ['2021-09-01','1999-3-17','2020-02-30','today','99-9-9',
                              '12.01.2020','11/22/2009','20-04-2019','01-07-2010','2016.03.15']
        for date in incorrect_dates_list:
            self.assertFalse(checks.input_check.written_date_correct(date))

if __name__ == '__main__':
    unittest.main()

