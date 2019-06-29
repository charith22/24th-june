import turtle as tt
a1=tt.Turtle()
colors=['red','blue','green']
dot_distance=10
width=10
height=15

a1.penup()
a1.goto(-360,0)
a1.penup()

for x in range(height):
    a1.pencolor(colors[x%3])
    for i in range(width):
        a1.dot()
        a1.forward(dot_distance)
    a1.forward(dot_distance*width)
    a1.right(90)
    a1.forward(dot_distance)
    a1.left(90)

tt.done()
