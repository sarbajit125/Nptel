def possiblemove(ax,ay,m,n):
    iboard=[]
    x=ax
    y=ay
    for i in range(m):
        for j in range(n):
            k=(i,j)
            iboard.append(k)
    moves=[(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2),(x+1,y-2),(x+2,y-1)]
    print(moves)
    pmoves=[]
    for item in moves:
        if item in iboard:
            pmoves.append(item)
    return(tuple(pmoves))

def explore(s,t,m,n):
    import numpy as np
    board=np.zeros([m,n],dtype=int)
    print(board)
    sx,sy=s
    print(sx)
    print(sy)
    tx,ty=t
    print(tx)
    print(ty)
    board[sx][sy]=1
    print("board",board)
    line=[(sx,sy)]
    print(len(line))
    while line !=[]:
        (ax,ay)=line.pop()
        print((ax,ay))
        d= possiblemove(ax,ay,m,n)
        print(d)
        for (nx,ny) in d:
            if board[nx][ny]==0:
                board[nx][ny]=1
                line.insert(0,(nx,ny))
                print(line)
    return(board[tx][ty])



m=int(input("Enter number of rows "))
n=int(input("Enter number of columns "))
s=(0,0)
t=(1,1)
res=explore(s,t,m,n)
print("Result is ",res)

