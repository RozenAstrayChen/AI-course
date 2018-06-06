import minimax as a
import purning
import purningV2

test = [-2,-81,-10,-62,29,-31,-52,-39,-69,23,-45,-35,1,-20,69,-62,32,-27,90,21,-94,-93,-61,11,50,-1,-56]
bits = 3
depth = 3
#test = [-5,36,-23,-21,-47,49,-1,2]


if __name__ == '__main__':
    """
    myTree = a.MiniMax(3,2)
    print("nodeNum = ",myTree.getNodeNum())

    
    print(myTree.minMaxTree[0])
    
    for i in range(0,myTree.getDepth()):
        depth = myTree.getDepth()-i

        myTree.minMaxTree.append(myTree.minMax_algorithm(depth,myTree.minMaxTree[i]))

        print(myTree.minMaxTree[i+1],end="  -> ")
        if myTree.judgeMinMax(depth-1):
            print("max")
        else:
            print("min")
    """
    """
    p = purning.Purning(2,3)
    p.testData()
    print(p.minMaxTree[0])
    p.purningStart()
    """
    p = purningV2.PurningV2(bits,depth)
    #p.testData()

    #frame = p.buildTree(4,[])
    #p.insertTree(test,2,4,frame)
    set = p.buildTreeV2(test,p.bits,p.depth)
    p.buildDepth(set,bits,p.depth-1)
    p.startPurning()