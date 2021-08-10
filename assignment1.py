def isprime(i):
    fact=[]
    for j in range(1,i+1):
        if (i%j==0):
            fact=fact+[j]
    if fact==[1,i]:
        return(True)

def factors(m):
    i=2
    fact=[]
    product=1
    while i<=m:
        if m%i==0:
            res=isprime(i)
            if res :
                fact=fact+[i]
        i=i+1
    for j in range(len(fact)):
        product=product*fact[j]
        if product==m:
            print(m,"is a primeproduct")
            return(True)

def primeproduct(m):
    if m<=0:
        print("Number is less than 0")
        return(False)
    else:
        factors(m)
m=int(input("Enter a number "))
primeproduct(m)


def delchar(s,c):
    l=list(s)
    if len(c)>1:
        print("Not applicable")
        return False
    while c in l:
        l.remove(c)
    return(''.join(l))

s=input("Enter String ")
c=input("Enter character to be deleted ")
res=delchar(s,c)
print(res)


def shuffle(l1,l2):
    l3=[]
    k=1
    for i in range(0,len(l1)):
        l3.append(l1[i])
    for j in range(0,len(l2)):
        l3.insert(k,l2[j])
        k=k+2
    return(l3)

def shufflelow(l1,l2):
    l3=l1
    k=1
    for j in range(0,len(l2)):
        if k<len(l3):
            l3.insert(k,l2[j])
            k=k+2
        else:
            l3.append(l2[j])
            k=k+2
    return(l3)

l1=[]
l2=[]
m=int(input("Enter of length of l1 "))
n=int(input("Enter of length of l2 "))
for i in range(m):
    k=int(input("Enter element of l1 "))
    l1=l1+[k]
for j in range(n):
    k=int(input("Enter element of l2 "))
    l2=l2+[k]
if m==n:
    res=shuffle(l1,l2)
elif m>n:
    res=shuffle(l1,l2)
elif m<n:
    res=shufflelow(l1,l2)
print(res)

