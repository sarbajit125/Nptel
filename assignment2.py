
def contracting(l):
    n=len(l)
    print(n)
    i=0
    l2=[]
    while i<n:
        if i== 0:
            diff=abs(l[i])
            l2=l2+[diff]
            print(l2)
        else:
            diff=abs(l[i-1]-l[i])
            l2=l2+[diff]
            print("l2 after ",i,"th iteration is ",l2)
            if l2[i]>=l2[i-1]:
                return False
        i=i+1
    return True

def counthv(l):
    n=len(l)
    i=1
    counthill=0
    countvall=0
    while i<n-1:
            if l[i]>l[i-1]and l[i]>l[i+1]:
                counthill=counthill+1
            if l[i]<l[i-1]and l[i]<l[i+1]:
                countvall=countvall+1
            i=i+1
    return(counthill,countvall)

def leftrotate(m):
    r=len(m)
    c=len(m[0])
    new=[]
    for i in range(r):
        temp=[]
        for j in range(c):
            temp.append(m[j][i])
        new.insert(0,temp)

    return(new)
list=[]
n=int(input("Enter total No of elements "))
for i in range(n):
    i=int(input("Enter element of list "))
    list=list+[i]
res=contracting(list)
res1=counthv(list)
print(res)
print("Print no of hills and valleys ",res1)
print("\n")
print("Matrix Code")
m=int(input("Enter no of rows "))
n=int(input("Enter no of columns "))
matrix=[]
for i in range(0,m):
    rows=[]
    for j in range(0,n):
        print("Enter element in (",i,j,") position ",end='')
        k=int(input(""))
        rows.append(k)
    matrix.append(rows)
res2=leftrotate(matrix)
print("Result after left rotation is\n",res2)




