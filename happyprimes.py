'''
Author: Rawan Hammad
Date: 10/04/2021
3-Minute YouTube Video: https://youtu.be/aQqDj-PZJDU 
"I have not given or received any unauthorized assistance on this assignment"
Homework #3
'''


def isHappy(a):
    '''
    This function utilizes a while loop to calculate the sum of the
    square of numbers then returns the sum to booleanReturn to check if 
    the sum is 1 or 4.
    '''

    #setting variables sum and remainder 
    sum = 0
    remainder = 0

    #while the user's input is not 0
    while a > 0:
        #calculate the remainder
        remainder = a%10
        #sum of the square of the remainder and previous sum
        sum += remainder**2
        #now assign a divided by 10 to a
        #if a is small (for example, 0.1, 0.2, etc), a = 0. if a is NOT greater than 0, it will exit out of this loop and return sum
        a = a//10

    return sum



def booleanReturn(a):
    '''
    This function will compare the sum returned by isHappy to 1 or 4.
    If the sum (previousResult) isn't equal to 1 or 4, it will call function isHappy again. 
    Once sum/previousResult is equal to 1 or 4, booleanReturn will return True if it's 1, False if it's 4, to main().
    '''
    previousResult = a
    #as long as sum returned from isHappy is NOT 1 or 4, this will keep running
    while(previousResult != 1 and previousResult != 4):
        #previousResult is the sum returned from isHappy; if it's NOT 1 or 4, it will take the 'previous' result and run isHappy again
        previousResult = isHappy(previousResult)

    #once the result is 1 or 4, it will exit out of the loop above and assign the sum/previousResult to Final Result
    finalResult = previousResult
     
    #Happy numbers always ends with a sum of 1 
    if finalResult == 1:    
        return True
    #Unhappy numbers always end with a sum of 4   
    elif finalResult == 4:    
        return False



def isPrime(number):
    '''
    This function will check if a number is prime by checking for remainders. 
    if the remainder is 0 when divided by range(2,number), return False. Otherwise, 
    the number is a prime number and the function returns True. Note the exceptions 1 and 2. 
    '''

    #for other prime numbers that are not 1 or 2
    if number > 1:
        for i in range(2, number):
            #if number divided by range(2,number) has a remainder of 0, number isn't prime, hence return False
            if (number % i) == 0:
                return False    
        else:
            return True 

    #Accounting for exceptions
    if number == 1: #1 is NOT a prime number
        return False
    if number == 2: #2 is a prime number
        return True



def main():
    '''
                    This function takes an integer from the user then prints whether the 
                    integer is a happy prime, sad prime, happy non-prime, or sad non-prime. 
    '''
    print("\n....................................................................................................................")
    print("..........................................WELCOME TO THE HAPPY-PRIME TEST...........................................")
    print(main.__doc__)
    
    #While statement continues looping the code until the user wishes to discontinue; hence, breaks
    while True:
        
        #input an integer
        print("\nInput a non-zero integer: ")
        a = int(input())
        
        #calling function booleanReturn, which returns True or False for happy, sad, respectively. 
        x = booleanReturn(a)

        #calling function isPrime, which returns True or False for prime or non-prime, respectively. 
        y = isPrime(a)

        '''
        Display Output
        '''
        #if number is both happy and prime
        if x == True and y == True:
            print("\n")
            print(a,"is a happy prime number.\n")

        #if number is sad and prime
        elif x == False and y == True:
            print("\n")
            print(a,"is a sad prime number.\n")

        #if number is happy and non-prime
        elif x == True and y == False:
            print("\n")
            print(a,"is a happy non-prime number.\n")

        #if number is sad and non-prime
        elif x== False and y == False:
            print("\n")
            print(a,"is a sad non-prime number.\n")

        #user input to continue or terminate program
        print("\nwould you like to continue? Press any key then enter to continue; otherwise, type 'no' then enter to end this code.")
        s = input()
        if s == "no":
            print("\n....................................................................................................................")
            print("....................................................GOODBYE.........................................................")
            print("....................................................................................................................")
            break


main()