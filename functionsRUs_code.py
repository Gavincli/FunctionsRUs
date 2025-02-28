#Gavin Clifton

import random

def playTheGame(homeTeam, awayTeam):
    home_score = 0
    away_score = 0
    
<<<<<<< Updated upstream
    #prevent ties
    while home_score == away_score:
        home_score = random.randrange(0,11)
        away_score = random.randrange(0, 11)
=======
    if choice == "1" :
        print("Lets go") # input custom function
    elif choice == "2":
        print("Hold")   # input custom function
    elif choice == "3":
        #print(f"Goodbye, {player_name}! Thanks for playing.")
        break
    else: 
        print("Invalid choice. Please enter 1, 2, or 3")



>>>>>>> Stashed changes

    print(f'{homeTeam}: {home_score}, {awayTeam}: {away_score}')

    #solve for win/loss
    if home_score > away_score:
        gameResult = 'W'
        #winCount += 1
    else:
        gameResult = 'L'
        #lossCount += 1

    
    return gameResult

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
    

#Play the game
result = playTheGame(home, away)


"""#return number of games, scores, and overall record
print()
for item in games:
    opponent = games[item][0]
    home_score = games[item][1]
    opp_score = games[item][2]
    
    print(f"{home}'s score: {home_score}, {opponent}'s score: {opp_score}")

print(f"Final season record: {home} {winCount}-{lossCount}")"""