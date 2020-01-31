def uniqueChars(string):
    s1 ={}
    res=''
    for i in string:
        if(i not in s1.keys()):
            res=res+i
            s1[i]=1
    return res

# Main
string = input()
uniqueChars(string)
