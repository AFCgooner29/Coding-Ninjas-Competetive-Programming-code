def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
    

print(fib(10))

#not the best way to do it can use DP