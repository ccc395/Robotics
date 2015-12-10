#!/usr/bin/python
# This is a ROS node that will command the motors to execute a given velocity
# Author: Your Name <your_email@vt.edu>

# Import the Default ROS tools
import rospy
# Import the JointState message from sensor_msgs
from sensor_msgs.msg import JointState
# Import String as well
from std_msgs.msg import String

# Create variable so we can always see/use it, but set it to a value that indicates it's not yet valid
pub_front_left = None
pub_front_right = None
pub_back_left = None
pub_back_right = None

#Function which is called every time a JointState is received, if the Subscriber is set up to use this function
def js_call(data):
  #print name of first joint in JointMessage. This will crash on an empty message
  print "Publishing", data.name[0]
  #Declare using the global pub
  global pub
  #Create the new message as an example output
  new_msg = String()
  new_msg.data = data.name[0]
  #Publish the new message for demonstration
  pub.publish(new_msg)

# If this is loaded as the main python file, execute the main details
if __name__ == '__main__':
  try:
    #Initialize node
    rospy.init_node('motor_command')
    # Declare we are using the pub defined above, not a new local variable
    global pub
    #Create publisher, to send out a String with the first joint name of every received message as an example.
    pub_enc_front_left = rospy.Publisher('/py_controller/front_left/cmd', String, queue_size=10)
    pub_enc_front_right = rospy.Publisher('/py_controller/front_right/cmd', String, queue_size=10)
    pub_enc_back_left = rospy.Publisher('/py_controller/back_left/cmd', String, queue_size=10)
    pub_enc_back_right = rospy.Publisher('/py_controller/back_right/cmd', String, queue_size=10)
    #Create subscriber, and tell it to call js_call() whenever a message is received
    sub_front_left = rospy.Subscriber('/py_controller/front_left/cmd', JointState, js_call)
    sub_front_right = rospy.Subscriber('/py_controller/front_right/encoder', JointState, js_call)
    sub_back_left = rospy.Subscriber('/py_controller/back_left/encoder', JointState, js_call)
    sub_back_right = rospy.Subscriber('/py_controller/back_right/encoder', JointState, js_call)

    #We need to wait for new messages
    rospy.spin()
  #If we are interrupted, catch the exception, but do nothing
  except rospy.ROSInterruptException:
    pass
