"""
Importing and drawing images.
1. In the folder that contains your code, create a folder called `images`.
2. Download an image and save it in that `images` folder. 
In your code:
3. Load the image into a global variable.
4. Draw the image where you need it.
"""

import arcade


WIDTH = 640
HEIGHT = 480


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...


if __name__ == '__main__':
    setup()
