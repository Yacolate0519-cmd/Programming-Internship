import re

'''

def good_function()
    print("Hello")
if x > 10
    print("Greater")
for i range(5):
    print(i)

'''

if __name__ == "__main__":
    with open('sample_code.txt' , 'r') as e:
        data = e.read()
        
        # brackets_error = r'^def (\w+)(?!\().*' # ()
        # if_error = r'^if [^\:]+(?!\s*:$).*' # if 

        # brackets_error = r'^def (\w+)(?!\(\))'
        brackets_error = r'^def (\w+)(?!\(\))'

        if_error = r'^if .+[^:](?!\s*:)'    

        brackets_error = re.findall(brackets_error , data)
        if_error = re.findall(if_error , data)
        
        print('This is brackets_error:')
        for i in brackets_error:
            print(i)
            
        print()

        print('This is if_error:')
        for i in if_error:
            print(i)
