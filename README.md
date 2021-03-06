# ROS_listener_talker_turtle
Proyecto en el que se usa ROS melodic en ubuntu 18.04, para poder hacer un ejercicio básico de comunicar dos nodos, además de controlar la tortuga de ROS, todo por medio de Python.
Como en este caso si bajas todo el repositirio y tratas de compilarlo este no va compilar, lo que debes hacer es crear una carpeta con el nombre de tu work space y dentro de esa carpeta crear otra llamada src.
- Al hacer esto, a la altura de la carpeta de tu workspace ingresa el sigueinte comando
```
catkin_make
```
- Después haber guardado el workspace y compilarlo, recuerda cada vez que abras una nueva terminal o pestaña de esta misma ingresar este comando para actulizar las variables del entorno de tu workspace, siempre a la altura de la carpeta de tu workspace:
```
source devel/setup.bash
```
- Luego en otra carpeta as el git clone del repositorio, luego ve a la dirección:
```
/ROS_listener_talker_turtle/src/
```
- Copia las carpetas o paquetes y pégalos en la capeta src del workspace que creaste al inicio.
- Después de copiar, ve a la altura de la carpeta de tu workspace en ingresa:
```
catkin_make
```
Para poder compilar.
- Recueda que cada vez que hagas un cambio importante como compilar o agregar paquetes ingresa en cada una de tus terminales:
```
source devel/setup.bash
```
- Para poder correr el proyecto en la terminal inicia el roscore.
```
roscore
```
## Talker - Listener
- Localidad de los archivos talker y listener en el proyecto
```
/nombre_de_tu_ws/src/talker_listener/src/
/nombre_de_tu_ws/src/talker_listener/src/talker.py
/nombre_de_tu_ws/src/talker_listener/src/listener.py
```
- Para poder corre el talker y el listener habre otra pestaña de la terminal e ingresa:
```
rosrun talker_listener talker
```
- Luego en otra pestaña ingresa:
```
rosrun talker_listener listener
```
- Si todo esta corriendo bien debes ver mensaje de *Hello World* en la pestaña donde corriste el listener.
- Para verificar el funcionamiento al ingresar el sigueinte comando en una nueva pestaña de la terminal:
```
rqt_graph
```
Se debe ver lo siguiente:
![RQT](rqt.png)
## Trutle espiral
- Localidad del archivo para poder mover la tortuga
```
/nombre_de_tu_ws/src/turtle_mov/src/turtle_mov.py
```

- Para poder correr la tortuga en espiral, ingresa el siguiente comando en una nueva terminal:
```
rosrun turtlesim turtlesim_node
```
- Al correr esto se debería ver algo como esto:
![RQT](turtle.png)
- Después en una nueva terminal ingresa el siguiEnte comando para poder correr el código que hicimos:
```
rosrun turtle_mov turtle_mov.py
```
- Al correr esto la tortuga al terminar el programa debe tener este movimiento:
![RQT](turtle_mov.png)
- Para poder a poner a la tortuga en su posición inicial ingresa en una nueva terminal:
```
rosservice call /reset
```
## Nota importante:
Cada vez que abras un terminal ingresa el siguiente comando a la altura de la carpeta de tu worspace de ROS:
```
source devel/setup.bash
```
