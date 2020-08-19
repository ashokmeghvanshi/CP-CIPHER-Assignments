
def EquilibriumIndex(array):
    
    length = len(array)

    for i in range(length):
        leftpartsum = 0
        rightpartsum = 0

        for j in range(i):
            leftpartsum = leftpartsum + array[j]

        for j in range(i+1,length):
            rightpartsum = rightpartsum + array[j]

        if leftpartsum == rightpartsum:
            return i 
	
    return -1
			
array = [-7, 1, 5, 2, -4, 3, 0]
index=EquilibriumIndex(array)

if index!=-1:
    print('Equilibrium Index of Array is',index)
else:
    print('Equilibrium Index Not Exist Array')
