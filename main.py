from Item import Item
from knapsackBranchAndBound import knapsackBranchAndBound
from knapsackBrutalForce import knapsackBrutalForce
from knapsackGreedy import knapsackGreedy

from utils import loadData, timer


if __name__ == "__main__":
    path = "C:/Users/54344/Desktop/FACULTAD/knapsack-problen/data"
    data = loadData(path)
    items = [Item(**item) for item in data]

    items.sort() #Es necesario tanto para el greedy como para el branch and bound

    W = 50 #W representa la capacidad de la mochila

    #Brutal Force Method
    #timer(knapsackBrutalForce, items, W)

    #Greedy Method
    #timer(knapsackGreedy, items, W)

    #Branch And Bound Method
    #timer(knapsackBranchAndBound, items, W)