
def oupput2Txt(array):
    f = open('judgement.txt','w+')
    for i in range (0,len(array)):
        f.write(str(array[i]))