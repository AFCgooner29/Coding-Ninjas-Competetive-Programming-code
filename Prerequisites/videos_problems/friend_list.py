inp_file = open("input.txt","r")
out_file = open("output.txt","w")
inp =[]
tot = [0]*7
for each in inp_file:
    inp.append(each.replace('\n',''))

for i in range(1,int(inp[0])+1):
    temp = list(map(int,inp[i].split()))
    for i in temp:
        tot[i]+=1
maxi = max(tot) 
for i in range(len(tot)):
    if(tot[i]==maxi):
        out_file.write(str(i)+"\n")
