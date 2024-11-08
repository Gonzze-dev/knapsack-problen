from Item import Item
from knapsackBranchAndBound import knapsackBranchAndBoundMain
from knapsackBrutalForce import brutalForce
from knapsackGreedy import knapsackGreedyMain
from nother import nother
from utils import loadData


if __name__ == "__main__":
    path = "C:/Users/54344/Desktop/FACULTAD/knapsack-problen/data"
    data = loadData(path)
    items = [Item(**item) for item in data]

    items.sort() #Es necesario tanto para el greedy como para el branch and bound

    W = 50 #W representa la capacidad de la mochila

    #brutalForce(items=items, W=W)
    #knapsackBranchAndBoundMain(items=items, W=W)
    
    #knapsackGreedyMain(items=items, W=W)