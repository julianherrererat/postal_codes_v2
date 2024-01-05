import mysql.connector


def insertar_datos(datos):
    config = {
        'user': 'root',
        'password': 'bia',
        'host': 'db',
        'port': '3306',
        'database': 'codigos_postales'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()


    tabla = 'coordenadas'

    for index, row in datos.iterrows():
        longuitud = row['lon']
        latitud = row['lat']

        query = f"INSERT INTO {tabla} (latitud, longuitud) VALUES (%s, %s)"
        cursor.execute(query, (latitud, longuitud))

    connection.commit()
    cursor.close()
