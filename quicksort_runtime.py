from random import randint

def create_array(size=10,max=50):
    array=[]
    for i in range(size):
        array.append(randint(0,max))
    return(array)



def quicksort(a):
    if len(a)<=1:
        return a
    smaller,equal,larger=[],[],[]
    pivot=a[randint(0,len(a)-1)]

    for x in a:
        if x<pivot:
            smaller.append(x)
        elif x==pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quicksort(smaller)+equal+quicksort(larger)

a=create_array()
print("unsorted array is :\n",a)
s=quicksort(a)
print("Sorted array is :\n",s)

