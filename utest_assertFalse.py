import unittest, re, myform_mail

class AssertFalseTest(unittest.TestCase):

    def test_realEmails(self):
        list_mail_cor = ['some@mail', 'some@mail.', '@mail.ru', 'incorrectMail@@mailCheck.point']
        
        for mail in list_mail_cor:
            self.assertFalse(myform_mail.mailCheck.match(mail))

if __name__ == '__main__':
    unittest.main()
