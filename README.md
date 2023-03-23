# Frutas y Verduras

Hola! El juego utliza Open-CV para detectar el rostro, en específico la boca. Cuando se comienza el juego, las futas o verduras (depediendo la elección) caen de la parte superior de la pantalla y el niño debera de "comerlas" abriendo la boca. Además, pueden caer objetos no comestibles.

El juego está dirigido para niños con necesidades educativas especiales. La velocidad lenta de la caida de los objetos permite que el niño pueda nombrar el objeto que esta cayendo y posteriormente "comerla".

## Como instalar
El proyecto se encuentra bajo la versió 3.10.10 de Python.
Sigue los siguientes pasos para poder utilizarla

* instalar la librería customtkinter. Utilizando

```
pip install customtkinter
```
* Crear un entorno vitual en el proyecto.
* Iniciar el entorno virtual e instalar las librerias que se encuentran en el archivo "requirements.txt". Utilizando

```
pip install -r requirements.txt
```

## Como se utiliza

Primero se debe ejecutar el archivo "main.pyw" y abrirá una ventana como la siguiente:

![image](https://user-images.githubusercontent.com/104779576/225750610-497510fe-ea6f-4ffe-8504-2ddaae98b927.png)

donde podremos seleccionar si queremos jugar con frutas o verduras. Despues de seleccionar la opción deseada, el juego comenzará.

 ## NOTAS
El juego aun se encuentra en fase de desarrollo, por lo que la configuración de la camara esta sujeta al equipo en que se utiliza el script. En caso de tener problemas, se debera cambiar el número de camara en "select_camera.py".

Actualmente, la velocidad de la caida de los objetos es por defecto, a una velocidad lenta. 
