import bisect
test_case = int(input())
def lower_bound(arr,val):
    mid = len(arr)//2
    if(arr[mid][0]>val and arr[mid-1][0]<val):
        return mid-1
    elif(arr[mid][0]>val):
        return lower_bound(arr[:mid],val)
    else:
        return lower_bound(arr[mid:],val)
def lower_bound2(arr,start,end,val):
    mid = (start+end)//2
    if(arr[mid][0]==val):
        return mid 
    elif(arr[mid][0]>val):
        return lower_bound2(arr,start,mid,val)
    else:
        return lower_bound2(arr,mid+1,end,val)


def finder(arr,arr2,time):
    arr.sort()
    arr2.sort()
my_arr = [1,3,5,6,8,9]
i = bisect.bisect_left(my_arr,2)
print(i)



    



# for i in range(test_case):
#     n_m = list(map(int,input().split()))
#     in_times = []
#     out_times = []
#     for j in range(n_m[0]):
#         temp = list(map(int,input().split()))
#         in_times.append(temp)
#     for j in range(n_m[1]):
#         finder(in_times,int(input()))
        
