
def GradingLogic(finalGrade):
    '''
    This function will ask you a few questions to check the readiness of your assignment for 
    final submission and will estimate your grade out of all possible points.
    '''

    print("")
    print(".......................................WELCOME TO GRADING LOGIC.......................................")
    print(GradingLogic.__doc__)
    print("Note: There is only", finalGrade, "possible points allowed in this program.")
    print("Please answer the following questions with a simple yes or no:")

    '''
    FIRST QUESTION
    '''
    print("Are you submitting your assignment as a single uncompressed .py file?")
  
    #user input
    x= input() 
    a= "yes"
    b= "no"
  
    #actions based on a yes or no answer
    if x == a:
        print("Great!")
    else:
        print("Your score will automatically be set to 0.")
        #exit the function and continue with regular program
        quit()


    '''
    SECOND QUESTION
    '''
    print("Have you included your name and the date?")

    #user input
    x= input()
    a= "yes"
    b= "no"

    #actions based on a yes or no answer
    if x == a:
        print("Wonderful!")
    else:
        print("Your score will automatically be set to 0.")
        #exit the function and continue with regular program
        quit()


    '''
    THIRD QUESTION
    '''
    print("Have you included the required honor statement?")

    #user input
    x= input()
    a= "yes"
    b= "no"

    #actions based on a yes or no answer
    if x == a:
        print("Moving on!")
    else:
        print("Your score will automatically be set to 0.")
        #exit the function and continue with regular program
        quit()


    '''
    FOURTH QUESTION
    '''
    print("Have you included a link to an unlisted 3-minute YouTube video presenting the code and answering the assigned questions?")

    #user input
    x= input()
    a= "yes"
    b= "no"

    #actions based on a yes or no answer
    if x == a:
        print("Good!")
    else:
        print("Your score will automatically be set to 0.")
        #exit the function and continue with regular program
        quit()


    '''
    IF ALL PREVIOUS ANSWERS WERE YES, THIS CODE BLOCK WILL BE REACHED 
    '''
    #Correctness of the code question
    print("Please input a number between 0 and 10 for the following questions:")
    print("Out of ten points, how would you evaluate the correctness of the code?")
    correctnessPoints= int(input())

    #Elegance of the code question
    print("Out of ten points, how would you evaluate the elegance of the code (data structure selection, algorithm efficiency, function implementation, etc.)?")
    elegancePoints= int(input())

    #Code hygiene question
    print("Out of ten points, how would you evaluate your code hygiene (white space, docstrings, etc.)?")
    hygienePoints= int(input())

    #YouTube video question
    print("Out of ten points, how would you rate your YouTube video's explanation of this code?")
    youtubePoints= int(input())

    #sum of all possible points WITHOUT late policy
    Total = youtubePoints + hygienePoints + elegancePoints + correctnessPoints

    #Late assignments deductions
    print("Did you submit your assignment on time? You can answer with a yes or no.")
    x= input()
    a= "yes"
    b= "no"

    #if the assignment was NOT late:
    if x == a:
        finalGrade = Total
    #if the assignment IS late: 
    else:
        print("Unfortunately, late assignments lose one percent of the total possible points per hour.")
        print("How many hours did you wait until you submitted your assignment?")
        hours = int(input())
        deductedPoints = hours * 0.4
        newTotal = Total - deductedPoints
        finalGrade = newTotal

    return finalGrade

print("Your grade is", GradingLogic(40), "out of 40 possible points.")