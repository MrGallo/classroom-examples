class Ring:
    def __init__(self, x, y, diameter, col):
        self.diameter = diameter
        self.rotation = random(2*PI)
        self.rotation_speed = random(-0.05, 0.05)
        self.arc_size = random(0, PI/2)
        self.arc_growth_speed = 0
        self.arc_growth_accel = random(0.0001, 0.001)
        self.x = x
        self.y = y
        self.color = col

    def update(self):
        self.arc_growth_speed += self.arc_growth_accel
        self.arc_size += self.arc_growth_speed

        if self.arc_size >= 3*2*PI/4 or self.arc_size <= 0:
            self.arc_size = constrain(self.arc_size, 0, 3*2*PI/4)
            self.arc_growth_speed = -self.arc_growth_speed
    
        self.rotation += self.rotation_speed

    def draw(self):
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.rotation)
        noFill()
        strokeWeight(10)
        stroke(self.color)
        arc(0, 0, self.diameter, self.diameter, 0, self.arc_size)
        popMatrix()


rings = []


def setup():
    global ring1, ring2

    size(800, 600)
    rings.append(Ring(width/2, height/2, 260, color(70, 130, 70)))
    rings.append(Ring(width/2, height/2, 260, color(20, 200, 10)))
    rings.append(Ring(width/2, height/2, 300, color(255)))
    rings.append(Ring(width/2, height/2, 300, color(255)))


def draw():
    global rings

    background(80)
    drawLogo(width/2, height/2)

    for ring in rings:
        ring.update()
        ring.draw()


def mousePressed():
    print("({}, {})".format(mouseX, mouseY))


def drawLogo(x, y):

    pushMatrix()
    translate(x, y)
    # bottom
    noFill()
    strokeWeight(30)
    stroke(255)
    strokeCap(SQUARE)
    arc(0, 0, 200, 200, -PI/4, 5*PI/4)

    # top
    stroke(20, 170, 10)
    strokeWeight(30)
    strokeCap(SQUARE)
    arc(0, 0, 200, 200, -2.93*PI/4, -1.07*PI/4)

    # inner left rect
    stroke(255)
    strokeWeight(30)
    strokeCap(SQUARE)
    line(0-15, 0+15, 0-60, 0+60)

    # inner left triangle
    fill(255)
    noStroke()
    strokeCap(SQUARE)
    triangle(0-4, 0+27, 0-4, 0-40, 0-26, 0+6)

    # inner right rect
    stroke(255)
    strokeWeight(30)
    strokeCap(SQUARE)
    line(0+15, 0+15, 0+60, 0+60)

    # inner right triangle
    fill(255)
    noStroke()
    strokeCap(SQUARE)
    triangle(0+4, 0+27, 0+4, 0-40, 0+26, 0+6)
    popMatrix()
