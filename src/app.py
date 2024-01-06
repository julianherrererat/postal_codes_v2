from flask import Flask, jsonify ,abort,make_response
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
    response = make_response(
        jsonify({'SERVICIO DE CARGA Y DESCARGA TIEMPO ** 3 MINUTOS **': 'http://localhost:9000/csv',
                 'SERVICIO DE CONSULTA DEL API Y CARGA DE INFORMACION': 'http://localhost:9000/receive-data'})
    )
    response.headers['Custom-Title'] = 'Página de Inicio'
    return response

###### SERVICIO 1: descarga el archivo y lo carga a la base de datos

@app.route('/csv', methods=['GET'] )
def micro1():
    datos_csv= descargar_csv()
    pt1 = lee_datos()
    pt2= insertar_datos(pt1)

    return jsonify({'cantidad': len(pt1) })


##### SERVICIO 2: hace peticion del servio y luego cruza toda la informacion

@app.route('/receive-data', methods=['GET'])
def micro2():
    datos_csv= consult_and_store()
    if not datos_csv:
        return jsonify({'error': 'Por favor, ingrese primero a /csv para descargar los datos'})
    else:
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
 

##### PUERTO DE SALIDA DE LA APLIACION

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True )