#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_in_circle():
    rospy.init_node('turtle_circle_mover', anonymous=True)
    
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(10)  # 10Hz
    
    vel_msg = Twist()
    
    # 원 운동 속도 설정
    vel_msg.linear.x = 2.0      # 전진 속도
    vel_msg.angular.z = 1.0     # 회전 속도
    
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_in_circle()
    except rospy.ROSInterruptException:
        pass