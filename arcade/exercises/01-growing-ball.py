"""
Start with the base arcade template: https://raw.githubusercontent.com/MrGallo/classroom-examples/master/arcade/arcade_template.py

Do the following as was shown last class. You may use my example as a REFERENCE. Do not copy and paste it!:
- Draw a circle somewhere, using circle_x and circle_y, circle_radius variables.
    - Initialize the variables on the GLOBAL level (not in teh game_loop function).
- Add the def on_mouse_press() function/event handler. Use the on_mouse_pressed event handler to register a click.
- Print out the mouse_x and mouse_y values in the on_mouse_press function.

Once this is accomplished, do the following.
- Make the circle grow every time a click happens.
    - Using the global variable for the circle's radius, increase the value in the on_mouse_press function.
- Make the circle grow only if the mouse is clicked WITHIN the circle.
  You need to use the global circle x, y variables with the mouse x and y variables and use the Pythagorean theorem.
  Google search: python how to calculate square root.

From here you can do many things:
- have the ball move around and try to click it.
- Every time the ball is clicked, reset its position randomly. Google: python generate random number
- When you click the ball, shrink it to a particular value, then change its position, resetting its size.
- Create a global variable for the user's score that is increased every time the ball is clicked. Display
  the score using arcade.draw_text().
- You could also keep track of the accuracy of the clicks by tracking all clicks that missed the ball.
"""

import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.AMAZON)

# Initialize your variables here

@window.event("on_draw")
def game_loop():
    # import global variables here.

    # update your variables here.

    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(100, 100, 25, arcade.color.CREAM)


arcade.run()
