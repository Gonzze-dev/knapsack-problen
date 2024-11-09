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

    # Incluyendo items hasta que la mochila se llene
    while j < len(items) and (totalWeight + items[j].weight) <= W:
        totalWeight += items[j].weight
        profitBound += items[j].profit

        j += 1

    # Si hay espacio para el siguiente item, incluirlo
    if j < len(items):
            profitBound += (W - totalWeight) * items[j].profitPerWeight

    return profitBound

def knapsackBranchAndBound(*args):

    items = args[0][0]
    W = args[0][1]

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