import arcade

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.AMAZON)

# Initialize your variables here
x = 50

@window.event("on_draw")
def game_loop():
    global x

    # update your variables here.
    x += 1

    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(x, 100, 25, arcade.color.CREAM)


arcade.run()
