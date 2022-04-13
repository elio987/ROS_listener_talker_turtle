#!/usr/bin/env python
#Autor: Leonardo Gracida Munoz
"""Codigo que usa ROS para poder publicar en el tpico de velocidades de la rotrtuga para moverla en forma de espiral una dsitancia determinada"""
import rospy
from geometry_msgs.msg import Twist
#inicializamos el nodo
rospy.init_node("turtle_mov")
#Creamos el publisher
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)
#Declaramos que vamos a mandar 20 mensajes por segundo
rate = rospy.Rate(20)
#Imiciamos el menasje a mandar de tipo Twist
turtle_cmd = Twist()
def mov_lin():
    #obtenemos el tiempo inicial
    t0 = rospy.get_rostime().to_sec()
    #Declaramos las velocidade lineales y angulares iniciales.
    turtle_cmd.linear.x = 1.25
    turtle_cmd.angular.z = 0.5
    #Inicimos en esta distancia
    dis = 0
    while dis < 30.0:
        #Obtenemos un nuevo tiempo
        tf = rospy.get_rostime().to_sec()
        #restamos para obtener el diferencial de timepo
        dt = tf-t0
        #Multiplicamos la distancia lineal por el diferencial y la sumamos a la distancia lineal recorrida total
        dis += turtle_cmd.linear.x*dt
        #mostramos la distancia recorrida
        rospy.loginfo("Distancia recorrida; %s",dis )
        #En cada ciclo le restamos un poco a la velocidad lineal para hacer el espiral
        turtle_cmd.linear.x  = turtle_cmd.linear.x  - 0.001
        #Publicamos la velocidad
        pub.publish(turtle_cmd)
        #Actualizamos el tiempo
        t0 = tf
        #Llamamos el sleep para garantizar los 20 mensajes por segundo
        rate.sleep()
#Si el archivo es corrido directametne y no llamado desde otro archivo corremos
if __name__ == "__main__":
    #Llamamos la funcion para mover la tortuga
    mov_lin()
