## Read input as specified in the question.
## Print output as specified in the question.

def counter(x):
    if(x//10==0):
        return 1
    else:
        return 1+counter(x//10)
    
print(counter(int(input())))