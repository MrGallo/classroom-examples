x = 0

def setup():
    size(640, 480)


def draw():
    global x
    
    if x >= 640:
        x = 0
    x += 3
    
    background(135, 206, 250)  # sky blue
    
    # cloud
    noStroke()
    ellipse(x, height/2, 50, 50)
    ellipse(x+30, height/2, 50, 50)
    ellipse(x+10, height/2-20, 50, 50)

