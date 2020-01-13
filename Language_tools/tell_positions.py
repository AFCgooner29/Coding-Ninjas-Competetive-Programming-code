inp = int(input())

students = []

for i in range(inp):
    arr = input().split()
    student = []
    student.append(arr[0])
    student.append(sum(list(map(int,arr[1:]))))
    students.append(student)
#below is sorting list based on second value for sub array
#still to implement when two marks are same then sort on base of roll no
students.sort(key= lambda pair: pair[1],reverse=True)
rank  = 1
for i in students:
    print(rank,i[0])
    rank+=1


def find_roll_no(arr):
    roll_no = []
    for i in range(len(arr)):
        asc = 0
        for j in arr[i]:
            asc+=ord(j)
        roll_no.append(asc)
        
    return roll_no


