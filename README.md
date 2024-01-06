# POSTAL CODES UK

Con el fin de dar solución a la prueba propuesta, el desarrollo de la misma se centro en establecer un Producto Mínimo Viable trabajando con dos servicios, atendiendo los requerimientos de la Prueba. Para tal fin, se utilizó el framework de Python Flask, combinado con Mysql, los cuales fueron orquestados por un Docker y Docker-compose. Resulta relevante indicar que el proceso de Docker-compose tiene una duración aproximada de 3.5 minutos. 

Igualmente, para el desarrollo de la prueba se utilizó como flujo para el manejo del repositorio GIT-FLOW, por medio del cual se crearón las siguientes ramas: 

- main
- Develop
- Features

Ahora bien, dentro de la base de datos se encuentran contenidas cuatro tablas, las cuales se referencian a continuación con sus respectivas funciones:

- maxid : Se almacena el ultimo Id de las coordenadas para la siguiente ejecucion, esto con el fin de hacer más eficiente el proceso.

- coordenadas : Contiene las coordenadas el archivo CSV, ademas se creo un *ID* con el que se pueden relacionar las tablas. 

- errores : En esta tabla se guardan las coordenadas y los id que no se pudieron procesar en el API de codigos postales

- codigos_posteles : Contiene toda la informacion que se descarga desde la API codigos postales y se crea un campo adicional *(fk_id)* para relacionarla con la tabla coordenadas.

---
---

## Servicios
En atención a los requerimientos de la Prueba respecto a los servicios solicitados, se informa que los servicios creados fueron los siguientes: 

### Servicio 1

El primer servicio utiliza *data_csv* y *carga_bd*, lo cual permite descargar el archivo, procesarlo y finalmente cargarlo en la base de datos establecida; nuevamente se reitera que dicho proceso tiene una duración aproximada de 3.5 minutos, el cual podría optimizarse utilizando en primera instancia redis y posteriormente Mysql. 

Finalmente, se agregaron ID para relacionar las tablas con el proposito de que al final se muestre el total de los datos que fueron efectivamente cargados. 

### Servicio 2

El segundo servicio utiliza *api_pos_code.py* *evalua_data.py* y *respuestas.py*, los cuales se ejecutan de manera concurrente con los ID's para indexar las consultas y evaluar los códigos postales más cercanos a la coordenada, lo cual para algunos casos corresponde a solo un código postal, pero en otros pueden ser más. 

Solo se procesan 5 coordeadas, las cuales incrementan en cada refresco de página para hacer el proceso óptimo, lo cual tiene una duración aproximada de 5 segundos.

Como resultado, al final se tiene: 

- Errores de archivo
- Resultados de la consulta (Solo muestra algunos datos, pero en la base de datos se encuentra consolidada la información)
- Último ID procesado 

---

## Cómo Desplegar con Docker Compose

### Requisitos

- Docker instalado
- Docker Compose instalado

### Pasos para Desplegar

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/julianherrererat/postal_codes_v2.git
    ```

2. Navegar al directorio del proyecto:

    ```bash
    cd repositorio
    ```

3. Ejecutar el comando Docker Compose para iniciar los servicios:

    ```bash
    docker-compose up -d
    ```

6. Accede a los servicios en el navegador o a través de las rutas proporcionadas por Docker Compose.

    ```
   localhost:9000
    ```

---
