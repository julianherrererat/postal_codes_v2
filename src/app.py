from flask import Flask, jsonify
import json
import mysql.connector
from data_csv import descargar_csv, lee_datos
from carga_bd import insertar_datos
from api_pos_code import consult_and_store
from respuestas import resultado, resultado_data

app = Flask(__name__)

## Esta es la pagina de Inicio
@app.route('/',methods = ['GET'] )
def ping():
<<<<<<< HEAD
    return jsonify( {'Response': 'TEST PAGINIA'})
=======
    return jsonify( {'SERVICIO DE CARGA Y DESCARGA TIEMPO **3 mintos**': 'http://localhost:9000/csv',
                     'SERVICIO DE CONSULTA DEL API Y CARGA DE INFORMACION': 'http://localhost:9000/receive-data'})
>>>>>>> 51b1849 (Completado, solo falta pulir)

###### descarga el archivo y lo carga a la base de datos

@app.route('/csv', methods=['GET'] )
def micro1():
    datos_csv= descargar_csv()
    pt1 = lee_datos()
    pt2= insertar_datos(pt1)
<<<<<<< HEAD
=======

>>>>>>> 51b1849 (Completado, solo falta pulir)
    return jsonify({'cantidad': len(pt1) })


##### hace peticion del servio y luego cruza toda la informacion

@app.route('/receive-data', methods=['GET'])
def micro2():
    datos_csv= consult_and_store()
    datos_totales = json.loads(resultado_data())
    datos_csv_json= jsonify({'ultimo_id': datos_csv})
    rta = json.loads(resultado())

    return jsonify({'ULTIMO ID PROCESADO': datos_csv_json.json , 'DATOS ERROREOS': rta, 'RESULTADOS CONSULTA': datos_totales })



### prueba de conexxion

@app.route('/test',methods= ['GET'])
def write_to_employee_data():
    config = {
        'user': 'root',
        'password': 'bia',
        'host': 'db',
        'port': '3306',
        'database': 'codigos_postales'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute( "SELECT * FROM codigos_postales.coordenadas;")
    resultado = cursor.fetchall()
    cursor.close()
    return jsonify({'test': str(resultado)})
 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True )