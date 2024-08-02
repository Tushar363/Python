import turtle

mypen= turtle.Turtle()
mypen.shape('turtle')
mypen.speed(20)

window= turtle.Screen()
window.bgcolor('white')
rainbow= ['red','orange','yellow','green','blue','indigo','violet','black']
size= 250
mypen.penup()
mypen.goto(0,-180)
for color in rainbow:
	mypen.color(color)
	mypen.fillcolor(color)
	mypen.begin_fill()
	mypen.circle(size)
	mypen.end_fill()
	size-=22

turtle.done()
