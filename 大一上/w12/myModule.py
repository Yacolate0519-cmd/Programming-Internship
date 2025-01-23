def fun(n):
    print(n)
    
def fibonacchi_recursisve(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacchi_recursisve(n - 1) + fibonacchi_recursisve(n - 2)

