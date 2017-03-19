import pyperclip
from EmailExtractor import EmailExtractor

text = str(pyperclip.paste())

mail_extractor = EmailExtractor(text)

#result_list = mail_extractor.get_mail_with_regex(r'[a-zA-Z]')

res_list = mail_extractor.get_mail_list()
print(res_list)