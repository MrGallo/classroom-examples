import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.SKY_BLUE)

# Initialize your variables here

@window.event("on_draw")
def game_loop():
    # import global variables here.

    # update your variables here.

    # Draw things here.
    arcade.start_render()
    x = 100
    y = 400
    arcade.draw_circle_filled(x, y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x+25, y-25, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x-35, y-25, 25, arcade.color.WHITE)

    arcade.draw_line(200, 200, 300, 300, arcade.color.RED, 10)


arcade.run()
