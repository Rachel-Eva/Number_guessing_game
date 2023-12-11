import math
import random
lower_bound=int(input("Enter the lower bound for the guess:"))
upper_bound=int(input("Enter the upper bound for the guess:"))
turns=round(math.log(upper_bound-lower_bound+1,2))
print("You've got ",turns,"number of guesses!")
count=0
num=random.randint(lower_bound,upper_bound)
while(count<turns):
    count+=1
    n=int(input("Enter your guess:"))
    if(n>num):
        print("Wrong! You guessed too high!")
    elif(n<num):
        print("Wrong! You guessed too low!")
    elif(n==num):
        print("BINGO! You guessed the number right!")
        break
    else:
        continue
if(n>num or n<num):
    print("You couldn't guess the number :( \nThe number was",num)
