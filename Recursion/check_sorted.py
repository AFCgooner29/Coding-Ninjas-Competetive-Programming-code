def is_sorted(arr,key):
    if(key==(len(arr)-1)):
        #print('true')
        return True
    else:
        if(arr[key]<arr[key+1]):
            is_sorted(arr,key+1)
        else:
            #print('false')
            return False


arr = [1,2,3,4,5,6,1]
if(is_sorted(arr,0)):
    print("Sorted")
else:
    print('Notsorted')