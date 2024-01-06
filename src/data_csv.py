##################################################
#
# Esta funcnion descarga el archivo desde google drive 
#       y luego lo carga a la base de datos definida desde el servicio
#
##################################################

import gdown
import pandas as pd


# Funcion para descargar el archivo en drive con la libreria gdonw

def descargar_csv():
    id='1JzGG10Z0Lkg3WDXfiB82wWo0a6unRjVM'
    print('Inicia la descarga de la información:  ....')
    url = f'https://drive.google.com/uc?id={id}'
    output = 'coordenadas.csv'  
    try:
        gdown.download(url, output, quiet=False)
    except:
        print('El Archivo no existe')

def lee_datos():
    datos=pd.read_csv('coordenadas.csv')
    return datos


