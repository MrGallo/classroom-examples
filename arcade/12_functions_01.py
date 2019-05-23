"""
1. Define a custom function called `draw_face`. Draw a face inside of it.
   Call the `draw_face` function in the `on_draw` function.

Next, make the function re-usable. As it stands, every time you call `draw_face`,
it will draw the face in the same location. We want to be able to draw a face at
any location.

2. Refactor the draw commands of the face with an `x` and `y` variable. Make
   all the draw commands' x and y locations relative to the `x` and `y` variables.
   Change the `x` and `y` values and confirm all the parts of the face are
   properly modified.
3. Turn the `x` and `y` (local) variables into parameter variables in the
   function definition.
4. Call the `draw_face` function multiple times and at different locations
   in the `on_draw` function.
"""

import arcade


WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")


def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()
    draw_face()


def draw_face():
    # face back
    arcade.draw_ellipse_filled(320, 240, 35, 40, arcade.color.YELLOW)

    # left eye
    arcade.draw_ellipse_filled(310, 250, 10, 13, arcade.color.WHITE)
    arcade.draw_ellipse_filled(310, 250, 3, 3, arcade.color.BLACK)

    # right eye
    arcade.draw_ellipse_filled(330, 250, 10, 13, arcade.color.WHITE)
    arcade.draw_ellipse_filled(330, 250, 3, 3, arcade.color.BLACK)

    # mouth
    arcade.draw_ellipse_filled(323, 225, 10, 7, arcade.color.BLACK)
    arcade.draw_ellipse_filled(320, 230, 10, 7, arcade.color.YELLOW)


if __name__ == '__main__':
    setup()
