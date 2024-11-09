import json
import os
from time import time

def loadData(path):
    '''
        Pasar el path de la carpeta donde se encunetran los datos
        ### Ejemplo
        path = "C:/Users/54344/Desktop/knaspack-problem/data"

        loadData(path)

        Return
        [
            {
                "id": 1,
                "weight": 10,
                "profit": 50
            },
            ...
        ]

        or

        None
    '''
    
    jsonFile = [f for f in os.listdir(path) if f.endswith('.json')]

    if not jsonFile:
        print("No se encontraron archivos JSON en la carpeta.")

    else:

        print("Archivos JSON disponibles:")
        for i, file in enumerate(jsonFile):
            print(f"{i + 1}. {file}")

        seleccion = int(input("Selecciona el número del archivo que quieres cargar: ")) - 1

        if 0 <= seleccion < len(jsonFile):
            fileSelected = jsonFile[seleccion]
            pathFile = os.path.join(path, fileSelected)

            with open(pathFile, "r") as file:
                data = json.load(file)

            return data
        else:
            print("Selección no válida.")

            return None
        
def timer(function, *args):
    print(f"\n{function.__name__}\n")
    
    start = time()
    maxProfit, bestItems = function(args)
    end = time()

    totalTime = start - end

    print("Máximo beneficio:", maxProfit)
    print("Mejor combinación de items:")
    for item in bestItems:
        print(item)

    print(f"Tiempo de ejecucion: {totalTime:.16f}s")