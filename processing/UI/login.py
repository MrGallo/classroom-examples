# Very messy.

import time

def setup():
    global back_img, menu_img, menu_shadow
    fullScreen(P2D)
    # size(720*2, 480*2, P2D)
    menu_img_raw = loadImage("6835100-landscape.jpg")
    menu_img = createGraphics(300, 150)
    menu_img.beginDraw()
    menu_img.imageMode(CENTER)
    menu_img.scale(0.5)
    menu_img.image(menu_img_raw, 0, 350)
    menu_img.endDraw()
    
    menu_shadow = createGraphics(350, 550)
    menu_shadow.beginDraw()
    menu_shadow.noStroke()
    menu_shadow.fill(0, 100)
    menu_shadow.rectMode(CENTER)
    menu_shadow.rect(350/2, 550/2, 300, 500, 10)
    menu_shadow.filter(BLUR, 3)
    menu_shadow.endDraw()
    
    back_img = loadImage("beach-blur-boardwalk-132037.jpg")
    back_img.loadPixels()
    back_img.filter(BLUR, 11)
    back_img.updatePixels()


def draw():
    start_time = time.time()
    
    # Background
    x = width/2 - map(mouseX, 0, width, -10, 10)
    y = height/2- map(mouseY, 0, width, -10, 10)
    imageMode(CENTER)
    image(back_img, x, y)
    print("Frame {}: {} ms.".format(frameCount, int((time.time()-start_time)*1000)))
    
    # MENU
    
    # Background
    imageMode(CENTER)
    image(menu_shadow, width/2+5, height/2+5)
    noStroke()
    rectMode(CENTER)
    fill(255)
    rect(width/2, height/2, 300, 500, 10)
    
    
    # Button
    fill("#06D6A0")
    rectMode(CENTER)
    rect(width/2, height/2+180, 250, 50, 5)
    fill("#FFFCF9")
    
    textSize(20)
    textAlign(CENTER, CENTER)
    text("Submit", width/2, height/2+180)
    
