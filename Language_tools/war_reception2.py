#way 1 by me
tot =int(input())
arr =  list(map(int,input().split()))
arr1 = list(map(int,input().split()))

arr.sort()
arr1.sort()
most_chairs = [1]*tot
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j] and arr[i]<arr1[j]):
            most_chairs[i]+=1
print(max(most_chairs))

#way 2
tot =int(input())
arr =  list(map(int,input().split()))
arr1 = list(map(int,input().split()))
max_chair  = 0
most_chairs1 = []
for i in arr:
    arr_t = [i,0]
    most_chairs1.append(arr_t)
for i in arr1:
    arr_t = [i,0]
    most_chairs1.append(arr_t)
for i in range(tot):
    for j in range(len(most_chairs1)):
        if(most_chairs1[j][0]>=arr[i] and most_chairs1[j][0]<=arr1[i]):
            most_chairs1[j][1]+=1
for i in range(tot):
    if(max_chair<most_chairs1[i][1]):
        max_chair = most_chairs1[i][1]
print(max_chair)
