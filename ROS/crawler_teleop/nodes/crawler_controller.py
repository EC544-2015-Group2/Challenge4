#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


def callback(msg, vel_pub):
    twist = Twist()
    twist.linear.x = msg.axes[1]
    twist.angular.z = msg.axes[2]
    vel_pub.publish(twist)

if __name__ == '__main__':
    try:
	rospy.init_node('crawler_controller')
       	vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
	joy_sub = rospy.Subscriber('joy', Joy, callback, vel_pub)
	rospy.spin()
    except rospy.ROSInterruptException:
        pass
