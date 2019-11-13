"""Need to create a default dict to store pressed/released values"""

# First, import defaultdict
from collections import defaultdict
import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        # Next, create a dict to store key presses.
        self.keys_pressed = defaultdict(bool)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        arcade.draw_circle_filled(100, 100, 25, arcade.color.BLUE)
        print(self.keys_pressed)  # print out the state of your key dict

    def update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        self.keys_pressed[key] = True

    def on_key_release(self, key, key_modifiers):
        self.keys_pressed[key] = False


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()