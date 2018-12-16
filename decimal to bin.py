print('python program for converting decimal to binary')

num = int(input('Enter a decimal num : '))
power=0
binary = 0
while num>0:
    binary += 10**power * (num % 2)
    num//=2
    power+=1
print(binary)
