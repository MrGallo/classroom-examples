# A functionless, non-DRY implementation of Clicky-Ball

COL1 = "#832232"
COL2 = "#EAF27C"

player1_score = 0
player2_score = 0

def setup():
    global ball1_x, ball1_y, ball2_x, ball2_y
    # size(640, 480)
    fullScreen()
    ball1_x = random(0+50, width/2-50)
    ball1_y = random(0+50, height-50)
    
    ball2_x = random(width/2+50, width-50)
    ball2_y = random(0+50, height-50)


def draw():
    # Player 1
    # Background
    fill(COL1)
    rect(0, 0, width/2, height)
    # ball
    fill(COL2)
    ellipse(ball1_x, ball1_y, 100, 100)
    # score 
    textSize(50)
    textAlign(CENTER, CENTER)
    fill(255)
    text("Score: " + str(player1_score), width/4, height/8)
    
    # Player 2
    # Background
    fill(COL2)
    rect(width/2, 0, width/2, height)
    # ball
    fill(COL1)
    ellipse(ball2_x, ball2_y, 100, 100)
    # score 
    textSize(50)
    textAlign(CENTER, CENTER)
    fill(255)
    text("Score: " + str(player2_score), 3*width/4, height/8)
    
    if player1_score >= 10:
        noLoop()
        background(255)
        fill(0)
        text("Player 1 wins!", width/2, height/2)
    elif player2_score >= 10:
        noLoop()
        background(255)
        fill(0)
        text("Player 2 wins!", width/2, height/2)


def mousePressed():
    global ball1_x, ball1_y, ball2_x, ball2_y, player1_score, player2_score
    
    # Check ball 1 click
    distance = dist(ball1_x, ball1_y, mouseX, mouseY)
    if distance < 50:
        player1_score += 1
        ball1_x = random(0+50, width/2-50)
        ball1_y = random(0+50, height-50)
        print("{}: Clicked Ball 1".format(frameCount))
    
    # Check ball 2 click
    distance = dist(ball2_x, ball2_y, mouseX, mouseY)
    if distance < 50:
        player2_score += 1
        ball2_x = random(width/2+50, width-50)
        ball2_y = random(0+50, height-50)
        print("{}: Clicked Ball 2".format(frameCount))
