# Challenge_Practicante_MLE

## Despliegue
* Primero, clonar el repositorio o descargarlo y ubicarlo en la instancia que se encargará de ejecutar el servicio
* Segundo, asegurarse de contar con las librerias requeridas para ejecutar el servicio. Estas se encuentran en el archivo **requirements.txt** y para instalarlas utilizar el comando `pip install -r requirements.txt`
* Tercero, abrir una consola de comandos en la carpeta principal del proyecto y ejecutar el comando `uvicorn main:app`
* Finalmente, el servicio estará habilitado y para utilizarlo, llamar a la URL `http://127.0.0.1:8000/probEnfermedadCardiaca` si se trabaja de manera local o `http://{IP_instancia}:8000/probEnfermedadCardiaca` donde se tiene que colocar el ip pública de la instancia donde se deployó el servicio.

## Instrucciones de uso
Realizar un **Post** request a la dirección URL `http://{IP_instancia}:8000/probEnfermedadCardiaca`, donde se tiene que colocar el ip pública de la instancia donde se deployó el servicio o `127.0.0.1` si se trabaja de maner local.

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
