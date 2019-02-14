import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
# Begin drawing

# Grass
arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, 100, (105, 214, 0))

# Sun
arcade.draw_circle_filled(WIDTH-100, HEIGHT-100, 50, arcade.color.TITANIUM_YELLOW)

# Left tree
arcade.draw_triangle_filled(200-40, 200-75, 200, 200, 200+40, 200-75, arcade.color.BROWN)
arcade.draw_xywh_rectangle_filled(200-10, 200-150, 20, 150-75, arcade.color.DARK_OLIVE_GREEN)

# Middle tree
arcade.draw_triangle_filled(WIDTH-200-40, 200-75, WIDTH-200, 200, WIDTH-200+40, 200-75, arcade.color.BROWN)
arcade.draw_xywh_rectangle_filled(WIDTH-200-10, 200-150, 20, 150-75, arcade.color.DARK_OLIVE_GREEN)

# right tree
arcade.draw_triangle_filled(WIDTH-125-40, 200-75, WIDTH-125, 200, WIDTH-125+40, 200-75, arcade.color.BROWN)
arcade.draw_xywh_rectangle_filled(WIDTH-125-10, 200-150, 20, 150-75, arcade.color.DARK_OLIVE_GREEN)

# End drawing
arcade.finish_render()
arcade.run()
