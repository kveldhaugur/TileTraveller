# búa til breytur fyrir tile_1_1...

# búa til function sem fara north, south, east, west

#veggir 
# tile_1_1 = 1.1
# tile_1_2 = 1.2
# tile_1_3 = 1.3

# tile_2_1 = 2.1
# tile_2_2 = 2.2
# tile_2_3 = 2.3

# tile_3_1 = 3.1
# tile_3_2 = 3.2
# tile_3_3 = 3.3

# wall_1 = [2.3, 2.2] 
# wall_2 = [2.2, 3.2]
# wall_3 = [2.1, 3.1]
# wall_4 = [1.1, 2.1]

def move_north(x, y):
    y += 1
    return (x, y)

def move_south(x, y):
    y -= 1
    return (x, y)

def move_west(x, y):
    x -= 1
    return (x, y)

def move_east(x, y):
    x += 1
    return (x, y)

def is_wall((a,b), (c,d)):
    if ((a,b), (c,d)) or ((c,d), (a,b)) == ((2,3), (2,2)):
        return True
    if ((a,b), (c,d)) or ((c,d), (a,b)) == ((2,2), (3,2)):
        return True
    if ((a,b), (c,d)) or ((c,d), (a,b)) == ((2,1), (3,1)):
        return True
    if ((a,b), (c,d)) or ((c,d), (a,b)) == ((1,1), (2,1)):
        return True
    else:
        return False


def check_north((a,b):
    """Takes (x,y) axis, runs the direction funtion 
    and then is_wall to check if the direction is available """
    (c,d) = (a,b)
    move_north(c,d)
    return is_wall((a,b), (c,d))

def check_south((a,b):
    (c,d) = (a,b)
    move_south(c,d)
    return is_wall((a,b), (c,d))    
    
def check_west((a,b):
    (c,d) = (a,b)
    move_west(c,d)
    return is_wall((a,b), (c,d))

def check_east((a,b):
    (c,d) = (a,b)
    move_east(c,d)
    return is_wall((a,b), (c,d))

possible_x = [1, 2, 3]
possible_y = [1, 2, 3]

possible_move = "(N)orth (S)outh (W)est (E)ast" 

possible_north = True
possible_south = False
possible_west = False
possible_east = False

x_as = 1
y_as = 1
player_tile = (x_as, y_as)

#while player_tile != (3, 3):
    #if 4 <= player_tile <= 0:
        #print error
        #continue

    #while player_tile in (possible_x, possible_y):
        #possible_move = possible_move.split(" ")
        
        #possible_move = " or ".join(possible_move)
        #print("You can travel {}.".format(possible_move.split(" ")))
        #player_input = input("Direction: ")
        
        #for player_tile is_wall

        #if player_input == "n" and player_tile != (wall_1 or wall_2 or wall_3 or wall_4):
            #player_tile = move_north(player_tile)
            #possible_south = True
            #possible_east = True
            
#print(player_tile)

direction_check_north = player_tile
check_north = check_north(direction_check_north)
if direction_check_north == True:
    possible_move += "(N)orth"
           
direction_check_east = player_tile
check_east = check_east(direction_check_east)
if direction_check_east == True:
    possible_move += "(E)east"

direction_check_south = player_tile
check_south = check_south(direction_check_south)
if direction_check_south == True:
    possible_move += "(S)outh"

direction_check_west = player_tile
check_west = check_west(direction_check_west)
if direction_check_west == True:
    possible_move += "(W)est"
    

#print available directions

if (player_input == "n") and (direction_check_north == True):
    move_north(player_tile)
else:
    print("Not a valid direction!")

if (player_input == "s") and (direction_check_south == True):
    move_south(player_tile)
else:
    print("Not a valid direction!")  

if (player_input == "w") and (direction_check_west == True):
    move_west(player_tile)
else:
    print("Not a valid direction!")  

if (player_input == "e") and (direction_check_east == True):
    move_east(player_tile)
else:
    print("Not a valid direction!")    

