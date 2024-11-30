import turtle
t = turtle.Turtle()

t.circle(100)
t.undo() #used for back the operation

#long way
t.reset()
t.right(90)
t.forward(100)
t.left(90)
t.circle(100)
t.reset()
#short way

t.goto(0,-100) #-100 goes forward down
t.circle(100)


t.reset()
#positioning system

t.up()     #pull the pen up , no drawing while moving
t.goto(100,100) #x and y position and move turtle to an absolute position
t.down()     #pull the pen down drawing while moving
t.circle(100)

#without up down you cant see the line

