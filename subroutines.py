import sys
import random
import time
users = 0 
RobinTotal = 0
HazzTotal = 0

def progstart():
  while True:
    userbegin = input('Welcome to DiGame (ver 1.0). Would you like to play? [Y/N]') #asks the user whether they would like to start the game or not
    if userbegin == 'Y':
      break
    elif userbegin == 'N':
      print('Goodbye!')
      sys.exit()
    else:
      print('Please try again. That does not appear to be a correct input!') #gives the user another chance if their input was an invalid option
      
def userlogin():
  global users
  while users < 2:
    username = input('Please enter your username: ') #gets the user to enter a username       
    password = input('Please enter your password: ') #gets the user to enter a password
    
    if username == 'Robin' and password == 'techsavvy':
      print('This player is now logged in!')
      users = users + 1 #updates the number of users logged in
      if users == 1:
        print('Next player please login!')
      elif users == 2:
        print('Okay, we can now begin!')
        
    elif username == 'Hazz' and password == 'SOTW69':
      print('This player is now logged in!')
      users = users + 1 #updates the number of users logged in
      if users == 1:
        print('Next player please login!')
      elif users == 2:
        print('Okay, we can now begin!')
      else:
        pass
      
    else:
      print('That doesn\'t seem to be correct. Please try again!') 

def diceroll():
  i = 0
  global RobinTotal
  global HazzTotal

  while i < 5:
    diceroll_p1_1 = random.randint(1,6)
    diceroll_p1_2 = random.randint(1,6)
    diceroll_p2_1 = random.randint(1,6)
    diceroll_p2_2 = random.randint(1,6)
    extradicerollp1 = random.randint(1,6)
    extradicerollp2 = random.randint(1,6)
    i = i+1
      
    if diceroll_p1_1 % 2 == 0 and diceroll_p1_1 != 0:
      diceroll_p1_1 = diceroll_p1_1 + 10
      
    else:
      diceroll_p1_1 = diceroll_p1_1 - 5
    
    if diceroll_p1_2 % 2 == 0 and diceroll_p1_2 != 0:
      diceroll_p1_2 = diceroll_p1_2 + 10
      
    else:
      diceroll_p1_2 = diceroll_p1_2 - 5
      
    if diceroll_p2_1 % 2 == 0 and diceroll_p2_1 != 0:
      diceroll_p2_1 = diceroll_p2_1 + 10
      
    else:
      diceroll_p2_1 = diceroll_p2_1 - 5
    
    if diceroll_p2_2 % 2 == 0 and diceroll_p2_2 != 0:
      diceroll_p2_2 = diceroll_p2_2 + 10
      
    else:
      diceroll_p2_2 = diceroll_p2_2 - 5
    
    if extradicerollp1 % 2 == 0 and extradicerollp1 != 0:
      extradicerollp1 = extradicerollp1 + 10
      
    else:
      extradicerollp1 = extradicerollp1 - 5
    
    if extradicerollp2 % 2 == 0 and extradicerollp2 != 0:
      extradicerollp2 = extradicerollp2 + 10
      
    else:
      extradicerollp2 = extradicerollp2 - 5
    
    RobinTotal = RobinTotal + diceroll_p1_1+diceroll_p1_2
    if RobinTotal < 0:
      RobinTotal == 0
    HazzTotal = HazzTotal + diceroll_p2_1+diceroll_p2_2
    if HazzTotal < 0:
      HazzTotal == 0
      
    if diceroll_p1_1 != diceroll_p1_1 and diceroll_p2_1 != diceroll_p2_2:
    
      print('Round number', i)
      print()
      print('Robin scored', diceroll_p1_1+diceroll_p1_2, 'after applying the modifiers!')
      print('Hazz scored', diceroll_p2_1+diceroll_p2_2, 'after applying the modifiers!')
      print()
      
      time.sleep(1)
    
    elif diceroll_p1_1 == diceroll_p1_2 and diceroll_p2_1 != diceroll_p2_2:
      
      print('Round number', i)
      print()
      print('Robin scored', diceroll_p1_1+diceroll_p1_2+extradicerollp1, 'after applying the modifiers!')
      print('Hazz scored', diceroll_p2_1+diceroll_p2_2, 'after applying the modifiers!')
      print()
      
      time.sleep(1)
      
    elif diceroll_p1_1 != diceroll_p1_2 and diceroll_p2_1 == diceroll_p2_2:
      
      print('Round number', i)
      print()
      print('Robin scored', diceroll_p1_1+diceroll_p1_2, 'after applying the modifiers!')
      print('Hazz scored', diceroll_p2_1+diceroll_p2_2+extradicerollp2, 'after applying the modifiers!')
      print()
      
      time.sleep(1)
    
    else:
      
      print('Round number', i)
      print()
      print('Robin scored', diceroll_p1_1+diceroll_p1_2+extradicerollp1, 'after applying the modifiers!')
      print('Hazz scored', diceroll_p2_1+diceroll_p2_2+extradicerollp2, 'after applying the modifiers!')
      print()
      
      time.sleep(1)      

