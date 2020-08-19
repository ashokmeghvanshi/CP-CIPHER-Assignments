
def SortedSquares(A):
    t=[]
    for i in range(len(A)):
        t.append(A[i]*A[i])

    #Bubble Sort
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if t[i]>t[j]:
                t[i],t[j]=t[j],t[i]
    return t

print(SortedSquares([-4,-1,0,3,10]))
