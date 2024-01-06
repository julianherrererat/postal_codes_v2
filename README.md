# POSTAL CODES UK

Dentro del proyecto se trabajo con dos servicios, de acuerdo con los requerimientos de la prueba, para ello se uso el framework de python Flask en combinacion con Mysql y todo orquestado por un Docker y Docker-compose. 

Para la prueba se tuvo en cuenta trabajar con GIT-FLOW donde se crearon 3 ramas

- main
- Develop
- Features

Dentro de la base de datos se crearon 4 tablas las cuales son: 
- maxid : Se almacena el ultimo Id de las coordenadas para la siguiente ejecucion, esto con el fin de hacer más eficiente el proceso.
- coordenadas : Contiene las coordenadas el archivo CSV, ademas se creo un *ID* con el que se pueden relacionar las tablas. 
- errores : en esta tabla se guardan las coordenadas y los id que no se pudieron procesar en el API de codigos postales
- codigos_posteles : Esta tabla contiene toda la informacion que se descarga desde la API codigos postales y se crea un campo adicional *(fk_id)* para relacionarla con la tabla coordenadas.

---

## Servicios

### Servicio 1

Breve descripción o contexto sobre el primer servicio.

### Servicio 2

Breve descripción o contexto sobre el segundo servicio.

---

## Cómo Desplegar con Docker Compose

### Requisitos

- Docker instalado
- Docker Compose instalado

### Pasos para Desplegar

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd tu_repositorio
    ```

3. Copia el archivo de configuración de Docker Compose (docker-compose.yml):

    ```bash
    cp ejemplo.docker-compose.yml docker-compose.yml
    ```

4. Abre el archivo `docker-compose.yml` en un editor de texto y ajusta la configuración según sea necesario.

5. Ejecuta el comando Docker Compose para iniciar los servicios:

    ```bash
    docker-compose up -d
    ```

6. Accede a los servicios en tu navegador o a través de las rutas proporcionadas por Docker Compose.

---

## Contacto

Opcionalmente, puedes incluir información de contacto como tu dirección de correo electrónico, redes sociales, etc., para que otros puedan ponerse en contacto contigo con preguntas o contribuciones.