def winner():
  
  if RobinTotal < HazzTotal:
    print('Well done Hazz, you won! You scored', HazzTotal, 'whilst Robin scored', RobinTotal, '.')
  elif HazzTotal < RobinTotal:
    print('Well done Robin, you won! You scored', RobinTotal, 'whilst Hazz scored', HazzTotal, '.')
  elif HazzTotal == RobinTotal: 
    print('Tiebreaker!')
    print('Each player will now roll 1 di. Whoever scores the highest wins! If they are the same, you will continue to the roll one di until someone scores higher than the other and hence wins the game!')
    
    while True:
      
      tiebreakerrollp1 = random.randint(1,6)
      tiebreakerrollp2 = random.randint(1,6)
    
      if tiebreakerrollp1 % 2 == 0 and tiebreakerrollp1 != 0:
        tiebreakerrollp1 = tiebreakerrollp1 + 10
      
      else:
        tiebreakerrollp1 = tiebreakerrollp1 - 5
        
      if tiebreakerrollp2 % 2 == 0 and tiebreakerrollp2 != 0:
        tiebreakerrollp2 = tiebreakerrollp2 + 10
        
      else:
        tiebreakerrollp2 = tiebreakerrollp2 - 5
        
      if tiebreakerrollp1 > tiebreakerrollp2:
        print('Robin scored', tiebreakerrollp1, 'compared to Hazz who scored', tiebreakerrollp2, ', so Robin won!')
        break
      
      else:
        print('Hazz scored', tiebreakerrollp2, 'compared to Robin who scored', tiebreakerrollp1, ', so Hazz won!')
        break

def savewinner(filename = 'winners.txt'):
  
  if RobinTotal > HazzTotal:
    winningusernamerobin = input('So Robin, under what name would you like to save your win?')
    robinwinnerinfo = (winningusernamerobin + ' / ' + str(RobinTotal))
    with open(filename,'a') as file:
        file.write(robinwinnerinfo + '\n')
  
  elif RobinTotal == HazzTotal and tiebreakerrollp1 > tiebreakerrollp2:
    winningusernamerobin = input('So Robin, under what name would you like to save your win?')
    robinwinnerinfo = (winningusernamerobin + ' / ' + str(RobinTotal))
    with open(filename,'a') as file:
        file.write(robinwinnerinfo + '\n')
  
  elif HazzTotal > RobinTotal: 
    winningusernamehazz = input('So Hazz, under what name would you like to save your win?')
    hazzwinnerinfo = (winningusernamehazz + ' / ' + str(HazzTotal))
    with open(filename,'a') as file:
        file.write(hazzwinnerinfo + '\n')
        
  elif RobinTotal == HazzTotal and tiebreakerrollp2 > tiebreakerrollp1:
    winningusernamerobin = input('So Haz`z, under what name would you like to save your win?')
    robinwinnerinfo = (winningusernamehazz + ' / ' + str(HazzTotal))
    with open(filename,'a') as file:
        file.write(hazzwinnerinfo + '\n')
  
        
def leaderboardchoice():
  while True:
    userlbchoice = input('Would you like to see the top 5 all time scorers and there scores? [Y/N]')
    if userlbchoice == 'Y':
      break
  
    elif userlbchoice == 'N':
      sys.exit('Okay. See you again soon!')
    
    else:
      print('Please use a correct input.')
      continue

def leaderboard(filename = 'winners.txt'):
  with open(filename, "r") as f:
    counter = 0
    for line in f:
        print(line)
        counter += 1
        if counter == 5:
          break
