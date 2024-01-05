import requests
import mysql.connector
from evalua_data import evaluacion

from sqlalchemy import create_engine

config = {
        'user': 'root',
        'password': 'bia',
        'host': 'db',
        'port': '3306',
        'database': 'codigos_postales'
    }

def consult_and_store():
    config = {
        'user': 'root',
        'password': 'bia',
        'host': 'db',
        'port': '3306',
        'database': 'codigos_postales'
    }

    try:
        # Establecer conexión con la base de datos
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute(f"SELECT max(id) from maxid ;")
        max_id = cursor.fetchall()
        print('pt1')
        if max_id == [(None,)]:
            ids=0
        else:
            ids=max_id[0][0]

        cursor.execute(f"SELECT  id,latitud, longuitud FROM coordenadas where id > {ids} order by id limit 5;")

        coordenadas = cursor.fetchall()
            
        print('Consulta Exitosa')
            
        ids = max([id for id, _, _ in coordenadas])
        print(ids)
        sql_insert_id = "INSERT INTO maxid (id) VALUES (%s)"
        cursor.execute(sql_insert_id, (ids,))
        connection.commit()

        for  id,lat, lon in coordenadas:
         
            api_url = f"https://api.postcodes.io/postcodes?lat={lat}&lon={lon}"
            response = requests.request("GET", api_url)
            #print(response.status_code)
            
            if response.status_code == 200:
                json_data = response.json()
                if  json_data["result"] is  None:
                    observaciones='La respuesta de la API no contiene informacion. o tiene probles en su CSV'
                    # Sentencia SQL para la inserción
                    sql_insert = "INSERT INTO errores (id_coordenada, latitud, longitud, observaciones) VALUES (%s, %s, %s, %s)"
                    # Valores a insertar
                    valores = (id, lat, lon, observaciones)

                    # Ejecutar la sentencia SQL
                    cursor.execute(sql_insert, valores)

                    connection.commit()
                else:
                    # Convertir la respuesta a formato JSON
                    json_data = response.json()
                    #print('Long: ',len(json_data['result']),  '  IDENTIFICADOR:  '   ,id)
                    json_carga = evaluacion(json_data['result'])
                    
                    ## Identificador 
                    json_carga['fk_id']=id

                    # Insertar los datos procesados en la base de dato
                    
                    cursor = connection.cursor()

                    nombre_tabla = 'codigos_postales'
                    engine = create_engine('mysql+mysqlconnector://root:bia@0.0.0.0:33060/codigos_postales')

                    json_carga.to_sql(nombre_tabla,if_exists='append', index=False,con=engine)

                    engine = create_engine('mysql+mysqlconnector://usuario:contraseña@localhost/nombre_basedatos')


                    connection.commit()
                
            else: 
                print('Error al obtener datos de la API') 

        cursor.close()
        connection.close()
        
    except Exception as e:
        print(e)
    return ids
