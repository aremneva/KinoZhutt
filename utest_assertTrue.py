import unittest, re, myform_mail

class AssertTrueTest(unittest.TestCase):
    def test_realEmails(self):
        list_mail_cor = ['mail@mail.com', 'm_ail@writeHere.ru.com', 'Mike.Smith@jobHunters.net', 'correctEmail@mailCheck.co']
        regex = re.compile('^[A-Za-z0-9\._]+@[A-Za-z0-9]+(\.[A-Za-z]+)+$')
        for mail in list_mail_cor:
            self.assertTrue(myform_mail.mailCheck.match(mail))

if __name__ == '__main__':
    unittest.main()

