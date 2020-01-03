

def tak_tak(n):
    i =0 
    while(n%11!=1):
        n =2*n
        i+=1
    return str(i)+" "+str(n)

print(tak_tak(17))