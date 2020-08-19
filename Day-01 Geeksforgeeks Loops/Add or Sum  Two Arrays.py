for _ in range(int(input())):
    a1=int(input())
    a=list(map(int,input().split()))
    b1=int(input())
    b=list(map(int,input().split()))
    
    la=len(a)
    lb=len(b)
        
    if la<lb:
        t=lb-la
        a=[0]*t + a
    else:
        t=la-lb
        b=[0]*t + b
    
    # 
    c=0
    
    length=len(a)
            
    s=''
    for i in range(length-1,-1,-1):
        t=a[i]+b[i]+c
        if t<10:
            s=str(t)+s
            c=0
        else:
            s=str(t%10)+s
            c=t//10
        #print(t,s,c)
    s=str(c)+s
    print(int(s))
