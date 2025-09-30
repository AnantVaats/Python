def factorial(n):
    if n==0:
        return 1
    else:
        #recursive function
        return n * factorial(n-1)

print(factorial(5))