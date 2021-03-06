#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String

def callback(data):
	pub = rospy.Publisher('/assignment1_publisher_subscriber', String, queue_size=10)
	pub.publish(str(data.data))
	#print(data.data)
	
		
def publisher_subscriber():
	print("Node started")
	rospy.init_node('publisher_subscriber', anonymous=True)

	rospy.Subscriber("/yaw", Float32, callback)

	rospy.spin()

if __name__ == '__main__':
	publisher_subscriber()
