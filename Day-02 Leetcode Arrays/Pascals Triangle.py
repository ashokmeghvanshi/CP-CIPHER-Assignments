def PascalTriangle(numRows):
    n=numRows
    t=[[1],[1,1]]
    a=[]
    p=[]
    for i in range(1,n+1):
        if i==1:
            a.append([t[0][0]])
        elif i==2:
            a.append([t[1][0],t[1][1]])
        else:
            p=[t[0][0]]
            for j in range(i-2):
                p.append(a[-1][j]+a[-1][j+1])
            p.append(t[0][0])
            a.append(p)
            p=[]
    return a

print(PascalTriangle(7))
