#!/usr/bin/python

# Demo of some programming concepts in Python
# Initial code written by: Jason Ziglar <jpz@vt.edu>
# Extended and modified by: Christopher Corbett <c3.corbett@gmail.com>
#importing math to be used in calculations
import math
# Define a function which computes the harmonic series
def harmonic_series(num_terms):
  '''Function which computes some number of terms from the harmonic series.
  num_terms: the number of terms to add together.
  returns: The value computed'''

  #Create variable to store result, set to some initial value
  value = 0

  #range produces a sequence of numbers, [0, num_terms), and executes the loop
  # with ii set to each value
  for ii in range(num_terms):
    #Set value to the value plus the next term
    # Note: Computers start counting at 0, so we have to add 1 to be safe
    value = value + (1.0 / (ii + 1))

  # Return the value to whomever called this function
  return value

#Defining a function to compute the summation approx. for pi
def pisum(piterations):
	  #creating a value to store pi, set to 0, and declaring a count variable
	  pi, count = 0, 1
	  #while the current variable is within the set:
	  while count <= piterations:
	    #utilizing the provided summation equation
	    pipiece = math.sqrt(6/(math.pow(count,2)))
	    #adding the newest approximation of pi to the sum
	    pi = pi + pipiece
	    count = count + 1
	  return pi

def harmonic_series_while(num_terms):
  '''Function which computes some number of terms from the harmonic series, using a while loop.
  num_terms: the number of terms to add together.
  returns: The sum of the first n terms of the series'''



  #Create variable to store summation
  value = 0
  #A counter to keep track of how many terms have been computed
  counter = 0

  # This will run until "counter <= num_terms" returns a false statement
  while counter < num_terms:
    value = value + (1.0 / (counter + 1))
    # Very important - while runs until it sees false, so we have to make sure
    # the test will eventually fail
    counter = counter + 1

  # Return value
  return value

#Starting here, the program begins execution, since the previous statements were describing functions, but not actually calling them
# Print a welcome
com = int(float(raw_input("Hello, Please choose a command: 1) harmonic series approximation program 2) pi approximation.")))
if com != 1 and com !=2:
  print "error: please choose either 1 or 2. You have now been chastised."
else:
  if com == 1:
	print "Welcome to a simple harmonic series approximation program."
	#Ask the user to select a function

	while True:
	  request = raw_input("Select which function to use: 1) For loop 2) While loop 3) Stop: ")
	  #Convert that input to an integer
	  request = int(float(request))
	  if request == 3:
	  	#Will stop the loop when executed
	  	break
	  if request != 1 and request !=2:
	  	#error message given when the received value does not match with either choice
	    print "error: please choose either 1 or 2. You have now been chastised."
	  else:
	    #Same as before, but in a single line.
	    iterations = int(float(raw_input("How many terms should I use? ")))
	    if iterations <=0:
	      print 0
	    else:
	    # Test input
	      if request == 1:
	        # Get value form function
	        result = harmonic_series(iterations)
	        # Print using a technique known as string interpolation. %s means "take the next value after the string and insert as a string"
	        # So it will look at the list of values after the % and grab the next (only) one
	        # For more details, look here: https://docs.python.org/2/library/stdtypes.html#string-formatting
	        print "For loop produces: %s" % result
	      else:
	        # Same as previous statement, but notice you don't have to store a value in a variable before using it, if it makes sense.
	        print "While loop produces %s" % harmonic_series_while(iterations)
  else:
	piterations = int(float(raw_input("How many iterations would you like?: ")))
	#stores the sum of the value of pi as pianswer
	pianswer = pisum(piterations)
	print "The pi summation is: %s" % pianswer
	 # ccc395
