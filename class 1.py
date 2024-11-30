import turtle
amul = turtle.Turtle()
amul.shape() #it shows current shape name default shape is classic
amul.shape('turtle')  #change the shape
help(turtle.shape) #know the shapes and more

amul.color() #default is ['black','black'] one is turtle color or another is line color

amul.forward(100) #samne jabe
amul.color("red") #turtle color
amul.forward(100)
amul.color("blue", "green") #line color change into blue and turtle color is green

amul.backward(300) #pichone jabe

#you cant use rgb directly you should change the setting like below
turtle.colormode(255)
amul.color(120,40,50)

turtle.done()