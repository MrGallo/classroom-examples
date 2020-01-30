import arcade

WIDTH = 800
HEIGHT = 600


class Dart(arcade.Sprite):
    def __init__(self, center_x: int, center_y: int, owner: 'Player'):
        super().__init__(center_x=center_x, center_y=center_y)
        self.texture = arcade.make_soft_square_texture(20, arcade.color.ORANGE, outer_alpha=255)
        self.target_queue = []
        self.current_target = None
        self.owner = owner

    def update(self):
        print(f"{self.target_queue=}")
        print(f"{self.current_target=}")
        if self.current_target:
            x, y = self.current_target

            error_x = x - self.center_x
            error_y = y - self.center_y

            if abs(error_x) < 1 and abs(error_y) < 1:
                try:
                    self.current_target = self.target_queue.pop(0)
                except IndexError:
                    self.current_target = None
                return

            # proportional
            self.change_x = 0.2 * error_x
            self.change_y = 0.2 * error_y
        else:
            if self.target_queue:
                self.current_target = self.target_queue.pop(0)
            else:
                self.current_target = (self.owner.center_x, self.owner.center_y)


        super().update()


class Player(arcade.Sprite):
    def draw(self):
        super().draw()
        self.dart.draw()

    def update(self):
        super().update()
        self.dart.update()


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.player = Player(center_x=50, center_y=50)
        self.player.texture = arcade.make_soft_square_texture(50, arcade.color.BLUE, outer_alpha=255)
        self.player.dart = Dart(self.player.center_x, self.player.center_y, self.player)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()

    def update(self, delta_time):
        self.player.update()

    def on_mouse_press(self, x, y, button, key_modifiers):
        self.player.dart.target_queue.append((x, y))


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
