import unittest
import myform
class Test_test_partner(unittest.TestCase):
    def test_true_description(self):
        list_description_t = ["our company", "company", "ford motor company", "restaurant chain",
                        "business partner", "our company has been in existence since 1996"]
        for y in list_description_t:
            self.assertTrue(myform.IsCorrectdescriptionT(y))


    def test_false_description(self):
        list_description_f = ["рсшыврсыв", "sfdsvfhjljnbdghjkhfbf", "ccccccccccc", "czcdscd@vfsvfsv.cvv",
                        "HGHGHGHGBCCDNCLASIFOEICOAIODS", "k3;6k3k4kfk44", "   44r4    55u7fsgtr  ", "fddffvcx fdfbd",
                       "", "      ", "v", "y-10-20", 
                       "f)", "grrrtr"]
        for y in list_description_f:
            self.assertFalse(myform.IsCorrectdescriptionF(y))


    def test_mail_T(self):
        list_email_t = ["aaa@mail.ru", "johnwilliams@gmail.com", "moscow23@yahoo.com"]
        for y in list_email_t:
            self.assertTrue(myform.isCorrectmailTrue(y))

    def test_mail_F(self):
        list_email_f = ["@mail.ru", "2222@rd@.cr", "456@bbvvvvv", "", "';.//;", "fe", "hb", "334"]
        for y in list_email_f:
            self.assertFalse(myform.isCorrectmailFalse(y))





if __name__ == '__main__':
    unittest.main()
