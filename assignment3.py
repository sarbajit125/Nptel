def merge(a,b):
    new=[]
    a_ind,b_ind=0,0
    while a_ind<len(a) and b_ind<len(b):
        if a[a_ind]<b[b_ind]:
            new.append(a[a_ind])
            a_ind+=1
        else:
            new.append(b[b_ind])
            b_ind+=1
    if a_ind==len(a):
        new.extend(b[b_ind:])
    else:
        new.extend(a[a_ind:])
    return new

def mergesort(list1):
    if len(list1)<=1:
        return list1
    left_list,right_list=mergesort(list1[:len(list1)//2]),mergesort(list1[len(list1)//2:])
    return merge(left_list,right_list)

def frequency(list1):
    #sort the array 
    l=mergesort(list1)
    print("Sorted Array is \n",l)
    count={}
    for i in l:
        count[i]=count.get(i,0)+1
    print(count)
    freq=[]
    for key in count:
        k=count.get(key)
        freq.append(k)
    print(freq)
    l2=mergesort(freq)
    print("Frequency sorted:\n",l2)
    minfreq=l2[0]
    print("Min Freq ",minfreq)
    maxfreq=l2[-1]
    print("Max Freq is ",maxfreq)
    minlist=[]
    for key,value in count.items():
        if minfreq==value:
            k=key
            minlist.append(k)
    print(minlist)
    maxlist=[]
    for key,value in count.items():
        if maxfreq==value:
            k=key
            maxlist.append(k)
    print(maxlist)
    finalmin=mergesort(minlist)
    finalmax=mergesort(maxlist)
    return(finalmin,finalmax)

n=int(input("Enter length of list "))
list1=[]
for i in range(n):
    k=int(input("Enter element "))
    list1.append(k)
print("The list is \n",list1)
res=frequency(list1)
print(res)


