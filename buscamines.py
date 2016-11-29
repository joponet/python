import turtle
import random
import array

size=30
rows=6
columns=6
mines=3

window = turtle.Screen()
window.setup(1000,700)
myturtle=turtle.Turtle()
myturtle.hideturtle()
myturtle.penup()
myturtle.home()
posxi=-int(size*columns/2)
posyi=-int(size*rows/2)
table=[]

def table_draw():
	myturtle.setpos(posxi,posyi)
	myturtle.pendown()
	posy=posyi
	for posx in range (posxi,-posxi,size):
		posy=-posy
		myturtle.setpos(posx,posy)
		myturtle.setpos(posx+size,posy)
	myturtle.setpos(posx+size,-posy)
	myturtle.penup()
	myturtle.setpos(posxi,posyi)
	myturtle.pendown()
	posx=posxi
	for posy in range (posyi,-posyi,size):
		myturtle.pendown()
		posx=-posx
		myturtle.setpos(posx,posy)
		myturtle.setpos(posx,posy+size)
	myturtle.setpos(-posx,posy+size)
	myturtle.penup()

def getpos(x,y):
	row=int((y-posyi)/size)
	col=int((x-posxi)/size)
	if (row<0 or row>=rows or col<0 or col>=columns):
		row=-1
		col=-1
	pos=[col,row]
	print (pos)
	return pos

def markpos(pos,color):
	x= posxi + pos[0]*size +size/2
	y= posyi + pos[1]*size +size/2
	myturtle.penup()
	myturtle.setpos(x,y)
	myturtle.dot(10,color)

def calcpos(pos):
	col=pos[0]
	row=pos[1]
	status=table[row][col]
	if (status==0): return 'green'
	if (status==1): return 'orange'
	if (status==2): return 'red'
	return 'grey'

def setpos(row,col,value):
	if (table[row][col]==2): return False
	if (row<0 or row>=rows or col<0 or col>=columns): return False
	ok=False
	if (value==2):
		table[row][col]=value
		setpos(row-1,col-1,1)
		setpos(row-1,col,1)
		setpos(row-1,col+1,1)
		setpos(row,col-1,1)
		setpos(row,col+1,1)
		setpos(row+1,col-1,1)
		setpos(row+1,col,1)
		setpos(row+1,col+1,1)
		ok=True
	if (value==1 and table[row][col]==0):
		table[row][col]=value
		ok=True
	return ok

def startpos():
	for i in range (rows):
		row=[]
		for j in range (columns):
			row.append(0)
		table.append(row)
	print (table)
	selected=0
	while (selected<mines):
		col=random.randrange(columns-1)
		row=random.randrange(rows-1)
		if (setpos(row,col,2)):
			print ("(",row,",",col,")")
			selected +=1
		else:
			print ("Repe: (",row,",",col,")")
	print (table)
	return

def sortirclick(x,y):
	if (x>posxi and x<posxi+20 and y>-posyi+5 and y <-posyi+15): return True
	return False

def click(x,y):
	pos=getpos(x,y)
	if (pos[0]>=0):
		color=calcpos(pos)
		markpos(pos,color)
	if (sortirclick(x,y)): turtle.bye()	

def main():
	table_draw()
	myturtle.setpos(posxi,-posyi+10)
	myturtle.write("Sortir")
	window.onclick(click)
	startpos()
	turtle.mainloop()
	turtle.done()

main()
