
import genetic

boardSize = 8
populationSize = 10
probability = 10


if __name__ == "__main__":

    question = genetic.Genetic(boardSize)
    question.startGA(populationSize,probability)






