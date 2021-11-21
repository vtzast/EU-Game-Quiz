import turtle


screen = turtle.Screen()
screen.title('E.U Members Game')

image = 'Europe.gif'
screen.addshape(image)
turtle.shape(image)

# Spotting the coordinates

def get_mouse_click_coord(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coord)
turtle.mainloop()
