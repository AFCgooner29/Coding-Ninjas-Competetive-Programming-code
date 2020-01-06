arr = [1,2,3,99,4,5,6,3,23,4]
num = 99

#find better way using just two variables
#investigate why none gets printed
def firstIndex(arr,x,key):
    if(key==(len(arr)-1)):
        if(arr[key]!=x):
            print('-1')
            return 0
        else:
            print(key)
            return key
    if(arr[key]==x):
        print(key)
        return key
    else:
        firstIndex(arr,x,key+1)
firstIndex(arr,num,0)
