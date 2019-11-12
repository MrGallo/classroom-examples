import math
import random

import arcade


WIDTH = 640
HEIGHT = 480


class Sprite:
    def __init__(self, x: int, y: int, x_speed: int = 0, y_speed: int = 0):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.radius = 25
        self.color = arcade.color.BLUE
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
    
    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x > WIDTH or self.x < 0:
            self.x_speed = -self.x_speed
        
        if self.y > HEIGHT or self.y < 0:
            self.y_speed = -self.y_speed


window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")

sprites = []

for _ in range(10):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    dx = random.randrange(-5, 5)
    dy = random.randrange(-5, 5)

    color = []
    for _ in range(3):
        color.append(random.randrange(255))

    s = Sprite(x, y, dx, dy)
    s.color = color
    sprites.append(s)


def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    for s in sprites:
        s.update()


@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    for s in sprites:
        s.draw()


@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    for s in sprites:
        a = s.x - x
        b = s.y - y
        dist = math.sqrt(a**2 + b**2)

        if dist < s.radius:
            color = []
            for _ in range(3):
                color.append(random.randrange(255))
            s.color = color
            s.radius += 5
            if s.radius > 50:
                sprites.remove(s)
            


if __name__ == '__main__':
    setup()
