inp1=list(map(int,input().split()))
total = 0
for i in range(len(inp1)):
    total+=inp1[i]
arr =set()
freq = {}
for i in range(total):
    var = int(input())
    if(var in freq.keys()):
        arr.add(var)
    else:
        freq[var]=1
print(len(arr))
for i in arr:
    print(i)

#one more way is to sort the inputs and then insert one by one into set where i is equal to i+1