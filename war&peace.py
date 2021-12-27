

from statistics import mean
import time
import random

class WarAndPeacePseudoRandomNumberGenerator():
    '''
    This class uses a text file to generate pseudo-random numbers using a file war-and-peace.txt
    '''
    def __init__(self, seed, numbits = 32):
        '''
        This method initializes the seed, number of bits which is 32 per the in-class discussion, length, and randNum; this is the constructor 
        '''
        #initialize the random number generator
        self.seed = seed

        #initialize the number of bits which are 32 bits in this program per the in-class discussion
        self.bits = numbits

        #the first run will have a seed value of None, therefore, create a seed number based on the time stamp of the system running it
        if self.seed is None:
            self.seed = time.time()

        #initialize an empty list for the pseudo random numbers
        self.randNum = []

        #read in the file war-and0peace.txt
        openfile = open("war-and-peace.txt", "r")
        
        #length of the read-in text file
        self.length = len(openfile.read())
        


    def random(self):
        '''
        random(self) generates a pseudo random number between 0 and 1 for the 32 bits/ runs
        '''
        #start the random number ar 0
        randNum = 0

        #for loop to generate the 32 bit random numbers; first at 1/2, second at 1/4, third at 1/8; etc (equation is 1/2**i per the in-class discussion)
        for i in range (1, self.bits + 1):
            self.randNum.append(1/2**i)

        #for loop to run 32 times
        for i in range (self.bits):
            #create a string type variable for characters 1 and 2
            char1 = ""
            char2 = ""

            #number of steps or pointer to the next character
            pointer = 100
            
            #when characters 1 and 2 are equal to one another, we'll need to try different numbers
            while char1 == char2:
                #the first character is at a new seed
                char1 = self.character(self.seed)
                #offset the seed by 100 steps to get to the next character
                self.seed = self.seed + pointer
                #get the second character at the new seed
                char2 = self.character(self.seed)
                #offset the seed by 200 steps from the current seed number (this way we can maintain 100 steps between each seed)
                self.seed = self.seed + 2*pointer

            #if the two characters are not equal to one another 
            if char1 != char2:
                #set the larger ASCII value to char 1, and the lower one to char 2
                char1 = max(char1, char2)
                char2 = min(char1,char2)
                #compare the ASCII values of the two characters to one another
                if char1 > char2:
                    randNum += True * self.randNum[i]

        
        #return the random number
        return randNum
    
    def character(self, seed):
        ''' 
        character(self, seed) gets a character from a text file at a specific seed value
        '''
        #set the seed number at the offset by getting the remainder of the seed number and length of the file; this ensures that the seed is within the length of the file
        self.seed = self.seed % self.length
        #read in the text file
        openfile = open("war-and-peace.txt", "r")
        #set seed
        openfile.seek(self.seed)
        #read one character from the seed value
        char = openfile.read(1)
        
        #returns the character
        return char
    
def main():
    ''' 
    This function calls a pseudo-random number generator class that reads in a file war-and-peace.txt and generates those numbers from [0.1)
    '''
    #we're setting the seed at 12345 here, but it can be set at () to allow for the machine's time stamp to take over the first seed
    PRNG = WarAndPeacePseudoRandomNumberGenerator(12345)

    #create an empty list for the random numbers to append them to this list 
    randList = []
    
    #get list of random numbers generated from 0 and 10,000
    for i in range (10001):
        #calling function random() to generate random numbers
        num = PRNG.random()
        #append the numbers to the randList
        randList.append(num)

    #printing first 10 random numbers in the list, for simplicity
    print('\nThe first 10 pseudo-randomly generated numbers are:')
    print(randList[0:10])
    print('\nminimum: {:4f}'.format(min(randList)))
    print('\nmaximum: {:4f}'.format(max(randList)))
    print('\nmean: {:4f}'.format(mean(randList)))
    print('')

main()