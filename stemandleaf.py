'''
Author: Rawan Hammad
Date: 09/27/2021
3-Minute YouTube Video: https://youtu.be/Dqe8Besdpvw 
"I have not given or received any unauthorized assistance on this assignment"
Homework #2
'''



from os import read



def readFile(userInput):
    '''
    This function uses the user's input of 1, 2, or 3 to 
    read-in the appropriate file then returns lineList. 
    '''
    
    if userInput == "1":
        #reads in StemAndLeaf1
        filename = 'C:/Users/rawan/OneDrive/Desktop/DePaul/DSC420-PYTHON/Assignment2/StemAndLeaf1.txt'
        infile = open(filename, "r")
        lineList = infile.readlines() 
        infile.close() 

        return lineList

    if userInput == "2":
        filename = 'C:/Users/rawan/OneDrive/Desktop/DePaul/DSC420-PYTHON/Assignment2/StemAndLeaf2.txt'
        infile = open(filename, "r")
        lineList = infile.readlines() 
        infile.close() 

        return lineList

    if userInput == "3":
        filename = 'C:/Users/rawan/OneDrive/Desktop/DePaul/DSC420-PYTHON/Assignment2/StemAndLeaf3.txt'
        infile = open(filename, "r")
        lineList = infile.readlines() 
        infile.close() 

        return lineList



def Conditions(lineList):
    '''
    Conditions function uses the selected file input to
    find the stem and leaf for each number in the list,
    eventually returning the stemlist with the nested list of leaves
    '''

    #create a list of stems then append an 'infinite' number of lists to the stem list to 
    # create a nested list that holds all leaves
    stemList = []
    for i in range(0,10000):
        stemList.append([])
    
    #Appending leaves to the respective stems
    for i in lineList:
        #num is the 'full' number in the list converted to integer
        num = int(i)

        #append the last digit of the number to the designated position within the list; position matches the stem
        stemList[num//10].append(num%10)
    
    #return the nested list holding the leaves
    return stemList



def printStemAndLeaf(stemList, userInput):
    '''
    This function creates a stem and leaf plot using the nested list, AKA stemList,
    created in the Conditions function. Note that the output range is based on the chosen
    file by the user, which was requested in main().
    '''
    if userInput =="1":
        #Note range was adjusted based on the lowest and highest numbers I found in the file
        for stemNumber in range(1, 10):
            print("Stem",stemNumber,":")
            #print the leaflist at each stemnumber in the nested list
            for leafList in stemList[stemNumber]:
                print(leafList,end=" ")
            print('\n')

    if userInput =="2":
        #Note range was adjusted based on the lowest and highest numbers I found in the file
        for stemNumber in range(1, 18):
            print("Stem",stemNumber,":")
            #print the leaflist at each stemnumber in the nested list
            for leafList in stemList[stemNumber]:
                print(leafList,end=" ")
            print('\n')

    if userInput =="3":
        #Note range was adjusted based on the lowest and highest numbers I found in the file
        for stemNumber in range(99, 111):
            print("Stem",stemNumber,":")
            #print the leaflist at each stemnumber in the nested list
            for leafList in stemList[stemNumber]:
                print(leafList,end=" ")
            print('\n')



def main():
    '''
    This program will ask you to input 1, 2, or 3, which will then call a function that imports the appropriate file,
    then, call a few other functions that create and print the stem and leaf plot.
    '''
    print("")
    print(".......................................WELCOME TO THE STEM & LEAF PLOT MAKER.......................................")
    print(main.__doc__)
    
    #While statement to keep program looping until user types 'no'
    while True:
        print("\nPlease input 1, 2 or 3 to import the dataset:")
        userInput = input()
        print("")

        #use userInput of 1, 2, or 3 to read the file. This will create a list then assign the list to variable selectedList
        selectedList = readFile(userInput)

        #selectedList is used to create the stem and leaf diagram in the Conditions function. This is then assigned to variable theFinalList.
        theFinalList = Conditions(selectedList)

        #TheFinalList and userInput is used to print the stem and leaf diagram in this step
        printStemAndLeaf(theFinalList, userInput)

        #user input to continue or terminate program
        print("\n.................................................................................................")
        print("would you like to continue? Press any key then enter to continue; otherwise, type 'no' then enter to end this code.")
        answer = input()
        if answer == "no":
            print(".................................................................................................")
            print("\n.............................................GOODBYE.............................................")
            print(".................................................................................................")
            
            #while loop ends
            break

main()
