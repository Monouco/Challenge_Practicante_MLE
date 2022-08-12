# Challenge_Practicante_MLE

## Despliegue
### Para una instancia o despliegue local
* Primero, clonar el repositorio o descargarlo y ubicarlo en la instancia que se encargará de ejecutar el servicio
* Segundo, asegurarse de contar con las librerias requeridas para ejecutar el servicio. Estas se encuentran en el archivo **requirements.txt** y para instalarlas utilizar el comando `pip install -r requirements.txt`
* Tercero, abrir una consola de comandos en la carpeta principal del proyecto y ejecutar el comando `uvicorn main:app`
* Finalmente, el servicio estará habilitado y para utilizarlo, llamar a la URL `http://127.0.0.1:8000/probEnfermedadCardiaca` si se trabaja de manera local o `http://{IP_instancia}:8000/probEnfermedadCardiaca` donde se tiene que colocar el ip pública de la instancia donde se deployó el servicio.

### Para el despliegue en HEROKU
* Crear una aplicación y agregarla a un pipeline en staging o production
* En la sección de **Deployment method** seleccionar la opcion de github y conectarla con este repositorio.
* En la sección de **Automatic deploys** seleccionar la rama de **dev** si se trabaja en staging o **main** si se encuentra en producción. Además, habilitar la opción de *Wait for CI to pass before deploy* y de despliegue automático.
* La información del CI se encuentra en el archivo `python-app.yml`.
* En el archivo `Procfile` esta la instrucción `web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app` que permite que el servicio pueda desplegarse en HEROKU.
* Finalmente, en la sección de **Manual deploy** desplegar la rama correspondiente a donde se esta trabajando. Esto solo es necesario la primera vez, ya que despues será deployado automáticamente por cómo se configuró anteriormente.
#### APPS en HEROKU
Se puede llamar a los servicios deployados:
* Staging: http://challenge-rimac-mle-dev.herokuapp.com/probEnfermedadCardiaca
* Production: http://challenge-rimac-mle.herokuapp.com/probEnfermedadCardiaca

## Instrucciones de uso
Realizar un **Post** request a la dirección URL `http://{IP_instancia}:8000/probEnfermedadCardiaca`, donde se tiene que colocar el ip pública de la instancia donde se deployó el servicio o `127.0.0.1` si se trabaja de maner local. O directamente a las siguientes URLs:
* Staging: http://challenge-rimac-mle-dev.herokuapp.com/probEnfermedadCardiaca
* Production: http://challenge-rimac-mle.herokuapp.com/probEnfermedadCardiaca

### Input
El servicio recibe los siguientes parámetros
```
{
  "age": 41,
  "sex": "M",
  "chestPainType": "ATA",
  "restingBP": 140,
  "cholesterol": 289,
  "fastingBS": 0,
  "restingECG": "Normal",
  "maxHR": 123,
  "exerciseAngina": "N",
  "oldpeak": 1.5,
  "sTSlope": "Flat"
}
```
estos cuentan con los siguientes tipos de datos
```
{
"age": integer,
"sex": "string",
"chestPainType": "string",
"restingBP": integer,
"cholesterol": integer,
"fastingBS": integer,
"restingECG": "string",
"maxHR": integer,
"exerciseAngina": "string",
"oldpeak": number,
"sTSlope": "string"
}
```
### Output
La respuesta del servicio es la siguiente
```
{
  "prob": 0.9084
}
```
donde la probabilidad es valor entre 0 y 1, limitado a 4 decimales.
