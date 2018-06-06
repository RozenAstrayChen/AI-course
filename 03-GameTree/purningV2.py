import minimax as m

root = 0
max = True
min = False

class PurningV2(m.MiniMax):
    def __init__(self,bits,depth):
        m.MiniMax.__init__(self,bits,depth)
        self.purningLeaf = []
        self.beta = 1000
        self.alpha = -1000
        self.pruned = 0

    def testData(self):


        self.bits = 2
        self.depth = 4
        self.tree = [[[[-5,36],[-23,-21]],[[-47,49],[-1,2]]],[[[31,-33],[-18,-37]],[[32,-41],[35,-46]]]]
        self.scanTree = []

    def buildTree(self,depth,tempList):
        if depth is 1:
            return tempList
        '''
        data = []
        for i in  range(0,bits):
            data.append(rawData[i])
            rawData.pop(i)
        '''
        tempList.append([])



        self.buildTree(depth-1,tempList[0])

        return tempList


    def insertTree(self,rawData,bits,depth,frameList):
        for frame in frameList:
            print(frame)
            if type(frame) is list:
                print(frame)
                self.insertTree(rawData,bits,depth,frame)
            else:
                for i in range(0,bits):
                    frame.append(rawData[i])
                    print(frame)

    def buildTreeV2(self,rawData,bits,depth):

        frame = []
        for i in range(0,int(pow(bits,depth)/bits)):
            arr = []
            for j in range(0,bits):
                arr.append(rawData[0])
                rawData.pop(0)


            frame.append(arr)
        print(frame)
        return  frame

    def buildDepth(self,listArray,bits,depth):


        ArrayList = []
        treeNode = int(pow(bits,depth)/bits)
        if int(pow(bits,depth)/bits) == 1:
            return ArrayList
        treeBranch = int(pow(bits,depth+1)/bits /treeNode)


        for j in range (0,int(pow(bits,depth)/bits)):
            temp = []
            for i in range(0,treeBranch):

                temp.append(listArray[0])
                listArray.pop(0)



            ArrayList.append(temp)

        self.buildDepth(ArrayList,bits,depth-1)

        self.tree =  ArrayList


    def startPurning(self):
        #self.testData()
        (alpha, beta) = self.children(self.tree, 0, self.alpha, self.beta)

        print("(alpha, beta): ", alpha, beta)
        print("Result: ", self.tree)
        print("Times pruned: ", self.pruned)
        print("Pruned leaf : ",self.purningLeaf)

    def children(self,branch,depth,alpha,beta):
        for child in branch:

            # It is a node which receive leaf alpha-beta
            if type(child) is list:
                (nalpha,nbeta) = self.children(child,depth+1,alpha,beta)

                #recursive to max
                if self.judgeMinMax(depth) is max:
                    alpha = nbeta if nbeta > alpha else alpha

                elif self.judgeMinMax(depth) is min:
                    beta = nalpha if nalpha < beta else beta


            # It is a leaf which judges current alpha and beta
            else:

                print("alpha = ", alpha, " ; beta = ", beta,"\ninput data is ",child,"\n")
                # purning
                if alpha >= beta:
                    print("Occur pruning !")
                    self.pruned += 1
                    self.purningLeaf.append(child)

                elif self.judgeMinMax(depth) is max and alpha < child:
                    alpha = child
                elif self.judgeMinMax(depth) is min and beta > child:
                    beta = child

        if depth == root:
            tree = alpha if root == 0 else beta
        return (alpha, beta)

