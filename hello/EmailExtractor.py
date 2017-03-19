import re

class EmailExtractor:

    def __init__(self, text):
        self.text = text

    def get_mail_with_regex(selfself, regex_text):
        re.compile(regex_text)

        return

    def get_mail_list(self):
        result_list = []

        # create email regex
        emailRegex = re.compile(r'''(
            [a-zA-Z0-9._+-]+         # email id
            @                        # @ symbol
            [a-zA-Z0-9._]+           # username
            (\.[a-zA-Z]{2,4}){1,2}   # dot-something
        )''', re.VERBOSE)

        for email in emailRegex.findall(self.text):
            result_list.append(email[0])

        return emailRegex