import time

def knapsackGreedy(items, W):
    totalProfit = 0
    weightAccumulated = 0
    bestItems = []

    for item in items:
        if weightAccumulated + item.weight <= W:
            # Si el item completo cabe, incluirlo
            weightAccumulated += item.weight
            totalProfit += item.profit
            bestItems.append(item)

    return totalProfit, bestItems


def knapsackGreedyMain(items, W):
    print("\nknapsack Greedy\n")
    
    start = time.time()
    maxProfit, bestItems = knapsackGreedy(items, W)
    end = time.time()

    totalTime = start - end

    print("Máximo beneficio:", maxProfit)
    print("Mejor combinación de items:")
    for item in bestItems:
        print(item)

    print(f"Tiempo de ejecucion: {totalTime:.16f}s")