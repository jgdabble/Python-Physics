import math

def physicstype():
	print("What type of physics would you like to calculate? (type in the number)")
	print("1. projectiles")
	print("2. friction")
	print("3. attwood machine")
	choice = input()

	if(choice == "1"):
		Projectiles()

	if(choice == "2"):
		Friction()

	if(choice == "3"):
		print("This part isn't ready yet.")
		physicstype()

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

	if(launchAngle != 0):
		Projectileangled(velocity, launchAngle, distance, time)

	if(height or time == "x" or "X"):
		Projectilevertical(height, time, gravity, distance, velocity)

	elif(distance or velocity == "x" or "X"):
		Projectilehorizontal(velocity, time, distance)
	
def Projectilevertical(height, time, gravity, distance, velocity):
	# This is the vertical function, this is the code responsible for calculating variables related to
	# the vertical component of the problem. Things like hight and time are calculated here.

	if(time == "x" or "X"):
		
		time = (height / (.5 * gravity)) ** .5
		print ("The total flight time of the projectile is: " + str(time) + " seconds.")

	if(height == "x" or "X"):
		
		height = (.5 * gravity) * (time ** 2)
		print ("The height the projectile was fired from is: " + str(height) + " meters.")

	if(distance or velocity == "x" or "X"):
		# This checks to see if anything else needs to be calculated, if not, then it will go to the answers function.
		Projectilehorizontal(velocity, time, distance)

	else:
		projectileanswers()

def Projectilehorizontal(velocity, time, distance):
	# This is the horizontal function, which is responsible for calculating the horizontal component of motion.
	if(velocity == "x"):
		
		velocity = distance / time
		print("The velocity of the projectile is: " + str(velocity) + " Meters per Second.")

	if(distance == "x"):
		
		distance = (.5 * velocity) * time
		print("The horizontal distance of the projectile is: " + str(distance) + " meters.")

	projectileanswers()

def Projectileangled(velocity, launchAngle, distance, time):
	# this is only used if the projectile is launched at an angle other than 0 degrees, or horizontal.

	if(velocity == "x"):
		velocity = (distance / time)

	verticalvel = (math.sin(math.radians(launchAngle)) * velocity) ** .5
	verticalvel = math.degrees(verticalvel)

	horizontalvel = (math.cos(math.radians(launchAngle)) * velocity) ** .5
	horizontalvel = math.degrees(horizontalvel)

	if(height or time == "x" or "X"):
		Projectileangledvertical(verticalvel, height, time, gravity, distance, horizontalvel)

	elif(distance or horizontalvel == "x"):
		Projectileangledhorizontal(time, distance, horizontalvel)

	else:
		projectileanswers()

def Projectileangledvertical(verticalvel, height, time, gravity, distance, horizontalvel):
	# this calculates the vertical component of a projectile if it launched at an angle other than horizontal.
	if(height == "x"):
		height = (-verticalvel) + ((.5 * gravity) * (time ** 2))
		print ("The height the projectile was fired from is: " + str(height) + " meters.")

	if(time == "x"):
		time = (height / ((.5 * gravity) + verticalvel)) ** .5
		print ("The total flight time of the projectile is: " + str(time) + " seconds.")

	if(distance or horizontalvel == "x"):
		Projectileangledhorizontal()

	else:
		projectileanswers()

def Projectileangledhorizontal(time, distance, horizontalvel):
	# This calculates the horizontal component of a projectile if launched at an angle other than horizontal.
	if(horizontalvel == "x"):
		horizontalvel = 2 * (distance / time)
		print("The velocity of the projectile is: " + str(horizontalvel) + " Meters per Second.")

	if(distance == "x"):
		distance = (.5 * velocity) * time
		print("The horizontal distance of the projectile is: " + str(distance) + " meters.")

	projectileanswers()

def projectileanswers():
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

