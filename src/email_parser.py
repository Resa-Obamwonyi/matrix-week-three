import re

class EmailParser:
    # regex pattern that validate email
    pattern = r'([a-zA-Z0-9+/]+)(@{1})([a-zA-Z0-9]+\.{1}[c][o][m])'
    keys = ['username', 'domain']

    def parse(self, email):
        ''' parse email and return a dictionary of username and domain if valid and return None otherwise'''
        # Add implementation here ...
        identifiedPattern = re.search(self.pattern,email)
        if identifiedPattern:
            new_list = list(identifiedPattern.groups())
            new_list.remove('@')

            self.convert_to_dict(self.keys, new_list)
        else:
            print("Nopity Nope") 


    def convert_to_dict(self, keys, emailList):
        '''
          Takes in two lists as params and return them as a dictionary.'''
        emailDictionary = zip(keys, emailList)
        print(dict(emailDictionary))

testEmail = EmailParser()
testEmail.parse('jane+doe@yahoo.com')