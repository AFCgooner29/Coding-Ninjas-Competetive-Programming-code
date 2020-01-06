arr = [1,4,10]

def find_sum(arr):
#very smart way sharan
#step 1 : base case is if arr len is 1 then return the value in arr
#step 2 : now len is great than 1 then add first value and recursively 
#call on the remaining array and decrease lenth variable
    if(len(arr)==1):
        return arr[0]
    return arr[0]+find_sum(arr[1:])

def find_sum2(arr,key):
# in this we are using key and when key is equal to len of arr then stop 
# otherwise get element at key and increase the key
    if(key==(len(arr)-1)):
        return arr[key]
    return arr[key]+find_sum2(arr,key+1)


print(find_sum2(arr,0))
print(find_sum(arr))
