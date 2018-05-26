import common
from  queen import  *
import math
'''
this class is Hill-Climb algorithm
'''

class Algorithm(Queen):
    def __init__(self,scope):
        Queen.__init__(self,scope)





    """
    Summary:
        this is check collision piece in board
    """
    def judgeBoard(self):
        collision = 0
        for i in range(0,self.width):
            #print('--------',i,'-----------')
            pieceCoordinate = self.pieceNode[i]
            collision += self.searchAllCollision(pieceCoordinate[0],pieceCoordinate[1])
            #common.printLocation(pieceCoordinate[0],pieceCoordinate[1])


        return collision
    """
    Summary:
        using random to search path
    """
    def randomSearch(self,pieceCoordinate):
        randomCol = random.randint(0, 7)
        self.moveTo([pieceCoordinate[0],pieceCoordinate[1]],[pieceCoordinate[0],randomCol])

    """Hill Climb Spread out tree
    Summary:
        the method is spread tree and search the path which are divided into three types:
        1.Best path : the node is a bit less than current node collision
        2.Normal path : the node is same as current node collision which is collect to listArray and choice by randam
        3.Worst path : the node is more than current node collision so you don't want to move it
        the heuristic function is :
            select Best > Normal(random) > worst(current path)
    Args:
        pieceCoordinate : your piece location
        collisionNow : current collision
    Return:
        listArray: reback node and refresh recode list
    """
    def HCspreadOutTree(self,pieceCoordinate):
        bestFlag = False
        normalFlag = False
        bestFirst = 10
        normalList = []
        collisionNow = self.judgeBoard()

        tempCoordinate = pieceCoordinate
        for i in range (0,self.width):
            self.moveTo(tempCoordinate, [pieceCoordinate[0], i])
            collison = self.judgeBoard()
            #self.showBoard()
            #print('now -> ',collisionNow,'; ','current -> ',collison,end=' ')
            # Worst case:
            if collison > collisionNow:
                #back
                pass
            # Best case:
            elif collison < collisionNow:

                bestFlag = True
                #bestList.append(i)
                bestFirst = i
            # Normal case:
            elif collison == collisionNow:

                normalFlag = True
                normalList.append(i)

            self.moveTo([tempCoordinate[0], i], tempCoordinate)

        if bestFlag == True:

            #self.moveTo(tempCoordinate, [pieceCoordinate[0], random.choice(bestList)])
            self.moveTo(tempCoordinate, [pieceCoordinate[0], bestFirst])
            #self.offsetStatus(tempCoordinate[1],bestFirst)
            #print('final board')
            #self.showBoard()
            return [pieceCoordinate[0], bestFirst]
        elif normalFlag == True:
            choice = random.choice(normalList)

            self.moveTo(tempCoordinate, [pieceCoordinate[0], choice])
            #print('final board')
            #self.showBoard()
            return [pieceCoordinate[0], choice]

    def restarting(self):
        for i in range (0,self.width):
            randomValue = random.randint(0,self.width-1)
            newLoation = self.pieceNode[i]
            #print (randomValue)
            self.moveTo(self.pieceNode[i],[newLoation[0],randomValue])
            self.pieceNode[i] = [newLoation[0],randomValue]
    """Hill search
    Summary:
        do up to 50 times, if collsion > 0 the hill-climb is no slove it 
    Return:
        calcuate times
    """
    def hillSearch(self):
        collision = 1
        j = 0
        re =0
        while(collision != 0):
            j += 1
            for i in range (0,self.width):


                collision = self.judgeBoard()
                #refresh
                self.pieceNode[i] = self.HCspreadOutTree(self.pieceNode[i])

            #print('final board collision = ',collision)
            #self.showBoard()
            if collision == 0:
                self.showBoard()
                return j
            if j == 1:
                self.restarting()
                j = 0
                re += 1
                print('restarting')
            #self.showBoard()

    '''Simaulted Annealing detlaE = collisionNow - collision
        Summary:
        Args:
        Return:
    '''
    def SAspreadOutTree(self, pieceCoordinate, tempture):
        normalFlag = False
        collisionNow = self.judgeBoard()

        tempCoordinate = pieceCoordinate
        randomMove = random.randint(0, self.width - 1)
        self.moveTo(tempCoordinate, [pieceCoordinate[0], randomMove])
        collision = self.judgeBoard()

        dE = collision - collisionNow



        # best case :
        if dE < 0:
            normalFlag = True
        #elif math.exp(((-1) * dE) / tempture) > ((random.random() % 1000) / 1000):
        elif math.exp(((-1) * dE) / tempture) > ((random.random() % 100) / 100):
            #print('no e', dE, math.exp(((-1) * dE) / tempture))
            normalFlag = True
        else:
            # reback
            normalFlag = False

        tempture *= 0.99
        #You need reset it
        self.moveTo([tempCoordinate[0],randomMove], tempCoordinate)

        if normalFlag == True:
            self.moveTo(tempCoordinate, [pieceCoordinate[0], randomMove])
            return [pieceCoordinate[0], randomMove],tempture

        elif normalFlag == False:
            return tempCoordinate,tempture

    '''
    Initialize the system configuration.
    Randomize x(0).
    Initialize T with a large value.
    Repeat:
        Repeat:
        Apply random perturbations to the state x = x + Δx.
        Evaluate ΔE(x) = E(x + Δx) − E(x):
        if ΔE(x) < 0, keep the new state;
        otherwise, accept the new state with probability P = e− ΔE
            T .
        until the number of accepted transitions is below a threshold level.
            Set T = T − ΔT .
        until T is small enough.
    '''
    def simulatedAnnleaing(self):
        tempture = 5
        collision = 10
        j=0

        while(tempture > 0.00001):

            for i in range(0, self.width):
                j += 1
                collision = self.judgeBoard()

                if collision == 0 :
                    print('final board , do times: ', j,' ; collision : ',collision)
                    self.showBoard()

                    return  j

                self.pieceNode[i],tempture = self.SAspreadOutTree(self.pieceNode[i],tempture)

        collision = self.judgeBoard()
        if collision > 0:
            print('error, collision = ,',collision,' , pls run again')
            print('do times = ',j)
            self.showBoard()









