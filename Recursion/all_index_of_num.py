arr = [1,2,3,99,4,5,6,3,99,23,4]
num = 99
arr1 = []
#find better way using just two variables
#investigate why none gets printed
def firstIndex(arr,x,key,arr1):
    if(key==(len(arr)-1)):
        if(arr[key]!=x):
            #print('-1')
            return 0
        else:
            arr1.append(key)
            return key
    if(arr[key]==x):
        arr1.append(key)        
    
    firstIndex(arr,x,key+1,arr1)
firstIndex(arr,num,0,arr1)
ans = ''
for i in arr1:
    ans+= str(i)+' '

print(ans[:-1])