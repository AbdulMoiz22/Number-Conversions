num = int(input('Enter a decimal num to be converted in binary : '))
power=0
binary = 0
while num>0:
    binary += 10**power * (num % 2)
    num//=2
    power+=1
print('In binary = ',binary)

octal =0
power =0
num = int(input('Now enter the number to be converted in octal from decimal: '))
while num>0:
    octal+= 10**power*(num%8)
    num//= 8
    power+=1
print('In Octal = ',octal)



