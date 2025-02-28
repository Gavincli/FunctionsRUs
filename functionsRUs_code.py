#Gavin Clifton

import random

#Get inputs
home = input('Enter the name of the home team: ')

numGames = int(input('Enter the number of games the team will play: '))

#key - away team, value: list of score and W/L
games = {}
winCount = 0
lossCount = 0


gameCount = 0
#repeat for game count
while gameCount < numGames:
    gameCount += 1
    away = input(f'Enter the name for the away team for game {gameCount}: ')
    games[away] = []
    
#generate scores
for key in games:
    home_score = 0
    away_score = 0
    
    #prevent ties
    while home_score == away_score:
        home_score = random.randrange(0,11)
        away_score = random.randrange(0, 11)

    #solve for win/loss
    if home_score > away_score:
        winner = 'Win'
        winCount += 1
    else:
        winner = 'Loss'
        lossCount += 1
    
    #assign values to dictionary
    for items in games.keys():
        games[key] = [key, home_score, away_score]


    


#return number of games, scores, and overall record
print()
for item in games:
    opponent = games[item][0]
    home_score = games[item][1]
    opp_score = games[item][2]
    
    print(f"{home}'s score: {home_score}, {opponent}'s score: {opp_score}")

print(f"Final season record: {home} {winCount}-{lossCount}")