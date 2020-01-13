tot=input()
stt = input()
a = 0
s = 0
p = 0
for i in stt:
    if(i=='a'):
        a+=1
    elif (i=='s'):
        s+=1
    elif(i=='p'):
        p+=1
print(str(a)+' '+str(s)+' '+str(p))