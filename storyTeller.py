
import random

#GLOBAL VARIABLES: setting the file names as global variables as they will be used multiple times within this program 
plot_names = 'plot_names.txt'
plot_adjectives = 'plot_adjectives.txt'
plot_professions = 'plot_professions.txt'
plot_adjectives_evil = 'plot_adjectives_evil.txt'
plot_villians = 'plot_villians.txt'
plot_villian_job = 'plot_villian_job.txt'
plot_verbs = 'plot_verbs.txt'  

class SimplePlotGenerator:
    '''
    Class SimplePlotGenerator generates a plot that returns "Something happens" when queried
    '''
    #initial variable
    def registerView(self, pg):
        '''
        registerView(self, pg) initializes self.pg
        '''
        self.pg = pg
    
    def generate(self):
        '''
        generated(self) returns "something happens" when queried
        '''
        return "Something happens" 

#when queried for a plot returns a random plot produced from the seven files, extend SimplePlotGenerator
class RandomPlotGenerator(SimplePlotGenerator):
    '''
    Class RandomPlotGenerator is inherited from SimplePlotGenerator. It open 7 text files, selects a random word within those files, then returns a sentence/ story. 
    '''
    #in this situation, return the plot by format
    def generate(self):
        '''
        generate(self) method is modified here; it uses the global variables (the text files), opens them, selects a random word in each file, 
        then combines them into a sentence. The sentence, self.pg, is returned.  
        '''
        #declaring global variable within function generate(self)   
        global plot_names, plot_villians, plot_adjectives, plot_adjectives_evil, plot_professions, plot_villian_job, plot_verbs
        
        #open files, read them, splitlines, select a random word, then assign it to the appropriate variable
        name = random.choice(open(plot_names).read().splitlines())
        adjective = random.choice(open(plot_adjectives).read().splitlines())
        profession = random.choice(open(plot_professions).read().splitlines())
        verb = random.choice(open(plot_verbs).read().splitlines())
        adjective_evil = random.choice(open(plot_adjectives_evil).read().splitlines())
        villian_job = random.choice(open(plot_villian_job).read().splitlines())
        villian = random.choice(open(plot_villians).read().splitlines())

        #combine all words into a story/ string called self.pg
        self.pg = '{}, a {} {}, must {} the {} {}, {}.'.format(name, adjective, profession, verb, adjective_evil, villian_job, villian)
    
        #return the story/ string/ sentence 
        return self.pg

