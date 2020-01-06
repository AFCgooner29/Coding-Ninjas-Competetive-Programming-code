def fun(arr,i):
    if(i==10):
        arr[0]=100
        return
    print(i,arr)
    fun(arr,i+1)
    print(i,arr)
    return

fun([2,2],8)