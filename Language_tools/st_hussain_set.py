
que = []
inp1 = list(map(int,input().split()))
inp2 = list(map(int,input().split()))
def hussain_set(arr,que,qur):
    count_m = 0
    arr.sort(reverse=True)
    point = 0
    for i in range(qur):
        ans =0
        curr_m = int(input())
        while(count_m<curr_m):
            if(point <len(arr) and (len(que)==0 or arr[point]>que[0])):
                ans = arr[point]
                point+=1
            else:
                ans = que[0]
                que.pop(0)
            que.append(ans//2)
            count_m+=1
        print(ans)
hussain_set(inp2,que,inp1[1])