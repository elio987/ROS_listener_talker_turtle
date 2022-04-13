#!/usr/bin/env python
#Autor: Leonardo Gracida Munoz
"""Programa de Python usando ROS, para poder publicar un mensaje tipo String
a un topico llamada /chat"""
import rospy
from std_msgs.msg import String
#Inicializamos el nodo
rospy.init_node("talker")
#Creamos el publisher
pub = rospy.Publisher("/chat", String, queue_size=1)
#Declaramos que vamos a mandar 10 mensajes por segundos
rate = rospy.Rate(10)
#El mensaje a enviar va a ser de tipo String
msg = String()
#Si el archivo es corrido directametne y no llamado desde otro archivo corremos
if __name__ == "__main__":
    #mientras ROS este activado
    while not rospy.is_shutdown():
        #Le unimos al mensaje el timepo transcurrido en ROS
        msg.data = "Hello world "+str(rospy.get_time())
        #Publicamos el mensaje
        pub.publish(msg)
        #Y hacemos el sleep para asegurar los diez mensajes por segundo
        rate.sleep()
