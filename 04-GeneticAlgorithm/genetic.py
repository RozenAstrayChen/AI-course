from indivdual import *


class Genetic(object):
    def __init__(self,scope):
        self.scope = scope
        self.goal = int((self.scope*(self.scope-1))/2)
        #self.goal = int((self.scope * (self.scope - 1)))

    def showData(self,population,fitnessValue):
        j = 0
        for i in population:
            print("(", fitnessValue[j], ")", i.pieceNode)
            j += 1

    def prepareNextYear(self,population):
        #print(len(population),self.num)
        for i in range(len(population),self.num):
            newIndivdual = Indivdual(self.scope)
            newIndivdual.regenerate()
            population.append(newIndivdual)
        return population
    """
        Summary:
            Initial Population
    """
    def startGA(self,num,probability):
        time = 0
        self.num = num
        self.population = self.initPopulation(num)

        while(1):
            time +=1
            self.fitnessValue = self.fitnessFunction(self.population)

            self.showData(self.population,self.fitnessValue)

            if self.reachGoal():
                print('did times = ',time)
                break
            else:
                time +=1

            survivePopulation = self.selection(self.population,self.fitnessValue)

            # generate chromosome
            generationChromosome = self.Crossover(survivePopulation)




            # grow up to indvidual
            nextPopulation = []
            for i in range(len(generationChromosome)):
                nextPopulation.append(self.growUp(generationChromosome[i]))

            #next generation do fitness
            self.population = nextPopulation
            self.fitnessValue = self.fitnessFunction(self.population)

            if self.reachGoal():
                print('did times = ',time)
                break

            # mutation
            self.population = self.mutation(probability, self.population)





            #self.showData(self.population, self.fitnessValue)
            #
            self.population = self.prepareNextYear(self.population)





    """
        Summary:
            Init Population
        Return:
            population : Indivdual of array
    """
    def initPopulation(self,num):
        population = []
        for i in range(0,num):

            indivdual = Indivdual(self.scope)
            indivdual.regenerate()
            population.append(indivdual)

        return  population


    """
    Summary:
        Fitness Function
    Return:
        fitnessSquence : Indivduals collision of array 
    """
    def fitnessFunction(self, population):
        fitnessSquence = []
        for i in population:
            #fitnessSquence.append(i.computeFitness1(self.goal))
            fitnessSquence.append(i.computeFitness1(self.goal))

        return fitnessSquence

    """
    Summary:
        Selection
    """
    def selection(self,population,fitnessValue):
        clonePopulation =[]
        select = int(self.num * 0.4)
        for i in range (select):
            maxIndex = fitnessValue.index(max(fitnessValue))

            #clone the best chromosome
            clonePopulation.append(population[maxIndex])
            #remove
            population.pop(maxIndex)
            fitnessValue.pop(maxIndex)

        print('----after select-------')
        for i in range(select):
            print(clonePopulation[i].pieceNode)

        return clonePopulation


    """
    Summary:
        Corssover
    """
    def Crossover(self,survivePopulation):
        offSpring = []
        for i in range (0,int(len(survivePopulation)/2)):
            male = random.randint(0,len(survivePopulation)-1)
            maleTemp = survivePopulation[male]
            survivePopulation.pop(male)

            female = random.randint(0, len(survivePopulation) - 1)
            femaleTemp = survivePopulation[female]
            survivePopulation.pop(female)



            #generationChromosome = self.chromosomeSingleSwitch(maleTemp
            #                                             ,femaleTemp)
            generationChromosome = self.chromosomeSingleSwitch(maleTemp
                                                               , femaleTemp)


            offSpring+=generationChromosome

        print('---CrossOver---')
        print('offSpring',offSpring)
        return offSpring



    """
    Summary:
        Mutation
    """
    def mutation(self,probability,population):

        randomInt = random.randint(0, 99)

        if randomInt < probability:
            print("Mutation happen!")

            for i in (0,len(population)-1):
                population[i].switch(self.scope/2)
                print('mutation ivdivdual = ',population[i].pieceNode,"i = ",i)


        return population




    def reachGoal(self):

        '''
        for i in population:

            #print(' collision = ',i.judgeBoard())
            if i.judgeBoard() == 0:
                print('reach point!')
                i.showBoard()
                return True
        '''
        j = 0
        for i in self.fitnessValue:
            if i == self.goal:
                print('reach point!')
                print('=================')
                print(self.population[j].pieceNode)
                self.population[j].print_board()
                return  True
            j +=1




    def chromosomeSingleSwitch(self,male,female):
        #print('male = ',male.pieceNode)
        #print('female = ',female.pieceNode)
        previous1Chromosome = []
        previous2Chromosome = []

        next1Chromosome = []
        next2Chromosome = []

        generationChromosome = []

        chromosomeLen = int((len(male.pieceNode) + len(female.pieceNode))/2)
        previous = int(chromosomeLen*0.4)

        next  = int(chromosomeLen - previous)

        #Single
        for i in range (previous):
            previous1Chromosome.append(male.pieceNode[i])
            previous2Chromosome.append(female.pieceNode[i])

        for i in range (previous,chromosomeLen):
            next1Chromosome.append(male.pieceNode[i])
            next2Chromosome.append(female.pieceNode[i])

        #print('test = ', previous1Chromosome, next2Chromosome)
        newChromosome1 = self.judgementSquence(previous1Chromosome + next2Chromosome)

        generationChromosome.append(newChromosome1)

        newChromosome2 = self.judgementSquence(previous2Chromosome + next1Chromosome)
        generationChromosome.append(newChromosome2)


        return generationChromosome

    def judgementSquence(self,chromosome):

        lossChromosome = []
        for i in range(0,self.scope):
            #for j in range(0,self.scope):
            if i in chromosome:
                pass
            else:
                lossChromosome.append(i)



        for i in range(0,self.scope):
            #print('chromosome = ', chromosome)
            rep = 0
            for j in range(i+1,self.scope):
                if chromosome[i] == chromosome[j]:
                    rep+=1

                if rep >= 1:
                    rep = 0

                    temp = random.randint(0,int(len(lossChromosome)-1))

                    chromosome[j] = lossChromosome[temp]

                    lossChromosome.remove(chromosome[j])

        return chromosome



    def chromsomeQueenSwitch(self,male, female ):

        previous1Chromosome = []
        middle1Chromosome = []
        next1Chromosome = []
        currentChromosome = []


        chromosomeLen = int((len(male.pieceNode) + len(female.pieceNode)) / 2)

        previous = int(chromosomeLen * 0.2)
        middle = int(chromosomeLen * 0.8)
        next = int(chromosomeLen - middle)

        #special
        for i in range (previous,middle):

            middle1Chromosome.append(male.pieceNode[i])

        for i in middle1Chromosome:
            female.pieceNode.remove(i)
        for i in range (0,previous):
            previous1Chromosome.append(female.pieceNode[i])
            female.pieceNode.pop(i)

        next1Chromosome = female.pieceNode

        currentChromosome.append(previous1Chromosome+
                                 middle1Chromosome+
                                 next1Chromosome)

        return currentChromosome




    def findSameValue(self,value,list):
        for i in list:
            if i == value:
                return  False
        return True



    def growUp(self,chromosome):
        new = Indivdual(self.scope)
        new.generatePiece(chromosome)

        return new


