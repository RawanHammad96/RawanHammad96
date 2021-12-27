'''
Author: Rawan Hammad
Date: 10/25/2021
3-Minute YouTube Video: https://youtu.be/Ehpbn-qbioE 
"I have not given or received any unauthorized assistance on this assignment"
Homework #6, Program #1
'''


def isPalindrome(date):
    '''
    isPalindrome checks if a string is a palindrome or not by reversing it then return True if it is a palindrome; otherwise, returns None
    '''
    #remove '/' from the date and replace it with 'nothing' then assign it to cleanDate
    cleanDate = date.replace("/","")

    #use [::-1] to reverse the given date and assign it to variable reversedDate
    reversedDate = cleanDate[::-1]

    #compare the clean date with the reversed date
    if cleanDate == reversedDate:
        #returns true if the reverse of the date matches the date; hence, palindrome condition is met 
        return True

    #returns none if the condition is not met

def display():
    '''
    display() will open the file in read mode then display all the lines in the file
    '''
    #reopen the file in read mode
    file = open('C:/Users/rawan/OneDrive/Desktop/DePaul/DSC420-PYTHON/Assignment6/arePalindromes.txt', "r")

    #read lines from the file
    line= file.readline()
    while(line!=""):
        print(line)
        line=file.readline()

    #close the file
    file.close()

def date():
    '''
    date() generates all possible dates in the 21st century, uses a function called isPalindrome
    to find palindrome dates, then writes those palindrome dates to a file called arePalindromes.txt. 
    NOTE: his function assumes that February is 28 days long. 
    '''
    #list of days in a month; 28 days in February; position 0 is 0 since first month starts at position 1 in the list with 31 days
    daysInMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #file name is arePalindromes.txt, created and opened in write mode
    file = open('C:/Users/rawan/OneDrive/Desktop/DePaul/DSC420-PYTHON/Assignment6/arePalindromes.txt', "w")

    #multiple loops to generate the date:
    #for years in the 21st century, from 2000 to 2099
    for year in range(2000, 2100):
        #for months in the range of 1 to 12
        for month in range(1, 13):
            #for days in the range of 1 to the number of days in a month per the daysInMonths list
            for day in range(1, daysInMonths[month] + 1):
                
                #this will be used for formatting
                slash = "/"

                #formatting for each day, month, and year combo with 2 spaces for each day and month, 4 for the year to get the DD/MM/YYYY format
                d = "{0:0=2d}".format(day)
                m = "{0:0=2d}".format(month)
                y = "{0:0=4d}".format(year)

                #concatenate strings to form the date DD/MM/YYYY
                date = d + slash + m + slash + y
               
                #assign the returned value True or None from function isPalindrome to palindromesBoolean
                palindromesBoolean = isPalindrome(date)
                #if isPalindrome returns True
                if palindromesBoolean == True:
                    #writes to file and appends a space to separate entries 
                    file.write(date + ' ')
    #close the file
    file.close()

def main():
    '''
                    This program uses several functions to decide whether a 21st century date is a palindrome or not. 
                        The output is printed out to a text file and displayed at the end of this program (below). 
    '''
    print("\n......................................................................................................................")
    print(".............................................WELCOME TO PALINDROME DATES..............................................")
    print(main.__doc__)

    #calling function date
    date()

    #display contents of the file
    display()
  
main()
