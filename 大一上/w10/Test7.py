def add(a,b):
	return a + b

def sub(a,b):
    return a - b

def run(func,a,b):
	return func(a,b)

k = run(add,10,20)
x = run(lambda a , b : a - b , 10 , 20)
t = run(lambda a , b : a * b , 10 , 20)
c = run(lambda a , b : a / b , 10 , 20)
a = run(lambda a , b : a % b , 10 , 100)

print('k=',k)
print('a=',x)
print(t,'\n',c,'\n',a)