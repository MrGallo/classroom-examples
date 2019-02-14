import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(50, 50, 30, arcade.color.BLUE_GREEN)

# End drawing
arcade.finish_render()
arcade.run()
