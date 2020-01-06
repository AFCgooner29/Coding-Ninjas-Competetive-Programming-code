arr = [2]*1000
num = 21
arr[0] = 21
def find(arr,x):
#this is the one way of recursively doing things in array
#this wont provide the index values of the value find
    if(len(arr)==1):
        if(arr[0]==x):
            return True
        else:
            return False
    if(arr[0]!=x):
        return find(arr[1:],x)
    else:
        return True

from sys import setrecursionlimit
setrecursionlimit(11000)
if(find(arr,num)):
    print('Is There')
else:
    print('Not')