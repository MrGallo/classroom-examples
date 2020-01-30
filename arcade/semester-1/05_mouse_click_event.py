import math
import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
ball_x = 50
x_speed = 7


def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    global ball_x, x_speed
    ball_x += x_speed

    if ball_x > WIDTH:
        x_speed = -5
    elif ball_x < 0:
        x_speed = 5


@window.event
def on_draw():
    global ball_x
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(ball_x, 100, 25, arcade.color.BLUE)


@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x, y, button, modifiers)
    a = x - ball_x
    b = y - 100
    dist = math.sqrt(a**2 + b**2)

    # next: complete the if statement. Print "CLICKED" if clicked.
    # if ...


if __name__ == '__main__':
    setup()
