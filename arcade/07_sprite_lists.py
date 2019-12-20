import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.player = arcade.Sprite(center_x=100, center_y=100)
        self.player.texture = arcade.make_soft_square_texture(50, arcade.color.BLUE, outer_alpha=255)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()

    def update(self, delta_time):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.player.center_x = x
        self.player.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):

        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
