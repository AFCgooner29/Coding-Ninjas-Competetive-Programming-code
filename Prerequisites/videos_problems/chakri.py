tot = input()
inp = list(map(int,input().split()))
minn = 100000000
pos = -99
max_prof = 0
for i in range(len(inp)):
    profit = 0
    for j in range(i+1,len(inp)):
        profit= inp[j]-inp[i]
        if(profit>max_prof):
            max_prof = profit
print(max_prof) 