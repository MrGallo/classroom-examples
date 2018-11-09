# Click on a color to make it transparent.


x = 0

def setup():
    global img, new_img, target
    size(640, 480)
    background(200)
    
    img = loadImage('basketball.jpg')
    new_img = makeTransparent(img, color(255, 255, 255))


def draw():
    global x
    x += 0.5
    if x + new_img.width > width:
        x = 0
    background(200)
    image(img, img.width, 100)
    image(new_img, x, 100)


def mousePressed():
    global img, new_img
    new_img = makeTransparent(img, get(mouseX, mouseY))


def makeTransparent(original, target=color(255), tolerance=100):
    """Will return a copy of an image with a prticular color made transparent.
    
    Args:
        original (PImage): The original image.
        target (color): The target color to make transparent. Default: white.
        tolerance (int): The tolerance for finding the target color. Default: 100
    
    Return:
        new_img (PImage): The new image with the target color made transparent.
    """
    
    new_img = createImage(original.width, original.height, ARGB)
        
    for i, colour in enumerate(original.pixels):
        diff = dist(red(colour), green(colour), blue(colour),
                    red(target), green(target), blue(target))
        if diff >= tolerance:
            new_img.pixels[i] = colour
    
    return new_img
