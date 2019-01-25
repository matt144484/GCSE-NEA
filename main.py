from subroutines import *

''' 
accounts;

username = Robin, password = techsavvy'
username = Hazz, password = 'SOTW69'

'''

progstart() #Does the user want to play the game?
userlogin() #User login system
diceroll() #Algorithm that performs the diceroll and outputs the score for each user each round
winner() #Determines the winner and congratulates them
savewinner() #Saves the winners name and score to an external.txt file
leaderboardchoice() #asks the user if they would like to see the top scorers leaderboard
leaderboard() #displays the top scorers leaderboard
