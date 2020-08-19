l=[3,4,2,0,1,6]
length=len(l)
s=0
if max(l)<=length-1:
        
    for i in range(length):
        if l[l[i]]==i:
            s=s+1
else:
    s=0
if s==length:
    print('Yes array is mirror image')
else:
    print('No array is mirror image')
    
