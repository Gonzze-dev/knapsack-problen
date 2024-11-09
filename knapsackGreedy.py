def knapsackGreedy(*args):
    items = args[0][0]
    W = args[0][1]

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