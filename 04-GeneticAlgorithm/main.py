
import genetic

boardSize = 10
populationSize = 10
probability = 30


if __name__ == "__main__":

    question = genetic.Genetic(boardSize)
    question.startGA(populationSize,probability)






