inp = [-1,2,3,-4,5,-1,4,7,8,-9]
max_sum = 0
curr_sum = 0
def find_max_sum(arr,cur_sum,max_sum,key):
    if(key==(len(arr)-1)):
        if(cur_sum>max_sum):
            return cur_sum
        return max_sum
    cur_sum+=arr[key]
    if(cur_sum>max_sum):
        max_sum =cur_sum
    if(cur_sum<0):
        cur_sum = 0
    return find_max_sum(arr,cur_sum,max_sum,key+1)
print(find_max_sum(inp,curr_sum,max_sum,0))   

for i in inp:
    curr_sum+=i
    if(curr_sum<0):
        curr_sum = 0
    if(curr_sum>max_sum):
        max_sum = curr_sum
print(max_sum)