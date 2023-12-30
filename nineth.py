
import random,sys
print("rock,paper ,scissors")
wins=0
loss=0
ties=0
while True:
 print("%s wins,%s loss,%s ties" %(wins,loss,ties))
  while True:
   print("enter your move rock ,paper or scissors")
   playermove = input()
   if playermove == "rock" or playermove == "paper" or playermove =="scissor"
       break
    
  if playermove == "rock":
      print("rock vs ....",end=' ')
  elif playermove == "paper":
       print("paper vs ....",end=' ')
  elif playermove == "scissors":
     print("scissors vs....",end=' ')
  comp = random.randint(1,3)
  if comp == 1:
     computermove="rock"
     print("rock")
  elif comp == 2:
      computermove = "paper"
      print("paper")
  elif comp = 3:
       computermove = "scissors"
       print("scissors")
  print()
  if playermove == computermove:
      print("its a tie!")
      tie = ties+1
  elif playermove 



