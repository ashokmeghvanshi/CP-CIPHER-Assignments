
def fibonacci(n):
    a=[0,1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        
        for i in range(2,n):
            a.append(a[i-1]+a[i-2])
        
    return a[-1]+a[-2]

print(fibonacci(4))
