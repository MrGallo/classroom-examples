"""
To be able to check if multiple keys are pressed, you
need to store a list of boolean values.

The list indicies are teh keyCode for each key. The list will store
true or false for that keyCode
"""

# Keycodes span roughly from 0-222
# setting keys[0-255] to False
keys_pressed = [False for key_code in range(256)]

def setup():
    size(640, 480)

def draw():
    background(0)
    
    if keys_pressed[38]:  # up
        background(200, 200, 0)
    if keys_pressed[32]:  # space
        ellipse(50, 50, 50, 50)
    

def keyPressed():
    global keys_pressed
    print(keyCode)
    keys_pressed[keyCode] = True


def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False
