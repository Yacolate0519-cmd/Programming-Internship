def func1(start,*args,**kwargs):
    print(start,'\n')
    for i in args:
        print(i,end='\t')
    print('\n')
    
    for key in kwargs:
        print(f'kwargs[{key}] = {kwargs[key]}')
        
func1(100 , 23 , 19 , 44 , 8 , a = 8 , name = 'david' , major = 'computer science')