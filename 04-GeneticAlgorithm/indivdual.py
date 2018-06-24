
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

    """
    Summary:
        Fitness Value
    """
    def computeFitness1(self,goal):
        #return self.judgeBoard()
        fitness = goal

        for i in range(self.scope):
            for j in range(i+1,self.scope):
                if math.fabs(self.pieceNode[i] - self.pieceNode[j]) == j-i:
                    # for each queen guarding another one reduce fitness by 1
                    fitness -= 1
        return  fitness
    """
    Summary:
        Fitness Value
    """
    def computeFitness2(self,goal):
        collision = self.judgeBoard()

        return (goal-collision)



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

