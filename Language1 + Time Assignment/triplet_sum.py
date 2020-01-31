""" Triplet sum
Send Feedback
Given a random integer array and a number x. 
Find and print the triplets of elements in the array which sum to x.
While printing a triplet, print the smallest element first.
That is, if a valid triplet is (6, 5, 10) print "5 6 10". 
There is no constraint that out of 5 triplets which have to be printed on 1st line. 
You can print triplets in any order, just be careful about the order of elements in a triplet.

Input format :
Line 1 : Integer N (Array Size)
Line 2 : Array elements (separated by space)
Line 3 : Integer x
Output format :
Line 1 : Triplet 1 elements (separated by space)
Line 2 : Triplet 3 elements (separated by space)
Line 3 : and so on
Constraints :
1 <= N <= 1000
1 <= x <= 100
Sample Input:
7
1 2 3 4 5 6 7 
12
Sample Output ;
1 4 7
1 5 6
2 3 7
2 4 6
3 4 5 """
from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

tot = int(input())
arr = list(map(int,input().split()))
sum_req = int(input())
arr.sort()
sum_1 = 0
def find_sum(arr,sum_req):
    i = 0
    j = 0
    for i in range(len(arr)):
        if(arr[i]>=sum_req):
            break
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]>=sum_req):
                break
            for k in range(j+1,len(arr)):
                if(arr[i]+arr[j]+arr[k]==sum_req):
                    print(str(arr[i])+' '+str(arr[j])+' '+str(arr[k]))
                elif (arr[i]+arr[j]+arr[k]<sum_req):
                    continue
                else:
                    break

def find_sum_search(arr,sum_req):
    #still n^3
    #freq added to take care of multiple last elements
    i = 0
    j = 0
    res = -1
    freq = {}
    for i in arr:
        if(i in freq.keys()):
            freq[i]+=1
        else:
            freq[i] = 1

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum_rem =sum_req - arr[i] - arr[j]
            res = BinarySearch(arr[j+1:],sum_rem)
            if(res==-1):
                continue
            else:
                for i in range(freq[sum_rem]):
                    print(str(arr[i])+' '+str(arr[j])+' '+str(sum_rem))
                continue
def find_sum_sorted(arr,sum_req):
    for i in range(len(arr)-1):
        l = i+1
        r = len(arr)-1
        while(l<r):
            if(arr[i]+arr[l]+arr[r]==sum_req):
                print(str(arr[i])+' '+str(arr[j])+' '+str(arr[r]))
                l+=1
                r-=1
            elif(arr[i]+arr[l]+arr[r]<sum_req):
                l+=1
            else:
                r-=1



#find_sum(arr,sum_req)
find_sum_search(arr,sum_req)