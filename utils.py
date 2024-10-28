import json
import os

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