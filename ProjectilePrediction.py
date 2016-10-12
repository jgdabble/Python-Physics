import math

"""def main():
	print("Welcome to the Physics PyCalc!")
	choice = input("What type of physics would you like to calculate?:")
	print("[Projectiles/Friction]")

	if(choice == "projectiles" or "Projectiles"):
		Projectiles()

	if(choice == "friction" or "Friction"):
		Friction()"""

def Projectiles():
	"""Asks for specifics of the problem, hight, distance, time, velocity etc."""
	lengthunits = input("Are you using meters or feet?")
	print("-------------------------------------------------------------------------------------------------")
	timeunits = input("Are you using seconds, minutes, or hours?")
	print("-------------------------------------------------------------------------------------------------")
	height = input("Enter the height that your projectile is fired from. If you are not given the hight, enter X.")
	print("-------------------------------------------------------------------------------------------------")
	distance = input("Enter the distance that your projectile flies before landing. If you are not given the distance, enter X.")
	print("-------------------------------------------------------------------------------------------------")
	time = input("Enter the total flight time of your projectile. If you are not given the time, enter X.")
	print("-------------------------------------------------------------------------------------------------")
	launchAngle = input("Enter the angle from the horizontal of the projectile at launch. If you are not given the angle, enter X.")
	print("-------------------------------------------------------------------------------------------------")
	velocity = input("Enter the velocity that your projectile is being fired at. If you are not given the velocity, enter X.")
	print("-------------------------------------------------------------------------------------------------")
	gravity = input("What acceleration is gravity? [10/9.8] :")

	# Because user input is saved as a string, this part converts each variable from a string to a float.
	# Float is short for Floating Point Decimal, which can be used in the same context as integer variables, but isn't restricted
	# to whole numbers like integers are.
	if(height != "x" and "X"):
		height = float(height)

	if(distance != "x" and "X"):
		distance = float(distance)

	if(velocity != "x" and "X"):
		velocity = float(velocity)

	if(launchAngle != "x" and "X"):
		launchAngle = float(launchAngle)

	if(time != "x" and "X"):
		time = float(time)

	gravity = float(gravity)

	componentdesision()

# Any line beginning with def defines a new function, which can be called later if required.
def componentdesision():
	global launchAngle
	global height
	global time
	global distance
	global velocity
	# In Python, indentation is how code is organized into branches.
	# this is the main function, this code will only be executed if main is called.
	if(launchAngle != 0):
		angled()

	if(height or time == "x" or "X"):
		vertical()

	elif(distance or velocity == "x" or "X"):
		horizontal()
	
def vertical():
	# This is the vertical function, this is the code responsible for calculating variables related to
	# the vertical component of the problem. Things like hight and time are calculated here.
	global height
	global time
	global gravity

	if(height == "x"):
		# The math formula for height, in case it isn't given in the problem.
		height = (.5 * gravity) * (time ** 2)
		print ("The height the projectile was fired from is: " + str(height) + " meters.")
	
	if(time == "x"):
		# The math formula for time, in case it isn't given in the problem, like in the lab.
		time = (height / (.5 * gravity)) ** .5
		print ("The total flight time of the projectile is: " + str(time) + " seconds.")

	if(distance or velocity == "x"):
		# This checks to see if anything else needs to be calculated, if not, then it will go to the answers function.
		horizontal()

	else:
		projectileanswers()

def horizontal():
	# This is the horizontal function, which is responsible for calculating the horizontal component of motion.
	global velocity
	global time
	global distance

	if(time == "x" or "X"):
		# This is just a fail safe, because time is nessessary for these equations, it checks to make sure that we actually have 
		# the value of time.
		vertical()

	if(velocity == "x"):
		# This calculates the velocity of the projectile just after shooting.
		velocity = 2 * (distance / time)
		print("The velocity of the projectile is: " + str(velocity) + " Meters per Second.")

	if(distance == "x"):
		# This calculates the distance the projectile will travel, in case it's not given in the problem.
		distance = (.5 * velocity) * time
		print("The horizontal distance of the projectile is: " + str(distance) + " meters.")

	# After everything is calculated and we have numerical values for every argument, the answers function is called.
	answers()

def angled():
	# this is only used if the projectile is launched at an angle other than 0 degrees, or horizontal.
	global velocity
	global launchAngle
	global distance
	global time

	if(velocity == "x"):
		velocity = 2 * (distance / time)

	verticalvel = (math.sin(math.radians(launchAngle)) * velocity) ** .5
	verticalvel = math.degrees(verticalvel)

	horizontalvel = (math.cos(math.radians(launchAngle)) * velocity) ** .5
	horizontalvel = math.degrees(horizontalvel)

def angledvertical():
	# this calculates the vertical component of a projectile if it launched at an angle other than horizontal.
	global verticalvel
	global height
	global time
	global gravity
	global distance
	global horizontalvel
	
	if(height == "x"):
		height = (-verticalvel) + ((.5 * gravity) * (time ** 2))
		print ("The height the projectile was fired from is: " + str(height) + " meters.")

	if(time == "x"):
		time = (height / ((.5 * gravity) + verticalvel)) ** .5
		print ("The total flight time of the projectile is: " + str(time) + " seconds.")

	if(distance or horizontalvel == "x"):
		angledhorizontal()

	else:
		projectileanswers()

def angledhorizontal():
	# This calculates the horizontal component of a projectile if launched at an angle other than horizontal.
	global time
	global distance
	global horizontalvel

	if(time == "x"):
		verticalvel()

	if(horizontalvel == "x"):
		horizontalvel = 2 * (distance / time)
		print("The velocity of the projectile is: " + str(horizontalvel) + " Meters per Second.")

	if(distance == "x"):
		distance = (.5 * velocity) * time
		print("The horizontal distance of the projectile is: " + str(distance) + " meters.")

	answers()

def answers():
	# This function only does one thing: tell you the solution to the calculations done above.
	print("------------------------------------------------------------|")
	print("The projectile was launched from a height of: " + str(height) + lengthunits)
	print("------------------------------------------------------------|")
	print("With a velocity of: " + str(velocity) + " " + lengthunits + " per " + timeunits)
	print("------------------------------------------------------------|")
	print("The projectile flew: " + str(distance) + lengthunits)
	print("------------------------------------------------------------|")
	print("The projectile launched at an angle of: " + str(launchAngle) + " degrees.")
	print("------------------------------------------------------------|")
	print("and the projectile had a total flight time of: " + str(time) + timeunits)

"""def Friction():
	mass = input("What is the mass of the object in question?")
	surfaceangle = input("What angle is the surface at?")
	netforce = input("What is the net force exerted on the object? (Up and to the Right are Positive(+)")
	friction = input("What is the force of friction?")
"""
# Python is a scripting language, meaning that it runs line by line instead of being compiled like java, C, C#, or almost any 
# other programming language out there. Because of this, we can only call a function after it's read over the function, so we
# call the function at the bottom of the script, so the computer has a chance to read over everything.
projectiles()
