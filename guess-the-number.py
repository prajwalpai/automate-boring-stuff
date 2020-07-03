from random import randint

print("I am thinking of a number between 1 and 20.")
actualnum = randint(0, 20)

for attempt in range(1, 7):
    num = int(input ("Guess the  number :"))
    if num > 20:
        print ('Bro! That is not within 1-20')
    elif num > actualnum:
        print ("The number is smaller than your guess")
    elif num < actualnum:
        print("The number is Greater than your guess")
    else:
        break

if (num == actualnum):
    print ("Thats Impressive! Indeed the number I was thking is {}".format(num))
else:
    print("You exhausted your guesses! The number I was thinking was {}".format(actualnum))
