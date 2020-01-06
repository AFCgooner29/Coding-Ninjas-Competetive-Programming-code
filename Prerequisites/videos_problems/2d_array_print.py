arr = [[1,2,3,4],[4,2,3,4],[9,54,2,1],[21,2,1,4]]
print("----------------")
def print_alt(arr,row,col):
    for i in range(col):
        if(i%2==0):
            for j in range(row):
                print(arr[j][i])
        else:
            for j in range(row-1,-1,-1):
                print(arr[j][i])
        print("----------------")

print_alt(arr,len(arr),len(arr[0]))


