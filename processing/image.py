# Need to load image file into 
# the sketch's data folder.
# Top menu: Sketch -> Add File

def setup():
    global sat_img
    size(640, 480)
    sat_img = loadImage("image0.png")
    
def draw():
    background(255)
    image(sat_img, 50, 50, 550, 550)
