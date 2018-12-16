print('python program for converting decimal to octal')

octal =0
power =0

num= int(input('Enter a number in decimal: '))
while num>0:
    octal+= 10**power*(num%8)
    num//= 8
    power+=1
print(octal)

         
