import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.player = arcade.Sprite(":resources:/images/animated_characters/male_adventurer/maleAdventurer_idle.png")
        self.player.center_x = 100
        self.player.center_y = 100

    def on_draw(self):
        arcade.start_render()  # keep as first line
        self.player.draw()


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
