#Please dont type letters
import random


tries = 0

num = input('\nPlease enter which range you want to guess the number from, for example enter 10 to get to guess from 1,10: ')
tries_num = int(input('\nPlease enter how many tries you want. from 1 - 100: '))
tries = tries_num
core_num = random.randint(1, int(num))
print(f'Hello Welcome to the Guessing game.\nYou have {tries} tries to guess the number!\nGoodLuck')

while tries:
    tries -= 1
    Guess = input('Guess a Number from 1 to '+num+': ')
    if int(Guess) < core_num:
        tries - 1
        print('Sorry this number is too low.\nYou have... ' + str(tries) + ' tries')
    elif int(Guess) > core_num:
        tries - 1
        print('Sorry this number is too high.\nYou have... ' + str(tries) + ' tries')
    elif int(Guess) == core_num:
        print('Good job you won!on your... ' + str(tries) + ' Try left!')
        break
    
    if not tries:
        print('oof you lose the game.The number was ' + str(core_num) + '.')