class InteractivePlotGenerator(SimplePlotGenerator):
    '''
    InteractivePlotGenerator is inherited from the SimplePlotgenerator class; it opens the files (global variables), reads them, splits lines, 
    selects 5 words from each file, appends them to a list, then uses queryUser to allow the user to select a word. The words selected are finally 
    concatenated into a string/sentence/story and returns it. 
    '''
    def generate(self):
        '''
        Generate(self) is a modified method; it selects 5 words from each file and queries user to select one then concatenates the results into a string.
        This function returns self.pg which is a story/ string/ sentence
        '''
        #declaring global variable within function generate(self)   
        global plot_names, plot_villians, plot_adjectives, plot_adjectives_evil, plot_professions, plot_villian_job, plot_verbs

        #creating a list for the 5 words that we will be selecting in the for loop below
        namesList = []
        adjectivesList = []
        professionsList = []
        verbsList = []
        evilAdjList = []
        villianList = []
        villianJobList = []

        #for words in the range 0 inclusive to 5 exclusive
        for i in range(0, 5):

            #open the file, read it, splitlines, select random word, assign to name
            verb = random.choice(open(plot_verbs).read().splitlines())
            #append the word to the list of 5 verbs
            verbsList.append(verb)

            #open the file, read it, splitlines, select random word, assign to name
            name = random.choice(open(plot_names).read().splitlines())
            #append the word to the list of 5 names
            namesList.append(name)

            #open the file, read it, splitlines, select random word, assign to name
            adjective = random.choice(open(plot_adjectives).read().splitlines())
            #append the word to the list of 5 adjectives
            adjectivesList.append(adjective)

            #open the file, read it, splitlines, select random word, assign to name
            profession = random.choice(open(plot_professions).read().splitlines())
            #append the word to the list of 5 professions
            professionsList.append(profession)

            #open the file, read it, splitlines, select random word, assign to name
            villianJob = random.choice(open(plot_villian_job).read().splitlines())
            #append the word to the list of the villian jobs or careers
            villianJobList.append(villianJob)
            
            #open the file, read it, splitlines, select random word, assign to name
            evilAdj = random.choice(open(plot_adjectives_evil).read().splitlines())
            #append the word to the list of 5 evil adjectives
            evilAdjList.append(evilAdj)

            #open the file, read it, splitlines, select random word, assign to name
            villian = random.choice(open(plot_villians).read().splitlines())
            #append the word to the list of 5 villians 
            villianList.append(villian)

        #query user to select the name, adjective; etc, then assign each entry (which is an integer) to a choice
        choice1 = int(self.pg.queryUser("Please, print a number corresponding to your name of choice:\n1. {}   2. {}   3. {}   4. {}   5. {} \n=> ".format(namesList[0],namesList[1],namesList[2],namesList[3],namesList[4])))
        choice2 = int(self.pg.queryUser("\nPlease, print a number corresponding to your adjective of choice:\n1. {}   2. {}   3. {}   4. {}   5. {} \n=> ".format(adjectivesList[0],adjectivesList[1],adjectivesList[2],adjectivesList[3],adjectivesList[4])))
        choice3 = int(self.pg.queryUser("\nPlease, print a number corresponding to your profession of choice:\n1. {}   2. {}   3. {}   4. {}   5. {} \n=> ".format(professionsList[0],professionsList[1],professionsList[2],professionsList[3],professionsList[4])))
        choice4 = int(self.pg.queryUser("\nPlease, print a number corresponding to your verb of choice:\n1. {}   2. {}   3. {}   4. {}   5. {} \n=> ".format(verbsList[0],verbsList[1],verbsList[2],verbsList[3],verbsList[4])))
        choice5 = int(self.pg.queryUser("\nPlease, print a number corresponding to your 'evil' adjective of choice:\n1. {}   2. {}   3. {}   4. {}   5. {} \n=> ".format(evilAdjList[0],evilAdjList[1],evilAdjList[2],evilAdjList[3],evilAdjList[4])))
        choice6 = int(self.pg.queryUser("\nPlease, print a number corresponding to your villian-career of choice:\n1. {}   2. {}   3. {}   4. {}   5. {} \n=> ".format(villianJobList[0],villianJobList[1],villianJobList[2],villianJobList[3],villianJobList[4])))
        choice7 = int(self.pg.queryUser("\nPlease, print a number corresponding to your villian name of choice:\n1. {}   2. {}   3. {}   4. {}   5. {} \n=> ".format(villianList[0],villianList[1],villianList[2],villianList[3],villianList[4])))

        #jsut a line to separate results 
        print("......................................................................................................................\n")

        #get the story/ sentence by using the user's input, subtracting 1 for the position/index in the list, then concatenate into a story
        self.pg = '\n'+namesList[choice1-1]+', a ' +adjectivesList[choice2-1]+' ' +professionsList[choice3-1]+', must '+verbsList[choice4-1]+' the '+evilAdjList[choice5-1]+ ' ' +villianJobList[choice6-1] +', '+ villianList[choice7-1]+'.'

        #return the sentence/ story/ string self.pg
        return self.pg


class Viewer():
    '''
    Viewer() class displays the results of the generated plot/ sentence/ output
    '''
    def registerGenerator(self, dr):
        '''
        Initializes registerView
        '''
        self.dr = dr
        self.dr.registerView(self)
    
    def queryUser(self, str):
        '''
        Gets user input/ query
        '''
        return input(str)

    def generate(self):
        '''
        calls generate() method
        '''
        print(self.dr.generate())


def main():
    '''
                            This program uses classes SimplePlotGenerator, RandomPlotGenerator, and InteractivePlotGenerator
                    which first returns 'something happens', next creates a story or a sentence randomly, then creates a story or sentence
                                                                 based on user input.
    '''
    print("\n......................................................................................................................")
    print("............................................WELCOME TO THE PLOT GENERATOR..............................................")
    print(main.__doc__)

    dv = Viewer()
    print("\n......................................................................................................................\n")
    print("RESULTS OF SIMPLE-PLOT-GENERATOR:\n")
    dv.registerGenerator(SimplePlotGenerator() )
    dv.generate()

    print("\n......................................................................................................................\n")
    print("RESULTS OF RANDOM-PLOT-GENERATOR:\n")
    dv.registerGenerator(RandomPlotGenerator() )
    dv.generate()

    print("\n......................................................................................................................\n")
    print("RESULTS OF INTERACTIVE-PLOT-GENERATOR:\n")
    dv.registerGenerator(InteractivePlotGenerator() ) 
    dv.generate()
    print("")

    print("......................................................................................................................")
    print(".....................................................GOODBYE..........................................................")
    print("......................................................................................................................")

main()