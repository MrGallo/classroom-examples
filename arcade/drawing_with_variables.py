import arcade


WIDTH = 640
HEIGHT = 480

# Get user input for x, y and radius.
x = int(input("Enter x location: "))
y = int(input("Enter y location: "))
radius = int(input("Enter radius: "))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.DEEP_PEACH)

# End drawing
arcade.finish_render()
arcade.run()
