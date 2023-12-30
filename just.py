#print("please type \"exit\" to terminate the program")
import random

secret=random.randint(1,10)

taken=0
for taken in range(1,7):
   print("enter a number between 1 and 10")
   guess= int(input())
   if guess == secret:
      print("u guess is correct! u guessed in "+str(taken)+ " tries")
      break
   elif guess < secret:
      print("ur guess is too low")
   elif guess > secret:
       print("u guess is too high")

