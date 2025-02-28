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


# setting up the custom function for the player to pick which team to play as
def playTournament():
    print("Choose your team:")
    lstNames=['BYU', 'UVU', 'USU', 'SDSU', 'OSU']
    for team in lstNames:
        print(team)
    # getting input for what team they're playing as
    selectTeam = input("\nEnter which team you want to play as: ")
    position = int(lstNames.index(selectTeam))
    # popping the home team from the list
    lstNames.pop(position)
    # display remaining teams that will be their opponents
    print("\nRemaining teams to play: ")
    for team in lstNames:
        print(team)
    # set up a loop to continue running until there are no more teams to select
    while lstNames.__len__() > 0:
        selectOpp = input("\nEnter which team you want to play: ")
        position = int(lstNames.index(selectOpp))
        # popping the opponent team from the list
        lstNames.pop(position)
        # games[selectOpp] = playTheGame(selectTeam,selectOpp)
        print(f"You chose to play {selectOpp}.\n")
        print(f"\nTeams remaining: ")
        for team in lstNames:
            print(team)
    print("None, calculating results...\n")

playTournament()