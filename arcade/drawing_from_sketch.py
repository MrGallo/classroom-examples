import arcade


WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Grass
    arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, 100, (105, 214, 0))

    # Sun
    arcade.draw_circle_filled(WIDTH - 100, HEIGHT - 100, 50, arcade.color.TITANIUM_YELLOW)

    # Left tree
    arcade.draw_triangle_filled(200 - 40, 200 - 75, 200, 200, 200 + 40, 200 - 75, arcade.color.BROWN)
    arcade.draw_xywh_rectangle_filled(200 - 10, 200 - 150, 20, 150 - 75, arcade.color.DARK_OLIVE_GREEN)

    # Middle tree
    arcade.draw_triangle_filled(WIDTH - 200 - 40, 200 - 75, WIDTH - 200, 200, WIDTH - 200 + 40, 200 - 75,
                                arcade.color.BROWN)
    arcade.draw_xywh_rectangle_filled(WIDTH - 200 - 10, 200 - 150, 20, 150 - 75, arcade.color.DARK_OLIVE_GREEN)

    # right tree
    arcade.draw_triangle_filled(WIDTH - 125 - 40, 200 - 75, WIDTH - 125, 200, WIDTH - 125 + 40, 200 - 75,
                                arcade.color.BROWN)
    arcade.draw_xywh_rectangle_filled(WIDTH - 125 - 10, 200 - 150, 20, 150 - 75, arcade.color.DARK_OLIVE_GREEN)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Drawing")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
