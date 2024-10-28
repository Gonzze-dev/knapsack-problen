import json
import random

#Este programa genera datos aleatorios para usar de prueba en el KP knapsack problem
def generateRandomData(nItems, x, y, k, n):
    data = []
    for i in range(nItems):
        item = {
            "id": i + 1,
            "weight": random.randint(x, y),
            "profit": random.randint(k, n)
        }
        data.append(item)
    
    with open("datos.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print(f"{nItems} ítems generados y guardados en 'data.json'.")


nItems = 10000
x, y = 1, 100 
k, n = 1, 150

generateRandomData(nItems, x, y, k, n)