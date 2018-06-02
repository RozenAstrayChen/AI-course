import math
import random
"""
The minmax generater which generating minmax tree.
then ouput three params:
1. Number of bits
2. Deep
3. tree node value
"""

class Treegenerater(object):
    # the deep in not include root
    def __init__(self,bits,depth):
        self.bits = bits
        self.depth = depth
        self.leafNum = int(math.pow(bits,depth))
        self.leafList = []
        self.newValue()

    def newValue(self):
        tempLeaf = []
        for i in range(0, self.leafNum):
            tempLeaf.append(random.randint(0,100))

        self.leafList = tempLeaf
    def getDepth(self):
        return self.depth
    def getNodeNum(self):
        return self.leafNum

    def getLeafList(self):
        return self.leafList




