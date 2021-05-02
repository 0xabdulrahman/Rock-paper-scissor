import random, os
from time import sleep
v = 'rock', 'paper', 'scissor'
print(v)
sleep(1)
thing = input('Enter your things : ')
sleep(1)
if thing == 'rock':
    z = random.choice(v)
    sleep(1)
    print(z)
    sleep(1)
    if z == 'paper':
        print('i won! ')
        input(' ')
        exit()
    if z == 'rock':
        print('Tie !')
        input(' ')
        exit()
    if z == 'scissor':
        print('You won ')
        input(' ')
        exit()
    else:
        print('Error')
        exit()
if thing == 'paper':
    z = random.choice(v)
    sleep(1)
    print(z)
    sleep(1)
    if z == 'scissor':
        print('i won! ')
        input(' ')
        exit()
    if z == 'paper':
        print('Tie !')
        input(' ')
        exit()
    if z == 'rock':
        print('You won ')
        input(' ')
        exit()
    else:
        print('Error')
        exit()
if thing == 'scissor':
    z = random.choice(v)
    sleep(1)
    print(z)
    sleep(1)
    if z == 'rock':
        print('i won! ')
        input(' ')
        exit()
    if z == 'scissor':
        print('Tie !')
        input(' ')
        exit()
    if z == 'paper':
        print('You won ')
        input(' ')
        exit()
    else:
        print('Error')
        exit()










        
