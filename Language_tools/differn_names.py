def differentNames(names,flag):
    freq={}
    for i in names:
        if(i in freq.keys()):
            freq[i]+=1
            flag=True
        else:
            freq[i]=1
    return freq,flag

# Main
names=input().strip().split()
flag = False
m,flag=differentNames(names,flag)
if flag:
    for key,values in m.items():
        if(values>1):
            print(key+' '+str(values))
else:
    print(-1)
