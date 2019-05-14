"""
Create a parallel list of y values for our trees.
For loops by default only loop over one list, not two.

Create a while loop to loop over both lists using
index variable `i`.

Use the `zip()` function to zip both lists and loop
over both lists.
"""

import arcade


WIDTH = 640
HEIGHT = 480

tree_x_locations = [100, 125, 300, 350, 600]
tree_y_locations = [200, 250, 225, 190, 100]


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

    # while loop with i
    # for both x and y
    i = 0
    while i < len(tree_x_locations):
        x = tree_x_locations[i]
        y = tree_y_locations[i]
        arcade.draw_circle_filled(x, y, 30, arcade.color.PINE_GREEN)
        i += 1

    # zip()
    for x, y in zip(tree_x_locations, tree_y_locations):
        arcade.draw_circle_filled(x, y, 30, arcade.color.PINE_GREEN)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