# This is where the projectile prediction ends, and Friction calculations begin.
def Friction():
	mass = input("What is the mass of the object in question?")
	print("-------------------------------------------------------------------------------------------------")
	surfaceangle = input("Is the surface an incline? If so, what angle is it at?")
	print("-------------------------------------------------------------------------------------------------")
	force = input("What is the force exerted on the object? (Up and to the Right are Positive(+))")
	print("-------------------------------------------------------------------------------------------------")
	forceangle = input("Is the force acting at an angle? If so, what angle?")
	print("-------------------------------------------------------------------------------------------------")
	frictionforce = input("What is the force of friction?")
	print("-------------------------------------------------------------------------------------------------")
	frictioncoefficient = input("What is the coefficient of friction?")
	print("-------------------------------------------------------------------------------------------------")
	acceleration = input("What is the acceleration of the object?")
	print("-------------------------------------------------------------------------------------------------")
	gravityForce = input("What is the force of gravity?")
	print("-------------------------------------------------------------------------------------------------")
	gravity = input("What acceleration is gravity? [10/9.8] :")

	if(mass != "x" and "X"):
		mass = float(mass)

	if(surfaceangle != "x" and "X"):
		surfaceangle = float(surfaceangle)

	if(force != "x" and "X"):
		force = float(force)

	if(forceangle != "X" and "X"):
		forceangle = float(forceangle)

	if(frictionforce != "x" and "X"):
		frictionforce = float(frictionforce)

	if(frictioncoefficient != "x" and "X"):
		frictioncoefficient = float(frictioncoefficient)

	if(acceleration != "x" and "X"):
		acceleration = float(acceleration)

	if(gravityForce != "x" and "X"):
		gravityForce = float(gravityForce)

	gravity = float(gravity)

	if(surfaceangle == 0):
		Frictionflat(gravity, frictionforce, frictioncoefficient, force, mass, acceleration)

	else:
		Frictionincline(gravity, force, frictionforce, frictioncoefficient, mass, acceleration, surfaceangle, gravityForce, forceangle)

def Frictionflat(frictionforce, forceangle, frictioncoefficient, force, mass, acceleration, gravity):

	if(forceangle !=0):
		if(gravcompsfound != True):
			Frictionangledforce(force, forceangle)

		else:
			if(frictionforce == "x" or "X"):https://tiplanet.org/forum/archives_voir.php?id=89439
				frictionforce = (mass * acceleration) - horizontalforce

	if(force == "x" or "X"):
		force = (mass * acceleration) + frictionforce

	if(frictionforce == "x" or "X"):
		frictionforce = (mass * acceleration) - force

	if(frictioncoefficient == "x" or "X"):
		frictioncoefficient = frictionforce / gravityForce

	FrictionAnswers()

def Frictionangledforce(force, forceangle, surfaceangle):
	verticalforce = math.sin(math.radians(forceangle)) * force
	verticalforce = math.degrees(verticalforce)

	horizontalforce = math.cos(math.radians(forceangle)) * force
	horizontalforce = math.degrees(horizontalforce)

	gravcompsfound = True

	if(surfaceangle != 0):
		Frictionincline(gravity, frictionforce, frictioncoefficient, mass, acceleration, horizontalforce, verticalforce)

	elif(surfaceangle == 0):
		Frictionflat(frictionforce, frictioncoefficient, verticalforce, horizontalforce, mass, acceleration, gravity)

	else:
		FrictionAnswers()


def Frictionincline(gravity, force, frictionforce, frictioncoefficient, mass, acceleration, surfaceangle, gravityForce, forceangle):
	print("This part isn't ready yet.")

	if(gravityForce == "x" or "X"):
		gravityForce = mass * gravity

	verticalgrav = math.sin(math.radians(surfaceangle)) * gravityForce
	verticalgrav = math.degrees(verticalgrav)

	horizontalgrav = math.cos(math.radians(surfaceangle)) * gravityForce
	horizontalgrav = math.degrees(horizontalgrav)

	if(acceleration == "x" or "X"):
		acceleration = horizontalgrav / mass

	if(forceangle !=0):
		if(gravcompsfound != True):
			Frictionangledforce(force, forceangle)

		else:
			if(frictionforce == "x" or "X"):
				frictionforce = (mass * acceleration) - horizontalforce

	if(force == "x" or "X"):
		force = (mass * acceleration) + frictionforce

	if(frictionforce == "x" or "X"):
		frictionforce = (mass * acceleration) - force

	if(frictioncoefficient == "x" or "X"):
		frictioncoefficient = frictionforce / verticalgrav

	FrictionAnswers()

def FrictionAnswers():
	print("------------------------------------------------------------|")
	print("The object has a mass of: " + mass + "kg.")
	print("------------------------------------------------------------|")
	print("The surface was an incline of: " + surfaceangle + " degrees.")
	print("------------------------------------------------------------|")
	print("A force of: " + force + "Newtons was exerted on the object,")
	print("at an angle of: " + forceangle + " degrees.")
	print("------------------------------------------------------------|")
	print("The total force of friction is: " + frictionforce + " Newtons,")
	print("with a coeficeint of: " + frictioncoefficient + ".")
	print("------------------------------------------------------------|")
	print("The object had an acceleration of: " + acceleration + "meters per second squared.")


physicstype()
