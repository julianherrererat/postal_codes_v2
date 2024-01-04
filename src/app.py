from flask import Flask, jsonify
import json



app = Flask(__name__)

## Esta es la pagina de Inicio
@app.route('/',methods = ['GET'] )
def ping():
    return jsonify( {'Response': 'TEST PAGINIA'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True )