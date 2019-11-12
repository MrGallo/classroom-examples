import arcade


WIDTH = 640
HEIGHT = 480


class Sprite:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 25, arcade.color.BLUE)


window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")

player = Sprite(200, 200)

def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    player.x += 1
    player.y += 1


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
