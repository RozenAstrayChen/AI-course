import minimax as m

"""
beta <= postive unlimted
alpha >= negative unlimated

        alpha----------------->
        <--------------------->
        <------------------beta
            
Step by step:
1. bfs,search and choice beta or alpha
2. if alpha and beta havn't "set" like this
                       alpha-->
        <--------------------->
        <-------beta
    you don't sperate node and ignore it
"""
class Purning(m.MiniMax):
    def __init__(self,bits,depth):
        m.MiniMax.__init__(self,bits,depth)
        self.purningLeaf = []
        self.beta = 1000
        self.alpha = -1000

    def testData(self):
        self.bits = 2
        self.depth =4
        self.minMaxTree[0] = [-5,36,-23,-21,-47,49,-1,2,31,-33,-18,-37,32,-41,35,-46]

    def purningStart(self):
        nbeta = self.beta
        nalpha = self.alpha
        beta = self.beta
        alpha = self.alpha

        currentDepth = 3
        if self.judgeMinMax(currentDepth):
            print("do max")
        else:
            print("do min")

        for i in range (0,len(self.minMaxTree[0])):
            depth = self.judgeMinMax(currentDepth)

            # Judge it can be purned or not
            if alpha > beta:
                print("This node will be purning! node value is : ", self.minMaxTree[0][i])
                self.purningLeaf.append(self.minMaxTree[0][i])
            else:



                alpha,beta = self.purningAlgorithm(self.minMaxTree[0][i],
                                                   alpha,
                                                   beta,depth)
                print("alpha = ",alpha," beta = ",beta)




            if (i+1) % (self.bits*self.bits)  == 0:

                alpha,beta = self.swaping(alpha,beta,depth-1)

            elif (i+1) % self.bits  == 0:
                print(i+1,self.bits,(i+1) % self.bits)
                alpha,beta = self.swaping(alpha,beta,depth)
                #alpha = self.alpha
                #beta = self.beta




        print("all of purning",self.purningLeaf)



    def purningAlgorithm(self,node,alpha,beta,depth):

        if depth:
            if node > beta :
                beta = node
        else:
            if node < beta:
                beta = node



        return alpha,beta

    def swaping(self,alpha,beta,NextminiORmax):

        if NextminiORmax:
            print("swapping max")
            #max
            if alpha > beta:
                beta = alpha
            alpha = self.alpha
        else:
            print("swapping min")
            #min
            if alpha < beta:
                alpha = beta
            beta = self.beta

        print("after swaping ,alpha = ", alpha, " beta = ", beta)
        return alpha,beta




