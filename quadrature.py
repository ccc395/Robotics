#!/usr/bin/python
# Object for decoding/estimating Quadrature decodings.
# Framework by: Jason Ziglar <jpz@vt.edu>
import math

class QuadratureEstimator:
  def __init__(self, ticks_per_revolution):
    self.ticks_per_revolution = ticks_per_revolution
    self._position = 0
    self._velocity = 0
    count = 0
    pulcount = 0
    vel = 0
    position = 0
    trash = 0
  def update(self, a_state, b_state, time):
    # Implement decoding here. Note you'll remove the pass statement once you start implementing this
      while True
      #sets up where the initial velocity and position is not calculated as it cannot be
        if count != 0:
          #if moving forward
          if ((a_state, b_state_old) == (1,0)) or ((a_state,b_state_old) ==(0,1)):
            #declares the direction of travel is forwards
            direction = "+"
            #declares the location of each pulse
            if (a_state, a_state_old, b_state) == (1,0,0):
              pulcount = pulcount + 1
            #calculates the velocity
            vel = (((pulcount/ticks_per_revolution) * 60)/(time - time_old))
          #if moving backward
          elif((a_state,b_state_old == (1,1))) or ((a_state,b_state_old) == (0,0)):
            #declares the direction of travel is reverse
            direction = "-"
            #declares the location of each pulse
            if (a_state, a_state_old, b_state) == (1,0,0):
              pulcount = pulcount + 1
            #calculates the velocity
            vel = (((pulcount/ticks_per_revolution) * 60)/(time - time_old))
          else:
            #stores the values for when there is no pulse or seperate tic
            trash = trash + 1
          #sets the current states as the old states
          a_state = a_state_old
          b_state = b_state_old
        else:
          time = time_old
          count = count + 1
          a_state = a_state_old
          b_state = b_state_old      
        self._velocity = direction + vel
        position = velocity * time

  @property
  def position(self):
      return self._position
  @property
  def velocity(self):
      return self._velocity



