for _ in range(int(input())):

    a=int(input())

    arr=list(map(int,input().split()))

    k=int(input())
        
    count=0

    for i in arr:

        if i<=k:

            count=count+1

    min_swap=1000000

    for i in range(a-count+1):

        temp=0

        for j in arr[i:i+count]:

            if j>k:

                temp=temp+1

        if temp<min_swap:

            min_swap=temp

    print(min_swap)
    
