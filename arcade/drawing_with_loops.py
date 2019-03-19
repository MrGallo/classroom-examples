"""
The goal is to use a for loop to draw a row of pine trees on the window.
Follow the steps in order.
1. With arcade, draw one pine tree. A sketch might help cut down your guess-and-check time.
    Pine tree:
        - Brown triangle on the top
        - Dark green rectangle as the trunk

2. Factor out variables for the tree's x and y positions.
   When you change any of the x or y variable values, the WHOLE tree should move without distorting.
   Example - Before:
        arcade.draw_circle_filled(50, 50, 25, arcade.color.BLUE)
        arcade.draw_circle_filled(70, 70, 25, arcade.color.BLUE)
   Example - After:
        x = 50
        y = 50
        arcade.draw_circle_filled(x, y, 25, arcade.color.BLUE)
        arcade.draw_circle_filled(x+20, y+20, 25, arcade.color.BLUE)

3. Now determine roughly where on the screen you want to start your row of trees.
    - Write down the start coordinate (x and y).
    - Write down the end coordinate.
    - Write down how many pixels apart you want them.

4. Create a for loop that will iterate over a range() from your start point,
   to your end point, increasing by the amount of pixels they are apart.
   Place your tree code in the loop and use the loop variable as your tree's x location.
"""


import arcade


WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


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


if __name__ == '__main__':
    setup()
