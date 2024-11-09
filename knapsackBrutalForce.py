from itertools import combinations

def knapsackBrutalForce(*args):
    items = args[0][0]
    W = args[0][1]

    #r representa el tamaño de las combinaciones
    maxProfit = 0
    bestItems = []
    
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            totalWeight = sum(item.weight for item in combo)
            totalProfit = sum(item.profit for item in combo)

            if (totalWeight <= W) and (totalProfit > maxProfit):
                maxProfit = totalProfit
                bestItems = combo

    return maxProfit, bestItems