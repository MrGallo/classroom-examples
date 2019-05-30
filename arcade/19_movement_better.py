"""
Using built-in key-press tracking.
Continuing from 07_player_movement.py
"""

from pyglet.window.key import KeyStateHandler
import arcade


WIDTH = 640
HEIGHT = 480

# start player position in middle of window
player_x = WIDTH/2
player_y = HEIGHT/2

# A defaultdict that holds the key presses
keys_pressed = KeyStateHandler()


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.push_handlers(keys_pressed)

    arcade.run()


def update(delta_time):
    global player_y
    if keys_pressed[arcade.key.UP]:
        player_y += 5


def on_draw():
    global player_x, player_y
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.BLUE)


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
