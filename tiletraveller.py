# In this assignment, you work in groups of 2-3 students each and apply pair programing. Moreover, you need to use git during the development of your solution.

# The assignment is to develop a computer game in which the player is located in a certain tile in a grid.  At each iteration, the program displays the directions for which there are adjacent tiles that the player can travel to.  

# The program only displays text, so you don’t actually draw the tile grid, but the program should behave as if the player is in a 3x3 grid with open and closed walls as seen in the following image:

# The player starts in tile (1,1). At the beginning, and after each move selected by the player, the program should print the player’s travel options. If there is an open wall in a direction, write that direction as a possible travel direction.

# At each iteration, the player enters the first letter of the direction he/she wishes to travel, after which the player should be located in another tile and the options for the new tile are then printed out.

# The player enters:

#     n/N for north (up)
#     e/E for east (right)
#     s/S for south (down)
#     w/W for west (left)

# If the player enters an invalid direction, the program prints “Not a valid direction!” and allows the player to enter the direction again.

# For example, in tile (1,1) it’s only possible to move north. In tile (1,2), the possible moves are north, east and south, and in tile (3,3) the valid moves are south and west.

# Tile (3,1) is the victory location.  When the player enters this tile, the program should notify him/her of their victory and quit running.

# Example run:

# You can travel: (N)orth.
# Direction: s
# Not a valid direction!
# You can travel: (N)orth.
# Direction: n
# You can travel: (N)orth or (E)ast or (S)outh.
# Direction: N
# You can travel: (E)ast or (S)outh.
# Direction: w
# Not a valid direction!
# You can travel: (E)ast or (S)outh.
# Direction: E
# You can travel: (E)ast or (W)est.
# Direction: e
# You can travel: (S)outh or (W)est.
# Direction: s
# You can travel: (N)orth or (S)outh.
# Direction: S
# Victory!

def move_north(x):
    (a, b) = x
    c = (a, b+1)
    return c

def move_south(x):
    (a, b) = x
    c = (a, b-1)
    return c

def move_west(x):
    (a, b) = x
    c = (a-1, b)
    return c

def move_east(x):
    (a, b) = x
    c = (a+1, b)
    return c

def is_not_wall(first, second):
    if ((first == (2, 3)) and (second == (2,2))) or ((first == (2, 2)) and (second == (2,3))):    
        return False
    elif ((first == (2, 2)) and (second == (3,2))) or ((first == (3, 2)) and (second == (2,2))):    
        return False
    elif ((first == (2, 1)) and (second == (3, 1))) or ((first == (3, 1)) and (second == (2, 1))):    
        return False
    elif ((first == (1, 1)) and (second == (2,1))) or ((first == (2, 1)) and (second == (1, 1))):    
        return False
    else:
        return True

def check_north(a):
    """Takes (x,y) axis, runs the direction funtion 
    and then is_not_wall to check if the direction is available """
    second = a
    first = move_north(a)
    wall_check = is_not_wall(first, second)
    return wall_check

def check_south(a):
    second = a
    first = move_south(a)
    wall_check = is_not_wall(first, second)
    return wall_check  
    
def check_west(a):
    second = a
    first = move_west(a)
    wall_check = is_not_wall(first, second)
    return wall_check

def check_east(a):
    second = a
    first = move_east(a)
    wall_check = is_not_wall(first, second)
    return wall_check


possible_tiles = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

possible_move = "" 


player_tile = (1, 1)

while player_tile in possible_tiles:
    possible_move = ""
    if player_tile == (3, 1):
        print("Victory!")
        break
            
    direction_check_north = player_tile
    north = check_north(direction_check_north)
    direction_check_north = move_north(direction_check_north)
    if (north == True) and (direction_check_north in possible_tiles):
        possible_move += "(N)orth "
            
    direction_check_east = player_tile
    east = check_east(direction_check_east)
    direction_check_east = move_east(direction_check_east)
    if (east == True) and (direction_check_east in possible_tiles):
        possible_move += "(E)ast "

    direction_check_south = player_tile
    south = check_south(direction_check_south)
    direction_check_south = move_south(direction_check_south)
    if (south == True) and (direction_check_south in possible_tiles):
        possible_move += "(S)outh "

    direction_check_west = player_tile
    west = check_west(direction_check_west)
    direction_check_west = move_west(direction_check_west)
    if (west == True) and (direction_check_west in possible_tiles):
        possible_move += "(W)est "
    
    #print available directions
    
    if len(possible_move) > 15:
        #splitta 2x
        possible_move = possible_move.split()
        string_print = " or ".join(possible_move)
        print("You can travel: {}.".format(string_print))

    elif 8 < len(possible_move) <= 15:
        #splitta 1x
        possible_move = possible_move.split()
        string_print = " or ".join(possible_move)
        print("You can travel: {}.".format(string_print))
    else:
        print("You can travel:", possible_move[:-1] + ".")

    player_input = input("Direction: ")
    player_input = player_input.lower()
    
    if (player_input == "n") and (north == True) and (direction_check_north in possible_tiles):
        player_tile = move_north(player_tile)

    elif (player_input == "s") and (south == True) and (direction_check_south in possible_tiles):
        player_tile = move_south(player_tile)

    elif (player_input == "w") and (west == True) and (direction_check_west in possible_tiles):
        player_tile = move_west(player_tile)

    elif (player_input == "e") and (east == True) and (direction_check_east in possible_tiles):
        player_tile = move_east(player_tile)
    else:
        print("Not a valid direction!")
        continue

     
