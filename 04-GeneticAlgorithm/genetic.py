from indivdual import *


class Genetic(object):
    def __init__(self,scope):
        self.scope = scope
        self.goal = int((self.scope*(self.scope-1))/2)

    def showData(self,population,fitnessValue):
        j = 0
        for i in population:
            print("(", fitnessValue[j], ")", i.pieceNode)
            j += 1

    def prepareNextYear(self,population):
        for i in range(len(population)-1,self.num):
            population.append(Indivdual(self.scope))
        return population
    """
        Summary:
            Initial Population
    """
    def startGA(self,num):
        time = 0
        self.num = num
        self.population = self.initPopulation(num)

        while(1):
            time +=1
            self.fitnessValue = self.fitnessFunction(self.population)

            self.showData(self.population,self.fitnessValue)

            if self.reachGoal(self.population):
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
            self.showData(self.population, self.fitnessValue)
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
            fitnessSquence.append(i.computeFitness(self.goal))

        return fitnessSquence

    """
    Summary:
        Selection
    """
    def selection(self,population,fitnessValue):
        clonePopulation =[]
        select = int(self.num * 0.6)
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
            '''
            while True:
                print(len(survivePopulation))
                female = random.randint(0, len(survivePopulation) - 2)
                print('male  =', male, 'female =', female)
                if male != female:
                    break
            '''
            #print('male = ',male)
            #print('female = ',female)


            generationChromosome = self.chromosomeSwitch(maleTemp
                                                         ,femaleTemp)


            offSpring+=generationChromosome

        print('---CrossOver---')
        print('offSpring',offSpring)
        return offSpring



    """
    Summary:
        Mutation
    """
    def Mutation(self):
        pass

    def reachGoal(self,population):
        for i in population:
            print(' collision = ',i.judgeBoard())
            if i.judgeBoard() == 0:
                print('reach point!')
                i.showBoard()
                return True



    def chromosomeSwitch(self,male,female):
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
            next1Chromosome.append(female.pieceNode[i])
            next2Chromosome.append(male.pieceNode[i])


        generationChromosome.append(previous1Chromosome + next1Chromosome)
        generationChromosome.append(previous2Chromosome + next2Chromosome)
        return generationChromosome


    def growUp(self,chromosome):
        new = Indivdual(self.scope)
        new.generatePiece(chromosome)

        return new


