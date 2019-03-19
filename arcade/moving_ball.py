import arcade


WIDTH = 640
HEIGHT = 480

x = 50
y = 50


def update(delta_time):
    global x
    x = x + 3
    print(x)

    if x > 300:
        x = 0


def on_draw():
    global x
    arcade.start_render()
    arcade.draw_circle_filled(x, y, 40, arcade.color.RED)


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
