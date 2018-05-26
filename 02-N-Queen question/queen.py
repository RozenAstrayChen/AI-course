from board import  *
from common import  *

class Queen(ChessBoard):
    def __init__(self,scope):
        ChessBoard.__init__(self,scope)


    def searchQueen(self,rows):
        for i in range (0,self.width):
            if self.chessboard[rows][i] == 1:
                return [rows,i]
            else:
                return None

    def searchAllCollision(self,row,col):

        c1 =  self.colsCollision(row,col)
        c2 = self.positiveObliqueCollision(row,col)

        c3 = self.negativeObliqueCollision(row,col)


        #print("col collision= ",c1," : oblique positive collision= ",c2,"oblique negative collision=",c3)
        return  c1+c2+c3
    """
    search cols and return how cols is collision
    """
    def colsCollision(self,row,col):
        collisionNum = 0
        for i in range(0,self.width):
            # that is you search collision piece

            if self.chessboard[i][col] == 1:
                if i != row :
                    collisionNum += 1

        return  collisionNum

    """summary
            cal positive oblique collision
        args:
            row
            col
    """
    def positiveObliqueCollision(self,row,col):

        return  self.__calObliqueCollision(row,col,True)
    """summary
                cal Negative oblique collision
        args:
            row
            col
    """
    def negativeObliqueCollision(self,row,col):
        return  self.__calObliqueCollision(row,col,False)


    """summary
            divided into third Quadrant, 
            row > cols ,row = cols ,row < cols
        args:
            row
            col
            value : this is offset arry
        return:
            collisionNum : cal collisison times
    """
    def __calObliqueCollision(self,row,col,value):
        collisionNum = 0


        if value == True:
            #print('-----P------')
            offsetRow, offsetCol = self.__currentLocation(row, col, value)
            #printLocation(row,col)
            while offsetRow != self.width and offsetCol != self.width:

                #printLocation(offsetRow, offsetCol)
                if self.chessboard[offsetRow][offsetCol] == 1:
                    if offsetRow != row and offsetCol != col:

                        collisionNum += 1

                offsetRow = offsetRow+1
                offsetCol = offsetCol+1

            return collisionNum

        if value == False:
            #print('-----N------')
            offsetRow, offsetCol = self.__currentLocation(row, col, value)
            while offsetRow != self.width and offsetCol != self.width and offsetCol != -1 :
                try:

                    #printLocation(offsetRow, offsetCol)
                    if self.chessboard[offsetRow][offsetCol] == 1:
                        if offsetRow != row and offsetCol != col:


                            collisionNum += 1


                    offsetRow = offsetRow + 1
                    offsetCol = offsetCol - 1

                except:
                    print("throw ",offsetRow,offsetCol,value)
                    break




            return collisionNum

    def __currentLocation(self,row,col,value):
        offset = 0
        if value is True:

            for i in range(0, self.width-1):

                if row == 0 or col == 0:
                    break
                offset = offset+1
                row = row-1
                col = col-1

        elif value is  False:
            for i in range(0, self.width-1):

                if row == 0 or col == self.width-1:
                    break
                offset =offset+1
                row = row -1
                col = col +1


        return row,col

