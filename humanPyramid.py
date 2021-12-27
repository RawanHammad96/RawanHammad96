'''
Author: Rawan Hammad
Date: 10/11/2021
3-Minute YouTube Video: https://youtu.be/G39ev0PbifA 
"I have not given or received any unauthorized assistance on this assignment"
Homework #4
'''


def humanPyramid(rowPosition, columnPosition):
    '''
    humanPyramid takes in the row position and column position from the user then uses a recursive function to return the weight on the person at the specified position. 
    '''

    #first row has no weight on them so it always returns 0
    if rowPosition == 0 and columnPosition == 0:
        return 0

    #the column position can never be greater than the row position; for example, (2,3) does not exist and returns 0
    #rows greater than 4 do not exist
    if (columnPosition > rowPosition) or  rowPosition > 4:
        print("This person does not exist. ")
        return 0

    #person is on the left side (positions B, D, G, and K) and has no weight from the left on them
    elif columnPosition == 0:
        #return 1/2 of the sum of his right person's weight and the total weight on his right person
        return (128 + humanPyramid(rowPosition - 1, columnPosition)) // 2

    #person is on the right side (positions C, F, J, and O) and has no weight from the right on them
    elif columnPosition == rowPosition:
        #return 1/2 of the sum of his left person's weight and the total weight on his left person
        return (128 + humanPyramid(rowPosition - 1, columnPosition - 1)) // 2

    #person is not on the left or right side; other positions (positions E, H, I, L, M, and N)
    else:
        #return 1/2 of the sum of his left person's weight, the total weight on his left person, 1/2 of the sum of his right person's weight,
        #and the total weight on his left person
        return (128 + ((humanPyramid(rowPosition - 1, columnPosition - 1)) + (humanPyramid(rowPosition - 1, columnPosition))) // 2)


def positionByLetter(rowPosition, columnPosition):
    '''
    This function returns a string of the letter associated with the person at the user-selected row and column positions
    '''
    if rowPosition == 0 and columnPosition == 0:
        return str("A")
    if rowPosition == 1 and columnPosition == 0:
        return str("B")
    if rowPosition == 1 and columnPosition == 1:
        return str("C")
    if rowPosition == 2 and columnPosition == 0:
        return str("D")
    if rowPosition == 2 and columnPosition == 1:
        return str("E")
    if rowPosition == 2 and columnPosition == 2:
        return str("F")
    if rowPosition == 3 and columnPosition == 0:
        return str("G")
    if rowPosition == 3 and columnPosition == 1:
        return str("H")
    if rowPosition == 3 and columnPosition == 2:
        return str("I")
    if rowPosition == 3 and columnPosition == 3:
        return str("J")
    if rowPosition == 4 and columnPosition == 0:
        return str("K")
    if rowPosition == 4 and columnPosition == 1:
        return str("L")
    if rowPosition == 4 and columnPosition == 2:
        return str("M")
    if rowPosition == 4 and columnPosition == 3:
        return str("N")
    if rowPosition == 4 and columnPosition == 4:
        return str("O")   
    
def figure(rowPosition, columnPosition, positionLetter):
    '''
    This function uses a for loop to print a figure of the human pyramid while replacing the chosen person's letter into the pyramid
    '''   
    
    if columnPosition > rowPosition or rowPosition > 4:
        return 0
    
    else:
        #number of rows
        rows = 5
        #number of spaces at each row
        space = rows - 1
    
        #for loop for each row
        for rowNum in range(0, rows):
            #for loop for each space in the row
            for colNum in range(0, space):
                print(end=" ")
        
            #decrease space by 1 before moving to the next row
            space = space - 1
        
            #for loop for each column
            for colNum in range(0, rowNum+1):
                #print the letter at the position if the column and row entered by user matches the one at the loop
                if colNum == columnPosition and rowNum == rowPosition:
                    print(positionLetter, end=" ")
                else:
                    #prints an X
                    print("X ", end="")
            print("\r")
 

    
def main():
    '''
                    This function takes the position of a person in a human pyramid. 
                    This position is categorized by its row position and column
                    position. The function will then print out the weight on that person 
                    and a figure of their position in the human pyramid. 
    '''
    print("\n......................................................................................................................")
    print("............................................WELCOME TO THE HUMAN PYRAMID..............................................")
    print(main.__doc__)

    #While statement continues looping the code until the user wishes to discontinue; hence, breaks
    while True:
        
        #position of human in the row
        rowPosition = int(input("\nEnter the position of the human in a row: \n"))

        #position of the human in the column
        columnPosition = int(input("Enter the position of the human in a column: \n"))

        #call function humanPyramid which is a recursive function. Assign the final weight on the person to finalWeight
        finalWeight = humanPyramid(rowPosition, columnPosition)

        #use the row and column position to decide which letter represents the person's position in the pyramid
        positionLetter = positionByLetter(rowPosition, columnPosition)

        #draw a figure of the person's position in the pyramid marking them by the letter associated with their (row,column)
        figure(rowPosition, columnPosition, positionLetter)

        #as long as the human exists in this pyramid (which we know the column position cannot be greater than the row's position)
        if rowPosition >= columnPosition and rowPosition <= 4:
            #print the weight returned from the recursive function
            print("\nTotal weight on person",positionLetter,"at position (", rowPosition,",",columnPosition,") is", finalWeight,"lbs.")

        #ask for user input to continue or terminate program
        print("\nwould you like to continue? Press any key then enter to continue; otherwise, type 'no' then enter to end this code.")
        s = input()
        print("......................................................................................................................")
        if s == "no":
            print("\n......................................................................................................................")
            print(".....................................................GOODBYE..........................................................")
            print("......................................................................................................................")
            break

#call main function
main()