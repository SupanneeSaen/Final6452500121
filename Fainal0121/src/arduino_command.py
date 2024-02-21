#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16


def send(num):
    pub = rospy.Publisher("arduinocommand",Int16,queue_size=10)
    pub.publish(num)

sub = rospy.Subscriber("Status",Int16,callback=send)
rospy.init_node("Arduino_Command")
rospy.spin()
