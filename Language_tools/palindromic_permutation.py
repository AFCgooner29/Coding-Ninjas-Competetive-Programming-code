test_case = int(input())
def assign_res(front,end_st,arr,st1,end1,val):
    i=0
    st = st1
    end=end1
    while(i<len(val)):
        arr[st]=val[i]+1
        front+=str(val[i]+1)+' '
        arr[end] =val[i+1]+1
        end_st = ' '+str(val[i+1]+1)
        st+=1
        end-=1
        i+=2
    return

def pal_permu(stt):
    freq ={}
    res = [0]*len(stt)
    for i in range(len(stt)):
        if(stt[i] in freq.keys()):
            freq[stt[i]].append(i)
        else:
            freq[stt[i]] = [i]
    odd=0
    even=0
    start = -1
    end = 0
    front =''
    end_st = ''
    mid_str =''
    for key,value in freq.items():
        if(len(value)%2==0):
            start+=1
            end-=1
            i=0
            while(i<len(value)):
                front+=str(value[i]+1)+' '
                end_st= str(value[i+1]+1)+' '+end_st
                i+=2
            #assign_res(front,end_st,res,start,end,value)
            even+=1
        else:
            odd+=1
    if(odd!=1 and odd!=0):
        print('-1')
        return
    for key,value in freq.items():
        if(len(value)%2!=0):
            mid_str = ''
            for i in value:
                mid_str+=str(i+1)+' '
    mid_str = mid_str[:-1]
    if(mid_str!=''):
        print(front.strip()+' '+mid_str.strip()+' '+end_st.strip())
    else:
        print(front.strip()+' '+end_st.strip())
    return
for i in range(test_case):
    pal_permu(input())



#abxxxab