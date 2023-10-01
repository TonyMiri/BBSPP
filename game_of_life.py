import sys, time, os, random

def initialize(grid: str):
    '''
    Initialize the game board with seed values
    -------------------------------------------
    Inputs:
        -str grid: list of dicts of tuple: bool
    Returns:
        int rows: number of columns visible in the terminal
        int columns: number of columns visible in the terminal
    '''
    #Get visible size of terminal
    columns, rows = os.get_terminal_size() #54 x 191
    print(columns, ":", rows)

    #Create a dict for every row with an (x,y) tuple as keys (coordinates)
    #and a 1 or 0 state for alive and dead cells
    for x in range(rows):
        row_dict = {}
        for y in range(columns):
            row_dict[(x,y)] = random.randint(0,1)
        grid.append(row_dict)
    return rows, columns

def get_neighbors(rows: int, columns: int):
    '''
    Get all the valid potential neighbors for each cell
    ---------------------------------------------------
    Inputs:
        -int rows: number of rows visible in the terminal
        -int columns: number of columns visible in the terminal
    Returns:
        - list of lists of lists - valid_neighbors - All coordinates for valid neighbor cells for each cell
    '''

    valid_neighbors = []

    #Get all the neigboring coordinates for each cell
    for idx, row_dict in enumerate(grid):
        for k, v, in row_dict.items():

            #Find coordinates of all potential neigbor cells (row, column) - (k[0], k[1])
            #example:  xxx
            #          x0x
            #          xxx
            neighbors = [[(k[0] -1, k[1] - 1), (k[0] -1, k[1]), (k[0] - 1, k[1] + 1)],
                        [(k[0], k[1] - 1), (k[0], k[1] + 1)],
                        [(k[0] + 1, k[1] - 1), (k[0] + 1, k[1]), (k[0] + 1, k[1] + 1)]]
            
            #Filter the coordinates of potential neighbors for non-negative values only
            #example for cell (0,0):  0x
            #                         xx
            neighbor_master = []
            for x in neighbors: #For every row-list of neighbors for each cell
                temp = []
                for y in x: #For each neighbor in the list
                    if all(j >= 0 for j in y):
                        if y[0] != rows and y[1] != columns:                
                            temp.append(y)
                neighbor_master.append(temp)
            valid_neighbors.append(neighbor_master)
    return valid_neighbors

def calc_next_grid_state(grid, neighbors, rows, columns):
    '''
    Determine next state of each cell in the grid
    ----------------------------------------------
    Input:
        -list of dicts - current state of game grid
        -neighbors - list of lists - valid neighbors for each cell
    '''
    #Initialize our coordinates and new empty grid
    y_coord = 0 #columns
    x_coord = 0 #rows
    updated_grid = [{}]


#Need to loop over grid instead of neighbors


    for q in neighbors:
        living_neighbors = 0
        for x in q: #For every list of valid neighbors
            this_cell = (x_coord, y_coord)
            state = grid[x_coord][this_cell]

            #Count the living neighbors
            if len(x): #if it has valid neighbors in that row
                for y in x: #for every valid neighbor
                    if grid[y[0]][y] == 1: #if that neighbor is alive
                        living_neighbors += 1

            #If our cell is already alive
            if state == 1 and living_neighbors in [2,3]:
                updated_grid[x_coord][this_cell] = 1
            elif state == 0 and living_neighbors == 3:
                updated_grid[x_coord][this_cell] = 1
            else:
                updated_grid[x_coord][this_cell] = 0

            #Update the coordinates in order to loop to next row in grid
            y_coord +=1 
            if y_coord == columns:
                if x_coord != rows-1:
                    y_coord = 0
                    x_coord += 1
                    updated_grid.append({})
                    continue
                #print(len(updated_grid[0]))
                return updated_grid

def update_grid(current_grid, next_grid):
    for idx, val in enumerate(next_grid):#for each row dict in current grid
        for k, v in val.items(): #for each item in the row
            current_grid[idx][k] = v

def print_grid(grid):
    for x in grid:
        row_string = ""
        for y in x.values():
            if y == 1:                   
                row_string += str(y)
                continue
            row_string += " "
        print(row_string)
    

if __name__ == "__main__":
    grid = []
    rows, columns = initialize(grid)
    print_grid(grid)
    while True:
        neighbors = get_neighbors(rows, columns)
        next_round = calc_next_grid_state(grid, neighbors, rows, columns)
        if next_round == None:
            break
        update_grid(grid, next_round)
        print_grid(grid)
        #sys.stdout.write("\033[0;0H")
        time.sleep(1)



#NOTES

# Living cells with two or three neighbors stay alive in the next step of the simulation.
# Dead cells with exactly three neighbors become alive in the next step of the simulation.
# Any other cell dies or stays dead in the next step of the simulation.

#  Position the Cursor:
#   \033[<L>;<C>H
#      Or
#   \033[<L>;<C>f
#   puts the cursor at line L and column C.

# counter = 0
# for x in range(10):
#     for y in range(4):
#         print(f"This is test #{counter}")
#         counter+=1
#         time.sleep(.1)
#     sys.stdout.write("\033[4A")