import turtle
import math

r=100
window = turtle.Screen()
window.setup(1000,700)
myturtle=turtle.Turtle()
myturtle.home()
segments=int(1)
while (r>0):
	r=int(input("Radi: "))
	if r>0:
		inc = int(math.acos(1-(1/r))*180/math.pi)
		print(inc)
		myturtle.clear()
		myturtle.penup()
		myturtle.setpos(r,0)
		myturtle.pendown()
		for a in range (0,360,inc):
			x=r*math.cos(a*math.pi/180)
			y=r*math.sin(a*math.pi/180)
			myturtle.setpos(x,y)
		myturtle.setpos(r,0)
		myturtle.penup()
		myturtle.home()



