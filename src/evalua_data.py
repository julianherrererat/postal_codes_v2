import pandas as pd

def evaluacion(json_evlua):
    # Evalua cual es la mas cercana para cargar o las carga todas
    menor_distancia = float('inf')
    registros_menor_distancia = []

    for registro in json_evlua:
        distancia_actual = registro["distance"]
        if distancia_actual < menor_distancia:
            menor_distancia = distancia_actual
            registros_menor_distancia = [registro]
        elif distancia_actual == menor_distancia:
            registros_menor_distancia.append(registro)
            # Iterar sobre los registros y ejecutar una sentencia SQL para insertarlos en la tabla

    df=pd.json_normalize(registros_menor_distancia,sep='_' )        
    registros_menor_distancia=df    #.to_json(orient='records')
    #########print(df.dtypes)
    return(registros_menor_distancia)
            

