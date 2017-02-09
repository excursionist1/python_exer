import pyperclip
import re
import os


# create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._+-]+         # email id
    @                        # @ symbol
    [a-zA-Z0-9._]+           # username
    (\.[a-zA-Z]{2,4}){1,2}   # dot-something
)''', re.VERBOSE)

# find
text = str(pyperclip.paste())

result_list = []

for email in emailRegex.findall(text):
    result_list.append(email[0])

if len(result_list) > 0:
    pyperclip.copy('\n'.join(result_list))
    print('Copied to clipboard:')
    print('\n'.join(result_list))
else :
    print('no email addr')


