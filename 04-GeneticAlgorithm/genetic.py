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
        #print(len(population),self.num)
        for i in range(len(population),self.num):
            population.append(Indivdual(self.scope))
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

            if self.reachGoal(self.population):
                print('did times = ',time)
                break
            else:
                time +=1

            survivePopulation = self.selection(self.population,self.fitnessValue)

            # generate chromosome
            generationChromosome = self.Crossover(survivePopulation)
            # mutation
            generationChromosome = self.mutation(probability, generationChromosome)



            # grow up to indvidual
            nextPopulation = []
            for i in range(len(generationChromosome)):
                nextPopulation.append(self.growUp(generationChromosome[i]))

            #next generation do fitness
            self.population = nextPopulation
            self.fitnessValue = self.fitnessFunction(self.population)




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
            fitnessSquence.append(i.computeFitness2(self.goal))

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
        #print('offSpring',offSpring)
        return offSpring



    """
    Summary:
        Mutation
    """
    def mutation(self,probability,population):



        for i in (0,len(population)-1):

            randomInt = random.randint(0,100)
            if randomInt <= probability:
                print("Mutation happen!")


                for j in range(0,int(self.scope/2)):

                    mutationChromosome = random.randint(0,self.scope-1)
                    mutationIndex = random.randint(0,self.scope-1)

                    #print(i, mutationIndex)
                    population[i][mutationIndex] = mutationChromosome
                #print('muation is index ',i," after is ",population[i])

                #print("mutation after =",population)

        return population




    def reachGoal(self,population):
        for i in population:
            print(' collision = ',i.judgeBoard())
            if i.judgeBoard() == 0:
                print('reach point!')
                i.showBoard()
                return True



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


        generationChromosome.append(previous1Chromosome + next2Chromosome)
        generationChromosome.append(previous2Chromosome + next1Chromosome)
        return generationChromosome

    def chromosomeTwoSwitch(self, male, female):
        previous1Chromosome = []
        previous2Chromosome = []

        middle1Chromosome = []
        middle2Chromosome = []

        next1Chromosome = []
        next2Chromosome = []

        generationChromosome = []

        chromosomeLen = int((len(male.pieceNode) + len(female.pieceNode)) / 2)

        previous = int(chromosomeLen*0.3)
        middle = int(chromosomeLen*0.8)


        #Two-point
        for i in range (previous):
            previous1Chromosome.append(male.pieceNode[i])
            previous2Chromosome.append(female.pieceNode[i])

        for i in range (previous,middle):
            middle1Chromosome.append(male.pieceNode[i])
            middle2Chromosome.append(female.pieceNode[i])

        for i in range (middle,chromosomeLen):
            next1Chromosome.append(male.pieceNode[i])
            next2Chromosome.append(female.pieceNode[i])



        generationChromosome.append(previous1Chromosome+
                                    middle2Chromosome+
                                    next1Chromosome)
        generationChromosome.append(previous2Chromosome+
                                    middle1Chromosome+
                                    next2Chromosome)

        return generationChromosome



    def growUp(self,chromosome):
        new = Indivdual(self.scope)
        new.generatePiece(chromosome)

        return new


