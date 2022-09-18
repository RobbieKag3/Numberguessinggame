
import random
number=random.randint(1,11)
chances=3
while chances>0:
    guess=int(input("Enter your guess : "))
    if (guess==number):
        print("YES YOUR GUESS IS CORRECT!")
        break
    else:
        print("TRY AGAIN!")
    chances=chances-1

if chances==0:
    print("ALL YOUR CHANCES ARE EXHAUSTED!.. THE CORRECT GUESS IS ", number)