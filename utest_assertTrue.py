import unittest, re, checks

class AssertTrueTest(unittest.TestCase):
    def test_realEmails(self):
        list_mail_cor = ['mail@mail.com', 'm_ail@writeHere.ru.com', 'Mike.Smith@jobHunters.net', 'correctEmail@mailCheck.co']
        for mail in list_mail_cor:
            self.assertTrue(checks.input_check.mail_correct(mail))

if __name__ == '__main__':
    unittest.main()

