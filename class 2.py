import turtle
amul = turtle.Turtle()
amul.color("red")
amul.shape('turtle')
wn = turtle.Screen()  #screen object
wn.bgcolor("black") #background color

#rgb use setup
turtle.colormode() #default 1.0
turtle.colormode(255)
wn.bgcolor(170,30,20)

#window title
wn.title("Amul")

#background picture
#image file should "gif" format and picture and python file should be same folder

'''
import turtle
amul = turtle.Turtle()
wn = turtle.Screen()
wn.bgpic("pic.gif")
'''