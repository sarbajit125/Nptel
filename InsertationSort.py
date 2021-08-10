def isort(seq):
    for i in range(len(seq)):
        pos=i
        while pos>1 and seq[i]<seq[i-1]:
            seq[i],seq[i-1]=seq[i-1],seq[i]
            pos=pos-1
    print("Inserted List is ",seq)
seq=[21,44,32,57,81,69]
isort(seq)

