import time
from itertools import combinations

def calcBestCombination(W, items):
    #r representa el tamaño de las combinaciones
    bestProfit = 0
    bestComb = []
    
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            totalWeight = sum(item.weight for item in combo)
            totalProfit = sum(item.profit for item in combo)

            if totalWeight <= W and totalProfit > bestProfit:
                bestProfit = totalProfit
                bestComb = combo

    return bestComb, bestProfit


def brutalForce (items, W):
    print("\nknapsack Brutal Force\n")
    
    start = time.time()
    bestComb, bestProfit = calcBestCombination(W, items)
    end = time.time() 

    totalTime = start - end

    print("Mejor combinación de items:")
    for item in bestComb:
        print(item)
    print(f"Beneficio total: {bestProfit}")

    print(f"Tiempo de ejecucion: {totalTime:.6f}s")
