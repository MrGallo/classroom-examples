import arcade


WIDTH = 640
HEIGHT = 480


class Sprite:
    def __init__(self, x: int, y: int, x_speed: int = 0, y_speed: int = 0):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 25, arcade.color.BLUE)


window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")

player = Sprite(200, 200, 1, 1)

def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    player.x += player.x_speed
    player.y += player.y_speed


@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    player.draw()


@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
