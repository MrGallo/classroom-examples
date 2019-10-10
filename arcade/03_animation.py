"""
Need a variable to facilitate change, or motion
- Where do you initialize it?
- Where do you update it?
- Where do you use it?

Make a variable called `x` and try to implement this.
"""

import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")


def setup():
    global x
    x = 100

    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    global x
    x += 1


@window.event
def on_draw():
    global x
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(x, 100, 25, arcade.color.BLUE)


if __name__ == '__main__':
    setup()
