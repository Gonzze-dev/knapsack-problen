import time

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level      # Nivel de la hoja (nodo) en el árbol
        self.profit = profit    # Beneficio acumulado
        self.weight = weight    # Peso acumulado
        self.bound = bound      # Cota superior (Upper bound)

def calculateBound(node, items, W):
    if node.weight >= W:
        return 0

    profitBound = node.profit
    j = node.level + 1
    totalWeight = node.weight

    # Incluyendo items hasta que la capacidad se alcance
    while j < len(items) and totalWeight + items[j].weight <= W:
        totalWeight += items[j].weight
        profitBound += items[j].profit

        j += 1

    # Si hay espacio para el siguiente item, incluir una fracción del mismo  
    if j < len(items):
            profitBound += (W - totalWeight) * items[j].valuePerWeight

    return profitBound

def knapsackBranchAndBound(items, W):
    # Ordenar items por valor/peso
    items.sort(reverse=True)

    # Cola para almacenar los nodos
    queue = []

    # Iniciar el primer nodo
    # El nodo raiz siempre su peso vale 0, al igual que sus demas valores, 
    # expeto el nivel que es negativo

    root = Node(-1, 0, 0, 0)

    root.bound = calculateBound(root, items, W)
    queue.append(root)

    maxProfit = 0
    bestItems = []

    while queue:
        # Tomar el nodo de mayor cota superior
        currentNode = queue.pop(0)

        # Si el nodo actual puede llevar a una solución mejor
        if currentNode.bound > maxProfit:

            # Hijo derecho (incluir el item actual)
            nextLevel = currentNode.level + 1

            if nextLevel < len(items):

                # Nodo que incluye el item
                includedNode = Node(
                    nextLevel,
                    currentNode.profit + items[nextLevel].profit,
                    currentNode.weight + items[nextLevel].weight,
                    0
                )

                # Calcular la cota superior para el nodo incluido (upper bound)
                if includedNode.weight <= W:
                    includedNode.bound = calculateBound(includedNode, items, W)
                    if includedNode.profit > maxProfit:
                        maxProfit = includedNode.profit
                        bestItems = [items[i] for i in range(includedNode.level + 1)]

                if includedNode.bound > maxProfit:
                    queue.append(includedNode)

            # Hijo izquierdo (excluye el item actual)
            excludedNode = Node(
                nextLevel,
                currentNode.profit,
                currentNode.weight,
                0
            )

            excludedNode.bound = calculateBound(excludedNode, items, W)

            if excludedNode.bound > maxProfit:
                queue.append(excludedNode)

    return maxProfit, bestItems

def knapsackBranchAndBoundMain(items, W):
    print("\nknapsack Branch And Bound\n")

    start = time.time()
    maxProfit, bestItems = knapsackBranchAndBound(items, W)
    end = time.time()

    totalTime = start - end

    print("Máximo beneficio:", maxProfit)
    print("Mejor combinación de items:")
    for item in bestItems:
        print(item)

    print(f"Tiempo de ejecucion: {totalTime:.16f}s")