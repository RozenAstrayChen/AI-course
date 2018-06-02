import tree_create as t

class MiniMax(t.Treegenerater):
    """
    when object init that will create a double list which will store tree data
    """
    def __init__(self,bits,depth):
        self.minMaxTree = [[]]
        self.bits = bits
        self.depth = depth
        t.Treegenerater.__init__(self,bits,depth)
        "store last depth node"
        self.minMaxTree[0].extend(self.getLeafList())

    """
    True : max
    False: min
    """
    def judgeMinMax(self,depth):
        if depth % 2 == 1:
            return False
        elif depth % 2 == 0:
            return True
    """
    every floor  node number is (bits^currentdepth)
    it function is count what is the root
    """
    def minMax_algorithm(self,peviousDepth,peviousNodeList):

        currentList = []

        currentDepth = peviousDepth-1
        miniMaxFlag = self.judgeMinMax(currentDepth)


        # Do Max search

        for i in range (0,len(peviousNodeList),self.bits):
            tempList = []

            for j in range (0,self.bits):
                tempList.append(peviousNodeList[i+j])

            #Do mini max
            if miniMaxFlag == True:
                miniMaxValue = max(tempList)
            elif miniMaxFlag == False:
                miniMaxValue = min(tempList)
            currentList.append(miniMaxValue)


        return currentList








