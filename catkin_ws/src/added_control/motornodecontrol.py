#!/usr/bin/python
# This is a ROS node designed to command the motors of KHAN and read the corresponding encoder data
# Author: Chris Corbett <ccc395@vt.edu>

# Imports
#commented out unecessary imports since we are not implementing encoder
import rospy
from sensor_msgs.msg import JointState
#from std_msgs.msg import String
#from khan_msgs.msg import Quadrature
#from rosgraph_msgs import Clock
#import quadrature
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
#from math import pi


#quad = quadrature.QuadratureEstimator(1000.0/3)

#frontleft
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_11", GPIO.OUT)
#front right
GPIO.setup("P8_9", GPIO.OUT)
GPIO.setup("P8_8", GPIO.OUT)
#rear left
GPIO.setup("P9_13", GPIO.OUT)
GPIO.setup("P9_15", GPIO.OUT)
#rear right
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_11", GPIO.OUT)


#controls front left wheel
def frontleft(flcmd):
  rate=6.8461703882*abs(flcmd.velocity[0]) + 4.7414065119 #emperically determined
  if rate > 99.9: #truncate PWM if velocity is too high
    rate = 100
  if flcmd.velocity[0] == 0:
    rate = 0
  PWM.start("P9_14", 50)
  if flcmd.velocity[0] > 0:
    #counterclockwise motion (forward)
    GPIO.output("P9_11", GPIO.HIGH)
    GPIO.output("P9_12", GPIO.LOW)
  if flcmd.velocity[0] < 0:
    #clockwise motion (backward)
    GPIO.output("P9_11", GPIO.LOW)
    GPIO.output("P9_12", GPIO.HIGH)


#controls front right wheel
def frontright(frcmd):
  rate=6.8461703882*abs(frcmd.velocity[0]) + 4.7414065119 #emperically determined
  if rate > 99.9: #truncate PWM if velocity is too high
    rate = 100
  if frcmd.velocity[0] == 0:
    rate = 0
  PWM.start("P8_13", 50)
  if frcmd.velocity[0] > 0:
    #counterclockwise motion (backward)
    GPIO.output("P8_8", GPIO.HIGH)
    GPIO.output("P8_9", GPIO.LOW)
  if frcmd.velocity[0] < 0:
    #clockwise motion (forward)
    GPIO.output("P8_8", GPIO.LOW)
    GPIO.output("P8_9", GPIO.HIGH)

 #controls rear left wheel
def rearleft(rlcmd):
  rate=6.8461703882*abs(rlcmd.velocity[0]) + 4.7414065119 #emperically determined
  if rate > 99.9: #truncate PWM if velocity is too high
    rate = 100
  if rlcmd.velocity[0] == 0:
    rate = 0
  PWM.start("P9_16", 50)
  if rlcmd.velocity[0] > 0:
    #counterclockwise motion (forward)
    GPIO.output("P9_13", GPIO.HIGH)
    GPIO.output("P9_15", GPIO.LOW)
  if rlcmd.velocity[0] < 0:
    #clockwise motion (backward)
    GPIO.output("P9_13", GPIO.LOW)
    GPIO.output("P9_15", GPIO.HIGH)

 #controls rear right wheel
def rearright(rrcmd):
  rate=6.8461703882*abs(rrcmd.velocity[0]) + 4.7414065119 #emperically determined
  if rate > 99.9: #truncate PWM if velocity is too high
    rate = 100
  if rrcmd.velocity[0] == 0:
    rate = 0
  PWM.start("P8_19", 50)
  if rrcmd.velocity[0] > 0:
    #counterclockwise motion (backward)
    GPIO.output("P8_10", GPIO.HIGH)
    GPIO.output("P8_11", GPIO.LOW)
  if rrcmd.velocity[0] < 0:
    #clockwise motion (forward)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_11", GPIO.HIGH)  




#subscribes to controller messages and calls functions that actually command wheels
def motorcommand():
    rospy.init_node('motorcommand', anonymous=True)
    rospy.Subscriber('/py_controller/front_left_wheel/cmd', JointState, frontleft)
    rospy.Subscriber('/py_controller/front_right_wheel/cmd', JointState, frontright)
    rospy.Subscriber('/py_controller/rear_left_wheel/cmd', JointState, rearleft)
    rospy.Subscriber('/py_controller/rear_right_wheel/cmd', JointState, rearright)
 
# FOLLOWING PART OF THE FUNCTION IS SUBSCRIBED TO TIME AND CALLS ENCODER-BASED FUNCTIONS, COMMENTED OUT BECAUSE OF LACK OF ENCODER


    rospy.spin()

if __name__ == '__main__':
  try:
    motorcommand()
  except rospy.ROSInterruptException:
    pass
