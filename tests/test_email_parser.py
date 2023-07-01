# Import all required modules
import unittest
import sys
sys.path.append('/Users/shee/Desktop/courses/we-tech-python tasks/matrix-week-three')
from src.email_parser import EmailParser


class Test(unittest.TestCase):
    testingParse = EmailParser()
    regexPattern = '([a-zA-Z0-9+/]+)(@{1})([a-zA-Z0-9]+\.{1}[c][o][m])'
    
    def test_parse(self):
        # pass
        self.assertRegex('jane+doe@yahoo.com', self.regexPattern, self.testingParse.parse(email='jane+doe@yahoo.com'))
        self.assertRegex('johndoe@bz2.com', self.regexPattern,  self.testingParse.parse(email='johndoe@gmail.com'))


if __name__ == '__main__':
    unittest.main()

