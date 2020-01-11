#Problem
#given a array, print the product array such that 
#all elements at A is product of all elements other than A[i]
#for eg A =[1,2,4]
#answ is [8,4,2]
#without using divide operator
# in o(1) space
def easy_way(arr):
    mult = 1
    for i in arr:
        mult*=i
    for i in range(len(arr)):
        arr[i] = mult//arr[i]
    return arr

def space_complexity_violated(arr):
    LP = []
    RP = [0]*len(arr)
    mult =1
    LP.append(1)
    RP[-1] =1
    for i in range(0,len(arr)-1):
        LP.append(LP[i-1]*arr[i])
    for i in range(len(arr)-1,0,-1):
        RP[i-1] = RP[i]*arr[i]
    for i in range(len(arr)):
        arr[i] = LP[i]*RP[i]
    print(arr)
#space_complexity_violated([1,2,4])

def optimal_method(arr):
    left_element = 1
    right_element = 1
    prod = [0]*len(arr)
    #Left Product
    for i in range(len(arr)):
        temp = left_element
        left_element*=arr[i]
        prod[i] = temp
    for i in range(len(arr)-1,-1,-1):
        prod[i]*=right_element
        right_element*= arr[i] 
    print(prod)
optimal_method([1,2,4])
