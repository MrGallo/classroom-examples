"""
Create a twoo-dimensional list to store the tree locations.
Use a for loop to draw the trees.
"""

import arcade


WIDTH = 640
HEIGHT = 480

tree_locations = [(100, 200), (125, 250), (300, 225), (350, 190), (600, 100)]


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
    arcade.draw_circle_filled(100, 100, 25, arcade.color.BLUE)

    # loop over two-dimensional list
    for x, y in tree_locations:
        arcade.draw_circle_filled(x, y, 30, arcade.color.PINE_GREEN)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
