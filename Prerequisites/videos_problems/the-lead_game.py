inp = int(input())
p1 = []
p2 = []
p1_lead = 0
p2_lead = 0
for i in range(inp):
    scores = list(map(int,input().split()))
    if(i==0):
        p1.append(scores[0])
        p2.append(scores[1])
    else:
        p1.append(scores[0]+p1[i-1])
        p2.append(scores[1]+p2[i-1])
    if(p1[i]>p2[i] and p1_lead<(p1[i] - p2[i])):
        p1_lead = p1[i] - p2[i]
    elif(p2[i]>p1[i] and p2_lead<(p2[i] - p1[i])):
        p2_lead = p2[i] - p1[i]
if(p1_lead>p2_lead):
    print ("1 "+str(p1_lead))
else:
    print ("2 "+str(p2_lead))