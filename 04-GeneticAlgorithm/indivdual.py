
from queen import *
import math

class Indivdual(Queen):
    def __init__(self,scope):
        self.scope = scope
        Queen.__init__(self, scope)


    def generatePiece(self,chromosome):
        self.pieceNode = []
        self.chessboard = [[0] * self.width for i in range(self.height)]

        for i in range(0, self.scope):


            self.chessboard[i][chromosome[i]] = 1

            self.pieceNode.append(chromosome[i])

    def switch(self, count):
        ''' swithed queen places 'count' times'''
        count = int(count)

        for i in range(count):
            j = random.randint(0, self.scope - 1)
            k = random.randint(0, self.scope - 1)
            self.pieceNode[j], self.pieceNode[k] = self.pieceNode[k], self.pieceNode[j]



    def regenerate(self):
        ''' randomly moves scope/2 queens
        used for creating new generation'''

        # randomly switvh 2 itmes
        #self.switch(self.scope/2)
        self.switch(3)

        # get a random number if it's lower than 0.25 switch anither item
        if random.uniform(0, 1) < 0.25:
            self.switch(1)

    """
    Summary:
        Fitness Value
    """
    def computeFitness1(self,goal):
        #return self.judgeBoard()
        fitness = goal

        for i in range(self.scope):
            for j in range(i+1,self.scope):
                if math.fabs(self.pieceNode[i] - self.pieceNode[j]) == j - i:
                    # for each queen guarding another one reduce fitness by 1
                    fitness -= 1
        return  fitness
    """
    Summary:
        Fitness Value
    """
    def computeFitness2(self,goal):
        collision = self.judgeBoard()

        return (collision)

    def print_board(self):
        ''' prints current board in a nice way!'''
        for row in range(self.scope):
            print("", end="|")

            queen = self.pieceNode.index(row)

            for col in range(self.scope):
                if col == queen:
                    print("Q", end="|")
                else:
                    print("_", end="|")
            print("")


    """
    Summary:
        this is check collision piece in board
    """
    def judgeBoard(self):
        collision = 0
        for i in range(0,self.width):
            #print('--------',i,'-----------')
            pieceCoordinate = self.pieceNode[i]
            #collision += self.searchAllCollision(pieceCoordinate[0],pieceCoordinate[1])
            collision += self.searchAllCollision(i,pieceCoordinate)
            #common.printLocation(pieceCoordinate[0],pieceCoordinate[1])


        return collision

