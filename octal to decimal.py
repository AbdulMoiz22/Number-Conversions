print('python program for converting octal to decimal')

num = int(input('Enter number in octal : '))
power = 0
decimal = 0
while num>0:
    decimal= 8**power*(num%10)
    num//=10
    power+=1
print(decimal)
