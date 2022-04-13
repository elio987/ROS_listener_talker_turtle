#!/usr/bin/env python
#Autor: Leonardo Gracida Munoz
"""Programa de Python usando ROS, para poder susbcribirce a un topico
llamado /chat para poder desplegar el mensaje recibido en un cosola"""
import rospy
from std_msgs.msg import String
#Inicializamos el nodo
rospy.init_node("listener")
#Creamos la funcion callback para poder desplegar el mensaje recibido
def callback(msg):
    rospy.loginfo("Mensaje recibido: %s",msg.data)
#Creamos el susbscriber
rospy.Subscriber("/chat",String,callback)
#Si el archivo es corrido directametne y no llamado desde otro archivo corremos
if __name__ == "__main__":
    #Repetimos el codigo de manera infinita.
    rospy.spin()
