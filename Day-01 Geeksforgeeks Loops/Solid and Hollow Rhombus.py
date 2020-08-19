#Solid Rhombus
n=4
for i in range(n):
    print(' '*(n-1-i)+'*'*n+' '*i)

for i in range(n):
    print(' '*(n-1-i)+'*'*n+' '*i+' '*i+'*'*n)


#Hollow Rhombus

n=4

print(' '*(n-1)+'*'*n)
for i in range(n-2):
    print(' '*(n-2-i)+'*'+' '*(n-2)+'*')
print('*'*n)
