"""
1. Create parallel lists of rain x and y values.
2. In the draw function, use a for loop with zip() to draw
rain at the x, y co-ordinates.
"""

import arcade


WIDTH = 640
HEIGHT = 480

# Parallel lists to store x and y values for each rain drop
rain_x_positions = [100, 200, 300]
rain_y_positions = [480, 480, 480]


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...

    # zip() pairs up values from multiple lists for we can
    # iterate through multiple lists at once
    for x, y in zip(rain_x_positions, rain_y_positions):
        arcade.draw_circle_filled(x, y, 25, arcade.color.BLUE)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
