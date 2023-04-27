import os
'''
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
'''

# Rules of the game
# 2 players, one plays with 'X', one plays with 'O'.
# The players play one turn at a time, alternating 
# each turn.
# A win is defined by 3 'X' or 'O' in a row
# The row can be horizontal, vertical, diagonal
# If all the boxes are filled, and there is no win, 
# it's a tie

def display_grid(grid_info):
    grid = "\n-------------\n\
| "+grid_info[0][0]+" | "+grid_info[0][1]+" | "+grid_info[0][2]+" |\n\
-------------\n\
| "+grid_info[1][0]+" | "+grid_info[1][1]+" | "+grid_info[1][2]+" |\n\
-------------\n\
| "+grid_info[2][0]+" | "+grid_info[2][1]+" | "+grid_info[2][2]+" |\n\
-------------\n"
    print(grid)
    
def clear_grid(grid_info):
        for row in grid_info:
            for i in range(3):
                row[i] = " "
                
def find_index(grid, value):
    for r in range(3):
        for c in range (3):
            if value == grid[r][c]:
                return [r,c]
    return None       

def print_winner(turn, player1, player2):
    if turn == 1:
        print(f"{player1} won!")
    else:
        print(f"{player2} won!")
    
# Setup the game
## Ask player's names
## Set the 'X' and 'O'
player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")
print(f"{player1} is 'X' and {player2} is 'O'")
## Set the grid
grid = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
grid = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
valid_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Play until win or tie
turn = 1
end = False
counter_turns = 0

while not end:
    os.system('cls')
    
    if turn == 1:
        print(f"{player1} (X), it's your turn!")
    else:
        print(f"{player2} (O), it's your turn!")
        
    #ask player to play
    display_grid(grid)
        
    # retry if couldn't find this value
    move = input ("Where do you want to play? ")
    index = find_index(grid, move)
    while index is None:
        print("This is not a valid position, can you retry?")
        move = input ("Where do you want to play? ")
        if move not in valid_positions:
            index = None
        else:
            index = find_index(grid, move)
    
    grid[index[0]][index[1]] = 'X' if turn == 1 else 'O'
    
    
    #check if win or tie
    #a row is filled with same values
    for r in range (3):
        if grid[r][0] == grid[r][1] and grid[r][1] == grid[r][2]:
            print_winner(turn, player1, player2)
            end = True
    #a column is filled with same values
    for c in range (3):
        if grid[0][c] == grid[1][c] and grid[1][c] == grid[2][c]:
            print_winner(turn, player1, player2)
            end = True
    #a diagonal is filled with same values
    if grid [0][0] == grid [1][1] and grid[1][1] == grid[2][2]:
        print_winner(turn, player1, player2)
        end = True
    if grid [0][2] == grid [1][1] and grid[1][1] == grid[2][0]:
        print_winner(turn, player1, player2)
        end = True
        
    counter_turns += 1

    if counter_turns == 9 and not end:
        #there is a tie
        print("That's a tie")
        end = True
    
    #change turn
    turn = 2 if turn == 1 else 1
## Show the grid and tell who's turn it is
## Ask where to place a mark
## Check for end scenarios
## repeat

# Display the result
## Say who end, or if there is a tie


