# Number_guessing_game
## Overview:
This python code uses the 'random' method to arbitrarily pick a number within the range given by the user. The user then gets a specific amount of tries to guess the randomly genenrated number.
## Requirements:
* Python 2.1
## Explanation:
* We first import both the random function and the math function.
* The program asks the user to input the lower and upper range inside which the random number is generated.
* We then decide the number of terms using the logarithmic function.
* This is then displayed to the user so they are aware of the number of tries they have.
* We set a variable to count the number of tries as the user enters guesses.
* We then use a while loop for the number of tries.
* The variable set for counting is incremented each time the while loop is entered.
* The user then enters their guess.
* If the guess is higher than the random number, then it will display a message saying the inputted number
is too high.
* If the guess is lower than the random number, then it will display a message saying the inputted number
is too low
* If the user guesses it right, then the congratulatory message is displayed.
* If all the turns are over and the user hasn't guessed the number yet, then the control flows into the 'if'
statement stating the actual number.
## Code:
```
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
```
## Output:
![output](https://github.com/Rachel-Eva/Number_guessing_game/assets/145921131/8fd75122-2108-4d1c-ae3c-43720dce644a)

