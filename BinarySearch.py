from ast import If


def ssort(seq):
    r=len(seq)
    for i in range(r):
        minpos=i
        for s in range(i+1,r):
            if seq[minpos]>seq[s]:
                minpos=s
        seq[i],seq[minpos]=seq[minpos],seq[i]
    print("Selection sorted array ",seq)
def bsearch(seq,s,e,x):
    mid=s+e//2
    if x==seq[mid]:
        return(mid)
    elif x<seq[mid]:
        return(bsearch(seq,0,mid,x))
    else:
        return(bsearch(seq,mid+1,e))
seq=[21,44,32,59,81,69]
x=32
ssort(seq)
result=bsearch(seq,1,len(seq),32)
print("postion of ",x," is ",result+1)
