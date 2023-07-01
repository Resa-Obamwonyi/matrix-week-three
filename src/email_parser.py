import re
import unittest

class EmailParser:
    # regex pattern that validate email
    pattern = r'([a-zA-Z0-9+/]+)(@{1})([a-zA-Z0-9]+\.{1}[c][o][m])'
    keys = ['username', 'domain']

    def parse(self, email):
        ''' parse email and return a dictionary of username and domain if valid and return None otherwise'''
        # Add implementation here ...
        self.email = email
        identifiedPattern = re.search(self.pattern,email)
        
        if identifiedPattern:
            email_split = list(identifiedPattern.groups())
            email_split.remove('@')

            self.convert_to_dict(self.keys, email_split)

        else:
            return None


    def convert_to_dict(self, keys, email_split):
        '''
          Takes in two lists as params and return them as a dictionary.'''
        emailDictionary = zip(keys, email_split)
        print(dict(emailDictionary))



testEmail = EmailParser()
testEmail.parse('jane+doe@yahoo.com')
print(testEmail.parse('jane+doeyahoo.com'))
