import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
x = 50
x_speed = 7


def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    global x, x_speed
    x += x_speed

    if x > WIDTH:
        x_speed = -5
    elif x < 0:
        x_speed = 5


@window.event
def on_draw():
    global x
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(x, 100, 25, arcade.color.BLUE)


@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
