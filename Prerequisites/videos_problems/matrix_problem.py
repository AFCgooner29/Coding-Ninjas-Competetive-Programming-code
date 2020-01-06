def all_dialgonal(arr,row,col):
    sum1 = 0
    rev = -1
    for i in range(row):
        sum1+=arr[i][i]
        arr[i][i] = 0
        sum1+=arr[i][rev-i]
        arr[i][rev-i] =0
    return sum1

def all_boundaries(arr,row,col):
    sum1 = 0
    for i in range(row):
        sum1+=arr[i][0]
        arr[i][0]=0
        sum1+=arr[i][-1]
        arr[i][-1] = 0
    
    for  i in range(len(arr[0])):
        sum1+=arr[0][i]
        arr[0][i] = 0
        sum1+=arr[-1][i]
        arr[-1][i] = 0
    sum1+=all_dialgonal(arr,row,col)
    return sum1

inp = int(input())
arr = []
for i in range(inp):
    row = list(map(int,input().split()))
    arr.append(row)

print(all_boundaries(arr,inp,inp))