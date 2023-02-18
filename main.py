print ('Dice Roll Game')

from random import randint
import time 

def drg():
  
 chosen = randint(1,6)

 if chosen == 1:
  dice = 1
  if dice == 1:
   print ('Dice = 1')
   
 if chosen == 2:
  dice = 2
  if dice == 2:
   print ('Dice = 2')
   
 if chosen == 3:
  dice = 3
  if dice == 3:
   print ('Dice = 3')
   
 if chosen == 4:
  dice = 4
  if dice == 4:
   print ('Dice = 4')
   
 if chosen == 5:
  dice = 5
  if dice == 5:
   print ('Dice = 5')
   
 if chosen == 6:
  dice = 6
  if dice == 6:
   print ('Dice = 6')

drg ()