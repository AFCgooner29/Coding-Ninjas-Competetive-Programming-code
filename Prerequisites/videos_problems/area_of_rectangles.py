rec1 = list(map(int,input().split()))
rec2 = list(map(int,input().split()))

def find_areas(x1,y1,x2,y2,x3,y3,x4,y4):
    l1 = x2-x1
    b1 = y2-y1
    l2 = x4-x3
    b2 = y4-y3
    area1 = l1*b1
    area2 = l2*b2
    bottom = max(x1,x3)
    left = max(y1,y3)
    top = min(x2,x4)
    right = min(y2,y4)
    int_ar = 0
    if((top>bottom) and (left<right)):
        int_ar = (top-bottom)*(right-left)    
    return (area1+area2-int_ar)

print(find_areas(rec1[0],rec1[1],rec1[2],rec1[3],rec2[0],rec2[1],rec2[2],rec2[3]))
