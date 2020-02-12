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
