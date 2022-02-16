import time

startState = [
    (0,2), # Tile 0 (empty tile)
    (2,0), # Tile 1 
    (1,1), # Tile 2
    (2,1), # Tile 3
    (0,1), # Tile 4
    (0,0), # Tile 5
    (1,0), # Tile 6
    (2,2), # Tile 7
    (1,2)  # Tile 8
    ]

# Heuristic. Returns minimum amount of movableTileCoords required if tiles could moveableTileCoord over each other.
def calculate_h(state):
    # solution stores the coordinates for the correct tile
    solution = [
        (2,2),
        (0,0), 
        (0,1), 
        (0,2), 
        (1,0), 
        (1,1), 
        (1,2), 
        (2,0), 
        (2,1) 
    ]
    
    amountOfMoves = 0

    # Calculate the amount of moves by getting the absolute difference between current position and solution position for x and y seperately and add them together
    for i in range(8):
        amountOfMoves += abs(state[i][0] - solution[i][0]) + abs(state[i][1] - solution[i][1])

    # Return the amount of moves
    return amountOfMoves

# Returns a list with the tile numbers of the tiles which can be moved
def possible_moves(state):

    # Get tiles adjacent to the empty tile (which is state[0])
    movableTileCoords = []

    movableTileCoords.append(((state[0][0] - 1), state[0][1]))
    movableTileCoords.append(((state[0][0] + 1), state[0][1]))
    movableTileCoords.append(((state[0][0]), state[0][1] - 1))
    movableTileCoords.append(((state[0][0]), state[0][1] + 1))

    # Check for tiles outside of the board
    for moveableTileCoord in movableTileCoords:
        if moveableTileCoord[0] > 2 or moveableTileCoord[0] < 0 or moveableTileCoord[1] > 2 or moveableTileCoord[1] < 0:
            movableTileCoords.remove(moveableTileCoord)
    
    # Get the tile numbers
    moves = []
    for i in range(len(state)):
        for movableTileCoord in movableTileCoords:
            if movableTileCoord == state[i]:
                moves.append(i)

    # Return the tile numbers of the tiles which can be moved
    return moves

# Returns the state after move a tile
def move_tile(state, tileNumber):
    newState = state.copy()
    newState[0], newState[tileNumber] = newState[tileNumber], newState[0]
    return newState

def print_state(state):
    print(state.index((0,0)), state.index((0,1)), state.index((0,2)))
    print(state.index((1,0)), state.index((1,1)), state.index((1,2)))
    print(state.index((2,0)), state.index((2,1)), state.index((2,2)))

def FindLowestF(input):
    f = 9999999
    for item in input:
        if item['f'] < f:
            bestItem = item
            f = item['f']
    
    return bestItem

def solveUsingAStar(startState):
    open = []
    closed = []
    open.append(
        {
            'f': calculate_h(startState),
            'g': 0,
            'h': calculate_h(startState), 
            'state': startState,
            'parent': None
        }
    )

    while len(open) != 0:
        print("RUN")
        q = FindLowestF(open)
        open.remove(q)

        possibleMoves = possible_moves(q['state'])
        childeren = []
        for move in possibleMoves:
            childeren.append(move_tile(q['state'], move))
        
        
        for child in childeren:
            if calculate_h(child) == 0:
                parent = q
                while parent != None:
                    print('-----')
                    print_state(parent['state'])
                    parent = parent['parent'] 

                return
            else:
                parent = q
                g = 0
                while parent != None:
                    g += 1
                    parent = parent['parent']
                h = calculate_h(child)
                f = g + h
            
                skip = False
                for item in open:
                    if item['state'] == child and item['f'] < f:
                        skip = True
                
                for item in closed:
                    if item['state'] == child and item['f'] < f:
                        skip = True

                if skip == False:
                    open.append(
                        {
                            'f': f,
                            'g': g,
                            'h': h, 
                            'state': child,
                            'parent': q
                        }
                    )
        
        closed.append(q)



print(solveUsingAStar(startState))

