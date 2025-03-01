# Gavin Clifton
# Ben Funk
# MaryCatherine Shepherd
# Sam Jenson
# Thomas Apke

import random

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
    winCount = int(0)
    lossCount = int(0)
    # set up a loop to continue running until there are no more teams to select
    while lstNames.__len__() > 0:
        selectOpp = input("\nEnter which team you want to play: ")
        position = int(lstNames.index(selectOpp))
        # popping the opponent team from the list
        lstNames.pop(position)
        # games[selectOpp] = playTheGame(selectTeam,selectOpp)
        print()
        print(f"You chose to play {selectOpp}.\n")

        #simulate the game, add to Win/Loss record
        

        result = playTheGame(selectTeam, selectOpp)
        if result == 'W':
            winCount += 1
            pass
        elif result == 'L':
            lossCount += 1
            pass

        print(f"\nEnter the next team. \nTeams remaining: ")
        for team in lstNames:
            print(team)
    print("None, calculating results...\n")
    return selectTeam, winCount, lossCount

# take the two variables and simulate a game
def playTheGame(homeTeam, awayTeam):
    home_score = 0
    away_score = 0
    
    #prevent ties
    while home_score == away_score:
        home_score = random.randrange(0,11)
        away_score = random.randrange(0, 11)

    print(f'{homeTeam}: {home_score}, {awayTeam}: {away_score}')

    #solve for win/loss
    if home_score > away_score:
        gameResult = 'W'
    else:
        gameResult = 'L'

    
    return gameResult

# Function to print team results
def printResults(selectTeam, winCount, lossCount):
    print(f"Final season record: {lossCount}: {selectTeam} - {winCount}")

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
        selectTeam, winCount, lossCount = playTournament()
        printResults(selectTeam, winCount, lossCount)
    elif choice == "2":
        print("Hold")   # input custom function
    elif choice == "3":
        print(f"Goodbye, {player_name}! Thanks for playing.")
        break
    else: 
        print("Invalid choice. Please enter 1, 2, or 3")




"""#return number of games, scores, and overall record
print()
for item in games:
    opponent = games[item][0]
    home_score = games[item][1]
    opp_score = games[item][2]
    
    print(f"{home}'s score: {home_score}, {opponent}'s score: {opp_score}")

print(f"Final season record: {home} {winCount}-{lossCount}") """




