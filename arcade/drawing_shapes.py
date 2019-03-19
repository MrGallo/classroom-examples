import arcade


WIDTH = 640
HEIGHT = 480


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...

    # Circle
    arcade.draw_circle_outline(320, 240, 25, arcade.color.BLUE, 5)
    # Ellipse
    arcade.draw_ellipse_filled(100, 100, 50, 100, arcade.color.RED)
    # Rectangle
    arcade.draw_xywh_rectangle_filled(300, 20, 300, 50, arcade.color.ORANGE_PEEL)
    # Triangle
    arcade.draw_triangle_outline(50, 50, 100, 100, 150, 50, arcade.color.WHITE, 15)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
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
