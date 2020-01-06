
inp = list(map(int,input().split()))
arr = list(map(int,input().split()))
def c_sum(arr,summ):
    sum1 = 0
    for i in range(len(arr)):
        sum1=arr[i]
        str3 = str(arr[i])
        if(sum1==summ):
            print("true")
            print(str3)
            return 0
        for j in range(i+1,len(arr)):
            sum1+=arr[j]
            str3+=" "+str(arr[j])
            if(sum1==summ):
                print("true")
                print(str3)
                return 0
    print("false")
    return 0

c_sum(arr,inp[1])