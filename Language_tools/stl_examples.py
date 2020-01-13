## to remove duplicates from a array
set1 =set()
arr = [1,2,3,4,5,6,7,8,9,2,3,5,6,2,1,3,6,3,2,1,4,6,7,8]
arr1 = [1,2,3,4,5,6,7,8,9,2,3,5,6,2,1,3,6,3,2,1,4,6,7,8]
arr1.sort()
def remove_using_set(set1,arr):
# O(n) space
# O(n) Time
    res = []
    for i in arr:
        set1.add(i)
    for i in set1:
        res.append(i)
    return res
print(remove_using_set(set1,arr))
def just_using_array(arr):
    res = []
    res.append(arr[0])
    for i in range(1,len(arr)):
        if(arr[i-1]!=arr[i]):
            res.append(arr[i])
    return res
print(just_using_array(arr1))

def find_frequency(arr):
    freq = {}
    for i in arr:
        if(i in freq.keys()):
            freq[i]+=1
        else:
            freq[i] = 1
    return freq
print(find_frequency(arr1))