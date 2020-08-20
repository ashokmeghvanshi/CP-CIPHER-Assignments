def LargestWordinDictionary():
    
    for _ in range(int(input())):

        a=int(input())

        stringlist=input().split()

        string=input()

        templist=[]
        
        for i in stringlist:

            templength=0

            for j in i:

                if j in string:

                    templength = templength + 1

            if templength == len(i):

                templist.append(i)
        
        max_len = -1

        for element in templist: 

            if len(element) > max_len: 

                max_len = len(element) 

                result = element 

        print(result)
LargestWordinDictionary()
