text_size = 30
rotation = 0
rotation_speed = 0
text_size_speed = 1
animate = False

def setup():
    size(640, 480)


def draw():
    global text_size
    global rotation
    global rotation_speed
    global text_size_speed

    if animate:
        rotation_speed += 0.01
        text_size_speed += 0.3
        text_size += text_size_speed
        rotation += rotation_speed
    
    background(0)
    
    textAlign(CENTER, CENTER)
    translate(width/2, height/2)
    rotate(rotation)
    textSize(text_size)
    fill(255, 255, 255, 255-text_size/2)
    text("Hello", 0, 0)


def mousePressed():
    global animate
    animate = not animate
