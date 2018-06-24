import common
import random

'''Chess Board class
Summary:
    The class is build base piece board
'''
class ChessBoard(object):
    '''Initialize object
    args :
        scope: A choice you want slove queen number

    '''
    def __init__(self,scope):


        # 8*8 chessboard
        self.width = scope
        self.height = scope
        self.pieceNode = []
        self.chessboard = [[0] * self.width for i in range(self.height)]
        #for ridx, rname in enumerate(list('87654321')):
        #    for fidx, fname in enumerate(list('abcdefgh')):
        #        tag = fname+rname
        self.generatePiece_random(scope)

    def horizonCoordinate(self):
        common.tabFour()

        for i in range (1,self.width+1):
            print(common.chessMap_from_index[i],end=" ")

        print()
        common.tabTwo()

        for i in range(0, self.width + 10):
            print("一", end="")

        common.enter()
    def verticalCorrdinate(self,cols):
        if cols <= 9:
            common.tabThree()
            print(cols,end=" ")
        else:
            common.tabTwo()
            print(cols, end=" ")

    def showPiece(self,rows,cols):
        if self.chessboard[rows][cols] == 1:
            return 'x'
        else:
            return ' '

    def showBoard(self):
        i =False
        #self.horizonCoordinate()
        for i in range(self.height):
            #self.verticalCorrdinate(i+1)
            for j in range(self.width):
                print("│", end="")
                print(self.showPiece(i,j),end="")
            print()
            #common.tabTwo()
            for j in range(self.width+10):
                print("一", end="")

            common.enter()
    '''Generate Piece
    Summary: 
        generate piece by random which range 0 ~ (width-1)
    args:
        number : your width
    '''
    def generatePiece_random(self,number):

        currentNumber = number-1
        for i in range (0,number):

            randomCol = random.randint(0,currentNumber)

            self.chessboard[i][randomCol] = 1

            self.pieceNode.append(randomCol)

    '''Move to 
    Summary:
        This will be shifted
    Args:
        before: current location
        after: Shifting set
    '''
    def moveTo(self,before,after):
        bRow = before[0]
        bCol = before[1]

        aRow = after[0]
        aCol = after[1]

        if self.chessboard[bRow][bCol] == 1:
            if self.chessboard[aRow][aCol] == 1:
                return False
            else:
                self.chessboard[aRow][aCol] = 1
                self.chessboard[bRow][bCol] = 0
                '''
                
                print("offset before ",end="")
                common.printLocation(bRow,bCol)
                print("after ",end='')
                common.printLocation(aRow,aCol)
                
                '''
        else:
            return  False



