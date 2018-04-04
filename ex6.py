# Type your code for binary search (Exercise 6) here
import random
number=random.randint(0,100)


guess=int(input("Guess an integer from 0 to 100 inclusive:"))


while True:
    if guess > 100:
        print('Hey! Between 0 and 100.')
        guess = int(input('Guess again'))
        continue
    if guess>number:
        print('Too high')
    elif guess<number:
        print('Too low')
    else:
        print('You got it!')
        break
    guess = int(input('Guess again'))
