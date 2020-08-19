number=10101001
copy=number
decimal=0
power=0
while number>0:
    t=number%10
    number=number//10
    decimal=decimal+t*2**power
    power=power+1
print('Decimal Number of ',copy,' is ',decimal)

copy=decimal

print('Again Decimal Number ',copy,' to Binary ')
    
def binary(decimal):
    
    if decimal>1:
        binary(decimal//2)
    print(decimal%2,end='')

binary(decimal)
    
