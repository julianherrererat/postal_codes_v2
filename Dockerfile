### crea un ambiente python
FROM python:3.12


## Copia los archivos

COPY . /app


### instala todo lo que se necesita
RUN pip install -r /app/requirements.txt

### Corre la app
CMD [ "python", "/app/src/app.py" ]