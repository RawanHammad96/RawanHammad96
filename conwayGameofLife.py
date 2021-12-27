
import numpy
import math

def conway(s,p):
    '''
    conway(s,p) takes in the size of a matrix, s, and a probability, p, to randomly generate a board then reshape it as a square matrix
    '''
    #randomly generate a board using probability, p, or 1 (all cells are alive) or 0 (all cells are dead)
    board = numpy.random.choice([1,0], s*s, p)
    
    #reshape it into a matrix of size s (which is s by s or s*s)
    board = board.reshape(s,s)
    
    #return the randomly board generated
    return board

def advance(b,t):
    '''
    advance(b,t) accepts a Conway board, b, and advances it in timesteps, t, according to the following rules:
    
    1. Any live cell (marked as 1) with fewer than two live neighbors die, as if by underpopulation. 
    2. Any live cell (marked as 1) with two or three live neighbors lives on to the next generation. 
    3. Any live cell (marked as 1) with more than three live neighbors dies, as if by overpopulation. 
    4. Any dead cell (marked as 0) with exactly three live neighbors becomes a live cell, as if by reproduction.
    
    This function then prints a new board for each timestep. 
    '''
    #save the board as new board
    newBoard = b
    
    #we know the size is 10, but this function only takes b, the board, and does not take in the size. So we'll use the square root of the board's size to get the sides lengths
    sides = int(math.sqrt(newBoard.size))
    
    #now we'll run the simulaton for the timesteps, t
    for i in range(0, t):
        
        #now we'll run each side of the board, where x and y mark the positions in the matrix
        for x in range(sides):
            for y in range(sides):
                #sum of left and right
                left, right = max(0, x-1), min(sides+1, x+2)
                #sum of up and down
                up, down = max(0, y-1), min(sides+1, y+2)
                #combine and find the sum
                n = newBoard[left:right, up:down]
                if newBoard[x,y] == 1:
                    neighbors = numpy.sum(n) - 1
                else:
                    neighbors = numpy.sum(n)
                
                #CONDITIONS FOR LIVE CELLS
                #if a cell is marked as 1 and is alive
                if newBoard[x,y] == 1:
                    #Any live cell (marked as 1) with fewer than two live neighbors die, as if by underpopulation. 
                    if neighbors < 2:
                        newBoard[x,y] == 0
                        
                    #Any live cell (marked as 1) with two or three live neighbors lives on to the next generation. 
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[x,y] = 1
                     
                    #Any live cell (marked as 1) with more than three live neighbors dies, as if by overpopulation.    
                    elif neighbors > 3:
                        newBoard[x,y] = 0
                        
                #CONDITIONS FOR DEAD CELLS
                #if a cell is marked as 0 or is dead
                elif newBoard[x,y] == 0:
                    #Any dead cell (marked as 0) with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if neighbors == 3:
                        newBoard[x,y] = 1
                    else:
                        newBoard[x,y] =0
                        
        #set current board as the next board, b
        b = newBoard
        #returns the newBoard generated      
        return b


def main():
    '''
                    This program implements Conway's Game of Life simulation using two functions, conway(s,p) and
                    advance(b,t) where s is the size of the board, p is the probability between 10% and 90%, and
                    t is the number of timestamps or runs. This program will generate a board for each timestamp 
                            displaying all the dead and live cells based on their neighbors' mortality. 
    '''
    print("\n......................................................................................................................")
    print("........................................WELCOME TO THE GAME OF LIFE PROGRAM...........................................")
    print(main.__doc__)
    
    #set the matrix size to s
    s = 8
    
    #set a range of probabilities from 10% to 90%
    p = [0.1, 0.9]
    
    #set the timestamps/runs
    t = 10
    
    #call function conway(s,p) to generate a random board and assign it to b 
    b = conway(s,p)
    
    #print results for all timestamps; call advance(b,t) which generates new boards based on the initial randomly generated board to continue the game
    for i in range(0, t):
        print("Board number:", i+1)
        #call advance and print the array carrying the board
        print(advance(b,t))

main()