"""
1. Define a custom function called `draw_face`. Draw a face inside of it.
   Call the `draw_face` function in the `on_draw` function.
   [Starter Code]
   (https://github.com/MrGallo/classroom-examples/blob/bafb60c0f7188822263a5c703359648be127b213/arcade/12_functions_01.py)

Next, make the function re-usable. As it stands, every time you call `draw_face`,
it will draw the face in the same location. We want to be able to draw a face at
any location.

2. Refactor the draw commands of the face with an `x` and `y` variable. Make
   all the draw commands' x and y locations relative to the `x` and `y` variables.
   Change the `x` and `y` values and confirm all the parts of the face are
   properly modified.
   [Step 2 Changes]
   (https://github.com/MrGallo/classroom-examples/commit/2bdf945a7e4562d7d8c4ff43a307fb7a935beb33#diff-7e4e0566072fe6add5a463761407d134)

3. Turn the `x` and `y` (local) variables into parameter variables in the
   function definition.
   [Step 3 Changes]
   (https://github.com/MrGallo/classroom-examples/commit/9949effdc353db6065679c083fef4b7ac577b393#diff-7e4e0566072fe6add5a463761407d134)

4. Call the `draw_face` function multiple times and at different locations
   in the `on_draw` function.
   [Step 4 Changes]
   (https://github.com/MrGallo/classroom-examples/commit/808037aa6f3cd510b774060665b0be3ac72b4f77#diff-7e4e0566072fe6add5a463761407d134)
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
    draw_face(320, 240)
    draw_face(100, 50)
    for x in range(0, WIDTH+1, 80):
        draw_face(x, 400)


def draw_face(x, y):
    # face back
    arcade.draw_ellipse_filled(x, y, 35, 40, arcade.color.YELLOW)

    # left eye
    arcade.draw_ellipse_filled(x-10, y+10, 10, 13, arcade.color.WHITE)
    arcade.draw_ellipse_filled(x-10, y+10, 3, 3, arcade.color.BLACK)

    # right eye
    arcade.draw_ellipse_filled(x+10, y+10, 10, 13, arcade.color.WHITE)
    arcade.draw_ellipse_filled(x+10, y+10, 3, 3, arcade.color.BLACK)

    # mouth
    arcade.draw_ellipse_filled(x+3, y-15, 10, 7, arcade.color.BLACK)
    arcade.draw_ellipse_filled(x, y-10, 10, 7, arcade.color.YELLOW)


if __name__ == '__main__':
    setup()
