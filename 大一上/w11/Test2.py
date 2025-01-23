def fibonacchi_recursisve(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacchi_recursisve(n - 1) + fibonacchi_recursisve(n - 2)
print(fibonacchi_recursisve(5))