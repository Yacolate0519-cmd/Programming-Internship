import re 
txt = input('Password: ')

if re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[$#@])[a-zA-Z\d$#@]{8,}$' , txt):
    print('Match the rule')
else:
    print('Not match the rule')
    