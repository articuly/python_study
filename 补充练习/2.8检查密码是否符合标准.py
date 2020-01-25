import re

p = 'ABd1234@1,a F1#,2w3E*,2We3345'
lst = []
password = input('please enter some password:')
pw = password.split(',')
for e in pw:
    if 6 <= len(e) <= 12:
        if re.search('[a-z]', e) is not None and re.search('[A-Z]', e) is not None and re.search('[0-9]', e) is not None \
                and re.search('[$#@]', e) is not None:
            lst.append(e)
        print(lst)
