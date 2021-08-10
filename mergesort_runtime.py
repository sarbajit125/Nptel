def merge(a,b):
    c=[]
    a_idx,b_idx=0,0
    while a_idx<len(a) and b_idx<len(b):
            if a[a_idx]<b[b_idx]:
                c.append(a[a_idx])
                a_idx+=1
            else:
                c.append(b[b_idx])
                b_idx+=1
    if a_idx==len(a):
            c.extend(b[b_idx:])
    else:
            c.extend(a[a_idx:])
    print(c)
    return c
def mergesort(a):
    if len(a)<=1:
        return a
    left,right=mergesort(a[:len(a)//2]),mergesort(a[len(a)//2:])
    print("left ",left)
    print("right ",right)
    return merge(left,right)


n=int(input("Enter the list length "))
list1=[]
for i in range(n):
    j=int(input("Enter element "))
    list1=list1+[j]
print("The unsorted Array is ",list1)
res=mergesort(list1)
print("The Sorted Array is ",res)
A=[1,2,3]
B=[4,5,6]
res1=merge(A,B)
print(res1)
