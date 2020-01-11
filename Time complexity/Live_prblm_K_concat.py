
def post_max_sum(arr):
    cur_sum = 0
    max_sum = 0
    for i in range(len(arr)-1,-1,-1):
        cur_sum+=arr[i]
        if(cur_sum>max_sum):
            max_sum = cur_sum
    return max_sum
def pre_max_sum(arr):
    cur_sum = 0
    max_sum = 0
    for i in range(0,len(arr)):
        cur_sum+=arr[i]
        if(cur_sum>max_sum):
            max_sum = cur_sum
    return max_sum
def kadenes(arr):
    cur_sum = 0
    max_sum = 0
    for i in range(0,len(arr)):
        cur_sum+=arr[i]
        if(cur_sum>max_sum):
            max_sum = cur_sum
        if(cur_sum<0):
            cur_sum =0
    return max_sum

def k_concat(arr,k):
    max_sum = 0
    sum_arr = sum(arr)
    if(k==1):
        return kadenes(arr)
    if(sum_arr>=0):
        max_sum+=max((k-2)*sum_arr+pre_max_sum(arr)+post_max_sum(arr),kadenes(arr))
    else:
        max_sum+=max(pre_max_sum(arr)+post_max_sum(arr),kadenes(arr))
    return max_sum

def k_concat2(arr,k):
    kadenes_sum = kadenes(arr)
    cur_sum = 0
    max_suffix_sum = 0
    max_prefix_sum = 0
    tot_sum = 0
    for i in range(len(arr)-1,-1,-1):
        cur_sum+=arr[i]
        max_suffix_sum = max(cur_sum,max_suffix_sum)
    tot_sum = cur_sum
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum+=arr[i]
        max_prefix_sum = max(cur_sum,max_prefix_sum)
    if(tot_sum<0):
        return max(max_prefix_sum+max_suffix_sum,kadenes_sum)
    else:
        return max(max_prefix_sum+max_suffix_sum+(tot_sum*(k-2)),kadenes_sum)


test_case = int(input())
for i in range(test_case):
    params = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(k_concat(arr,params[1]), end='\n')

