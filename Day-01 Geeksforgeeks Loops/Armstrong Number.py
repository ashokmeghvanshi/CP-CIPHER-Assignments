for _ in range(int(input())):
    n=int(input())
    m=n
    s=0
    while n>0:
        t=n%10
        s=s+t*t*t
        n=n//10
    
    if m==s:
        print('Yes')
    else:
        print('No')
        
