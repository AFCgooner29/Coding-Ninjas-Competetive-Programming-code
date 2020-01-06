def print_num(x):
    if(x==1):
        return '1'
    else:
        return print_num(x-1)+" "+str(x)

from sys import setrecursionlimit
setrecursionlimit(11000)
print(print_num(int(input())))

#what is the max recursion depth in python??
#it is 1000