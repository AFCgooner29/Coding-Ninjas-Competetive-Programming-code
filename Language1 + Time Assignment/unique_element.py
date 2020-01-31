""" Find the Unique Element
Send Feedback
Given an integer array of size 2N + 1. In this given array, N numbers are present twice and one number is present only once in the array.
You need to find and return that number which is unique in the array.
Note : Given array will always contain odd number of elements.
Input format :
Line 1 : Array size i.e. 2N+1
Line 2 : Array elements (separated by space)
Output Format :
Unique element present in the array
Constraints :
1 <= N <= 10^6
Sample Input :
7
2 3 1 6 3 6 2
Sample Output :
1
 """

def FindUnique(arr,n):
    freq = {}
    sum1 = 0
    sum2 = 0
    for i in arr:
        sum1+=i
        if(i in freq.keys()):
            freq[i]+= 1
            sum2+= 2*i
        else:
            freq[i] = 1
    return sum1-sum2

            

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr,n)
print(unique)
