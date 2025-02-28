# Gavin Clifton
# Ben Funk
# MaryCatherine Shepherd
# Sam Jenson
# Thomas Apke

import random

# custom function that displays the menu
def menu(): 
    print("\nMenu: ")
    print("1. Start a new season: ")
    print("2. View season results: ")
    print("3. Quit")
    choice = input("Enter your choice here: ")
    return choice

# main line of code
while True:
    choice = menu()
    
    if choice == "1" :
        print("Lets go") # input custom function
    elif choice == "2":
        print("Hold")   # input custom function
    elif choice == "3":
        print(f"Goodbye, {player_name}! Thanks for playing.")
        break
    else: 
        print("Invalid choice. Please enter 1, 2, or 3")







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

def playTournament():
    print("Choose your team:")
    lstNames=['BYU', 'UVU', 'USU', 'SDSU', 'OSU']
    for team in lstNames:
        print(team)
    selectTeam = input("\nEnter which team you want to play as: ")
    position = int(lstNames.index(selectTeam))
    lstNames.pop(position)
    print("\nRemaining teams to play: ")
    for team in lstNames:
        print(team)
    while lstNames.__len__() > 0:
        selectOpp = input("\nEnter which team you want to play: ")
        position = int(lstNames.index(selectOpp))
        lstNames.pop(position)
        # games[selectOpp] = playTheGame(selectTeam,selectOpp)
        print(f"You chose to play {selectOpp}.\n")
        print(f"\nTeams remaining: ")
        for team in lstNames:
            print(team)
    print("None, calculating results...\n")

playTournament()