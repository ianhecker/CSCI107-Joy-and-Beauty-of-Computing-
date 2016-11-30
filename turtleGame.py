# -----------------------------------------+
# Ian Hecker                               | 
# CSCI 107, Assignment 10                  |
# Last Updated: December 2, 2015           |
# -----------------------------------------|
# Gamer Turtle! A simple concept game where| 
# three similar dots must be eaten in a row|
# -----------------------------------------+
import turtle
import random
wn = turtle.Screen()
wn.bgcolor("black")
turtle.title("Gamer Turtle!")
#------------------------------
title_turtle = turtle.Turtle()
title_turtle.hideturtle()
title_turtle.color("white")
title_turtle.up()
title_turtle.goto(0, 250)
title_turtle.write("Eat three dots of the same color!", False, align="center", font=("Verdana", 20, "italic"))
title_turtle.goto(0, 230)
title_turtle.write("Use arrow keys to navigate", False, align="center", font=("Verdana", 16, "italic"))
gamer = turtle.Turtle()
gamer.speed(0)
gamer.up()
gamer.color("white")
gamer.shape("turtle")
#--------------------
def dotColor():
	dave = turtle.Turtle() #Dave draws the dots
	dave.speed(0); dave.up(); dave.hideturtle()
	#------------------------------------------
	x = -150 #Creating Variables for coordinate plane and lists
	y = -150
	random_color_list = []
	color_list = ["red", "orange", "yellow", "green", "blue", "purple", "teal", "coral", "pink", "LimeGreen", "white"]
	coordList = []
	#-----------------
	for i in range(7): #For loops draw a 7 x 7 grid of dots
		for i in range(7):
			dave.goto(x, y)
			if x == 0 and y == 0: #skips dot at (0, 0)
				pass
			else:
				randomColor = random.choice(color_list) #Picking random color
				random_color_list.append(randomColor) #adds new color to list to keep track of
				dave.dot(20, randomColor)
				newCoordItem = "(" + str(x) + ", " + str(y) + ")" #formatting for list for comparing strings later
				coordList.append(str(newCoordItem)) #Now we have a list of colors/coordinates bound by index #
			y = y + 50 #moves up 50
		x = x + 50 #moves right 50
		y = -150 #moves turtle down to bottom (resetting)
	#----------------------------------------------------
	global random_color_list #allows variables to be accessed outside of function
	global color_list
	global coordList
#------------------	
dotColor()
#------------------------------
coordinates_already_visited = [] #Defining lists beforehand or else error occurs
three_colors_in_a_row = []
#------------------------
def gameMechanics(): #will allow gamer.turtle to detect which dot he ate
	x_test = int(round(gamer.xcor(), -1)) #round removes pesky decimal/zeroes and makes sure
	y_test = int(round(gamer.ycor(), -1)) #its a multiple of 50
	positionCheck = str("(" + str(x_test) + ", " + str(y_test) + ")") #formatting for comparing str's
	#-------------------------------------------------------------------------------------------------
	if positionCheck in coordinates_already_visited:
		pass #Keeps gamer.turtle from re-eating dots	
	elif positionCheck in coordList: #if coords not in list, gamer will eat the dot
		color_number = coordList.index(positionCheck)
		color_from_list = random_color_list[color_number]
		gamer.color(color_from_list)
		gamer.shapesize(1.5, 1.5, 1)
		gamer.dot(20, "black")
		coordinates_already_visited.append(str(positionCheck))
		three_colors_in_a_row.append(color_from_list)
	else: #just in case something goes wrong, gives a "pass"
		pass
	#----------------------------------
	global coordinates_already_visited
	global three_colors_in_a_row
	#----------------------------------
	if len(three_colors_in_a_row) == 2: #Checking if the colors in the list are similar
		if three_colors_in_a_row[0] != three_colors_in_a_row[1]:
			del three_colors_in_a_row[0] #if not similar, reset
			gamer.shapesize(1.5, 1.5, 1)
		else:
			gamer.shapesize(2, 2, 1)
	if len(three_colors_in_a_row) == 3:
		if three_colors_in_a_row[1] != three_colors_in_a_row[2]:
			for i in range(2):
				del three_colors_in_a_row[0]
				gamer.shapesize(1.5, 1.5, 1)
		else: #final else is the winning setup portion of code
			gamer.shapesize(2.5, 2.5, 1)
			three_colors_in_a_row = []
			winner_winner = turtle.Turtle()
			winner_winner.hideturtle()
			winner_winner.color("gold"); winner_winner.up()
			winner_winner.goto(0, -270)
			winner_winner.write("You've won!", False, align="center", font=("Arial", 30, "normal"))
			winner_winner.goto(0, -300)
			winner_winner.write("Click to exit", False, align="center", font=("Arial", 16, "normal"))
			turtle.tracer(0)
			wn.exitonclick()
	else:
		pass
#-----------
def right(): #tells gamer what to do if arrow is pressed
	gamer.setheading(0)
	gamer.fd(50)
	gameMechanics()	
def left():
	gamer.setheading(180)
	gamer.fd(50)
	gameMechanics()		
def up():
	gamer.setheading(90)
	gamer.fd(50)
	gameMechanics()	
def down():
	gamer.setheading(270)
	gamer.fd(50)
	gameMechanics()
#------------------		
wn.onkey(right, "Right") #helps gamer read keyboard key input
wn.onkey(left, "Left")
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.listen()
wn.mainloop()




