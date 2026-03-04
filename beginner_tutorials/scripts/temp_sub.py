#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def callback(msg):
    temperature = msg.data
    
    rospy.loginfo(f"Received Temperature: {temperature:.2f}")
    
    if temperature >= 35.0:
        rospy.logwarn("⚠ WARNING: High Temperature Detected!")

def temperature_subscriber():
    rospy.init_node('temperature_subscriber', anonymous=True)
    
    rospy.Subscriber('/temperature', Float32, callback)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        temperature_subscriber()
    except rospy.ROSInterruptException:
        pass