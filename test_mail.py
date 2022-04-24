import unittest
from myform import shame, checkmail

class Test_testmail(unittest.TestCase):
    def test_Bad(self):
        self.assertFalse(shame.match("worst@..."))

    def test_Good(self):
        self.assertTrue(shame.match("best@gmail.com"))        
        
    def test_Testcheckmail(self):
        choice = [
                  ("what a question?","aaa777@mail.ru"),
                  ("what a problem?","shine35@gmail.com"),
                  ("Are you have ?","fastback@hotmail.net"),
                  ("Question?", "qstn@aus.com")
                  ]                        
        for(quest,mail) in choice:
           self.assertIsNone(checkmail(quest, mail))         
           

if __name__ == '__main__':
    unittest.main()
