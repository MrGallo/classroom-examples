page = 0

def setup():
    size(640, 480)

def draw():
    if page == 0:
        background(155, 3, 255)
        fill(255)
        ellipse(100, 100, 40, 40)
    elif page == 1:
        background(255, 255, 0)
    elif page == 2:
        background(255, 100, 3)


def mousePressed():  # Triggers once per mouse-press
    global page
    page += 1
    if page == 3:
        page = 0
