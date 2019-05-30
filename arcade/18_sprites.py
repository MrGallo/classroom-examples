"""
Sprites in arcade.
Sprites are just game objects that interact with eachother.
E.g., the player, enemies, lazer bolts, asteroids.

Provided you have an image, rendering sprites is faster than drawing shapes.
"""

import os
import arcade

# Because my code is in a sub-folder, I need to tell python
# to read in files relative to my code file.
# You may not have to import os and insert the following two lines.
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

WIDTH = 640
HEIGHT = 480

player = arcade.Sprite('images/playerShip1_blue.png', center_x=WIDTH/2, center_y=HEIGHT/2, scale=0.5)


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    player.draw()


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
