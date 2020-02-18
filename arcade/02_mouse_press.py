"""
Check for a mouse click on a circle.

- Draw a circle somewhere, using circle_x and circle_y, circle_radius variables.

"""

import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.AMAZON)

# Initialize your variables here
circle_x = WIDTH//2
circle_y = HEIGHT//2
circle_radius = 100

@window.event("on_draw")
def game_loop():
    # import global variables here.

    # update your variables here.

    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(circle_x, circle_y, circle_radius, arcade.color.WHITE)


arcade.run()
