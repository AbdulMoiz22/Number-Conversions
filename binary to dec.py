print('python program for converting binary to decimal')

num = int(input('Enter a binary num: '))
dec = 0
power = 0
while num>0:
    dec += 2**power* ( num % 10)
    num//=10
    power+=1
print(dec)
    
