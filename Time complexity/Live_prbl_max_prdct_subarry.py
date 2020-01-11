#max product subarry
#first lets try max product of non negative arry

def max_product_pstive_arry(arr):
    max_prdct = 1
    cur_prdct = 1
    for i in range(len(arr)):
        cur_prdct*=arr[i]
        if(cur_prdct==0):
            cur_prdct =1
        max_prdct =max(max_prdct,cur_prdct)
    return max_prdct
def max_product(arr):
    max_prdct = 1
    cur_prdct = 1
    neg_prd = 1
    
    for i in range(len(arr)):
        flag = 0
        cur_prdct*=arr[i]
        if(cur_prdct<0):
            if(neg_prd==1):
                flag=1
                neg_prd = cur_prdct
            cur_prdct = 1
        if(cur_prdct==0):
            cur_prdct =1
        if(neg_prd!=1):
            if(flag!=1):
                neg_prd*=arr[i]
            if(neg_prd>0):
                max_prdct =max(max_prdct,cur_prdct,neg_prd)        
                cur_prdct =neg_prd
                neg_prd =1
        max_prdct =max(max_prdct,cur_prdct,neg_prd)
    return max_prdct
def max_product2(arr):
    max_prdct = 1
    cur_prdct = 1
    neg_prd = 1
    for i in arr:
        if(i>0):
            cur_prdct*=i
            neg_prd = min(neg_prd*i,1)
        elif(i==0):
            cur_prdct = 1
            neg_prd =1
        else:
            temp = cur_prdct
            cur_prdct = max(neg_prd*i,1)
            neg_prd = temp*i
        max_prdct = max(cur_prdct,max_prdct)
    return max_prdct    
print(max_product([1,2,3,4,-50,600,-1,0,9,10000]))
print(max_product2([1,2,3,4,-50,600,-1,0,9,10000]))