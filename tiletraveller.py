# búa til breytur fyrir tile_1_1...

# búa til function sem fara north, south, east, west

#veggir 

def move_north():
    player += 0.1
    return player

def move_south():
    player -= 0.1
    return player

def move_west():
    player -= 1
    return player

def move_east():
    player += 1
    return player

tile_1_1 = 1.1
tile_1_2 = 1.2
tile_1_3 = 1.3

tile_2_1 = 2.1
tile_2_2 = 2.2
tile_2_3 = 2.3

tile_3_1 = 3.1
tile_3_2 = 3.2
tile_3_3 = 3.3

player = tile_1_1

wall_1 = [tile_2_3, tile_2_2] 
wall_2 = [tile_2_2, tile_3_2]
wall_3 = [tile_2_1, tile_3_1]
wall_4 = [tile_1_1, tile_2_1]

possible_move = "(N)orth (S)outh (W)est (E)ast" 

possible_north = True
possible_south = False
possible_west = False
possible_east = False

while player != tile_3_3:
    print("You can travel {}.".format(possible_move.split[0:6])
    player_input = input("Direction: ")
    if player == tile_1_1:
        player_input == "n"