import turtle
t = turtle.Turtle()

#set turtle drawing speed
t.speed(0) # 0 is fast 1 is slow
#lets make a square box

#hard way
'''
t.forward(100)
t.left(90) #upper
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
'''
t.begin_fill() # for fill the box with color after draw and default color is black
t.fillcolor("blue") #customize color
#easy way
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
#after this program i want to hide the turtle
t.hideturtle() #kintu er easy way oi lekhar  upor likhle we cant see turle during drawing


turtle.done()