from Item import Item
from knapsackBranchAndBound import knapsackBranchAndBoundMain
from knapsackBrutalForce import brutalForce
from knapsackGreedy import knapsackGreedyMain
from utils import loadData


if __name__ == "__main__":
    path = "C:/Users/54344/Desktop/knaspack-problem/data"
    data = loadData(path)
    items = [Item(**item) for item in data]

    W = 50 #W representa la capacidad de la mochila
    
    #brutalForce(items=items, W=W)
    #knapsackBranchAndBoundMain(items=items, W=W)
    #knapsackGreedyMain(items=items, W=W)