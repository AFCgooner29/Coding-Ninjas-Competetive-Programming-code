#900 1000 1100 1030 1600
#1900 1300 1130 1130 1800
tot =input()
arr =  list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr.sort()
arr1.sort()
max_seat = 1
curr_seat = 1
i = 1
j = 0
while (i<len(arr) and j<len(arr1)):
    if(arr[i]<arr1[j]):
        i+=1
        curr_seat+=1
        if(curr_seat>max_seat):
            max_seat=curr_seat
    elif(arr[i]==arr[j]):
        i+=1
        j+=1
        if(curr_seat>max_seat):
            max_seat=curr_seat
    else:
        curr_seat-=1
        j+=1

print(max_seat)

