import minimax as a


if __name__ == '__main__':
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

