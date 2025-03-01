# Gavin Clifton
# Ben Funk
# MaryCatherine Shepherd
# Sam Jenson
# Thomas Apke

import random
games = {}
#Introduction to game, explains rules and prompts for a name
def intro():
    print("Welcome to the Women's Soccer Season Generator Game!")
    name = input('Enter your name: ').title()
    print(f"Hi {name}! Here are the rules of the game:\n"
        "1. Select an option from the menu.\n"
        "2. If option one, choose your team from the list of all teams.\n"
        "3. Select an opposing team.\n")
    return name

player_name = intro()

#Get inputs
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
    gameCount = 1
    while lstNames.__len__() > 0:
        selectOpp = input("\nEnter which team you want to play: ")
        position = int(lstNames.index(selectOpp))
        # popping the opponent team from the list
        lstNames.pop(position)
        # games[selectOpp] = playTheGame(selectTeam,selectOpp)
        print()
        print(f"You chose to play {selectOpp}.\n")

        #simulate the game, add to Win/Loss record
        

        result, home_score, away_score = playTheGame(selectTeam, selectOpp)
        games[f'Game {gameCount}'] = [selectOpp, home_score, away_score] 
        gameCount += 1
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
    
    return gameResult, home_score, away_score

# Function to print team results
def printResults(selectTeam, winCount, lossCount):
    print(f"Final season record: {selectTeam} : {winCount} - {lossCount}")

# custom function that displays the menu
def menu(): 
    print("\nMenu: ")
    print("1. Start a new season: ")
    print("2. View season results: ")
    print("3. Quit")
    choice = input("Enter your choice here: ")
    return choice

#return number of games, scores, and overall record
def displayGameResults(selectTeam):
    print("\nGame Results:")
    for game, result in games.items():
        opponent, home_score, opp_score = result
        print(f"{game}: {selectTeam} {home_score} - {opponent} {opp_score}")

# main line of code
while True:
    choice = menu()
    
    if choice == "1" :
        print("Let's go\n") # input custom function
        selectTeam, winCount, lossCount = playTournament()
        printResults(selectTeam, winCount, lossCount)
    elif choice == "2":
        if games:
            displayGameResults(selectTeam)
        else:
            print("\nNo games played yet, try simulating a season.")
    elif choice == "3":
        print(f"Goodbye, {player_name}! Thanks for playing.")
        break
    else: 
        print("Invalid choice. Please enter 1, 2, or 3")










