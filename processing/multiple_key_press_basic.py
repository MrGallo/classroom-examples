"""
To be able to check if multiple keys are pressed, you
need to store a few boolean vriables that remember if the keys are
being pressed. I made two below for the space bar and the up arrow.
"""

space_pressed = False
up_pressed = False

def setup():
    size(640, 480)

def draw():
    background(0)
    
    if up_pressed:
        background(200, 200, 0)
    if space_pressed:
        ellipse(50, 50, 50, 50)
    

def keyPressed():
    global space_pressed, up_pressed
    print(keyCode)
    if keyCode == 32:  # space keycode is 32
        space_pressed = True
    elif keyCode == 38:  # up arrow
        up_pressed = True


def keyReleased():
    global space_pressed, up_pressed
    if keyCode == 32: # space keycode is 32
        space_pressed = False
    elif keyCode == 38:  # up arrow
        up_pressed = False
