import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.sprite1 = arcade.Sprite(center_x=100, center_y=200)
        self.sprite1.texture = arcade.make_soft_square_texture(50,
                                                               arcade.color.BLACK,
                                                               outer_alpha=255)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.sprite1.draw()

    def update(self, delta_time):
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
