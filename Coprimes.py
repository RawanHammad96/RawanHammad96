def coprime(a,b):
    '''
    This function utilizes a for-loop to find the highest common factor
    for two numbers, with the maximum highest common factor being 1. 
    If the highest common factor for two numbers is 1, this function returns TRUE,
    which means that the two numbers are coprime. 
    '''
    highestCommonFactor = 1

    #assign the smaller entry to x
    if a > b:
        x = b
    else:
        x = a
    
    #loop to find the highest common factor, i
    for i in range(1, x+1):
        #if the numbers a and b divided by i have a remainder of 0:
        if a%i==0 and b%i==0:
            #highest common factor is i
            highestCommonFactor = i

    #if i is 1, then the highest common factor is 1, which returns TRUE
    if highestCommonFactor == 1:
        return True
    #otherwise, returns FALSE if the highest common factor was not 1
    else:
        return False



def coprime_test_loop():
    '''
                    This function takes two numbers from the user then prints 
                    whether the two numbers are coprime or not. 
    '''
    print("")
    print(".......................................WELCOME TO THE COPRIME TEST.......................................")
    print(coprime_test_loop.__doc__)
    print("In number theory, two integers a and b are said to be coprime if the only positive integer that divides both is 1.")
    print("Now let's put this to the test!")
    
    #While statement continues looping the code until the user wishes to discontinue; hence, breaks
    while True:
        #empty line
        print("")

        #input first number as integer and assign it to variable a
        print("Input the first number: ")
        a = int(input())

        #input second number as integer and assign it to variable b
        print("Input the first number: ")
        b = int(input())
        
        #calling function coprime() and passing a and b to the function. Assign the return value of TRUE or FALSE to x
        x = coprime(a,b)

        #check if the returned value assigned to x was True, hence are coprime; otherwise, x is False if they are NOT coprime
        if x == True:
            print(a,"and",b,"are coprime.")
        else:
            print(a,"and",b,"are NOT coprime.")
        
        #empty line
        print("")
        #user input to continue or terminate program
        print("would you like to continue? Press any key then enter to continue; otherwise, type 'no' then enter to end this code.")
        s = input()
        if s == "no":
            print("Goodbye!")
            break

coprime_test_loop()