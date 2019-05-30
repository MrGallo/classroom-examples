"""
Importing and drawing images.
1. In the folder that contains your code, create a folder called `images`.
2. Download an image and save it in that `images` folder. 
In your code:
3. Load the image into a global variable.
4. Draw the image where you need it.
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

# Load image into a global variable
# WARNING: Do NOT load images within update or on_draw.
tile_img = arcade.load_texture('images/platformPack_tile001.png')


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

    # http://arcade.academy/arcade.html?highlight=draw_texture#arcade.draw_texture_rectangle
    arcade.draw_texture_rectangle(100, 200, tile_img.width, tile_img.height, tile_img)


if __name__ == '__main__':
    setup()
