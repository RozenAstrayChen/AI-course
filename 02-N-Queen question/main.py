
import algorithm as h
import output
from datetime import datetime

'''[Summary]
this is a question which is slove N-queen question by Hill-Climbing
'''

if __name__ == "__main__":

    num = input('pls in put queen number : ')
    print(str(datetime.now()))
    HC = h.Algorithm(int(num))
    times = HC.hillSearch()
    print('do ...',times,' times')
    print(str(datetime.now()))
    output.oupput2Txt(HC.pieceNode)
    print('--------------Another-------------')
    #SA = h.Algorithm(10)
    #times = SA.simulatedAnnleaing()
    #print('do ...', times, ' times')


