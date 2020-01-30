import random

import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.player = arcade.Sprite(center_x=100, center_y=100)
        self.player.texture = arcade.make_soft_square_texture(50, arcade.color.BLUE, outer_alpha=255)

        self.enemy_texture = arcade.make_soft_square_texture(50, arcade.color.RED, outer_alpha=255)
        self.enemies = arcade.SpriteList()

        # create an enemy
        for _ in range(3):
            enemy = arcade.Sprite()
            enemy.center_x = random.randrange(0, WIDTH)
            enemy.center_y = random.randrange(HEIGHT//2, HEIGHT)
            enemy.texture = self.enemy_texture
            self.enemies.append(enemy)

        self.laser_texture = arcade.make_soft_square_texture(30, arcade.color.ORANGE, outer_alpha=255)
        self.lasers = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.player.draw()
        self.enemies.draw()
        self.lasers.draw()

    def update(self, delta_time):
        self.lasers.update()

        for enemy in self.enemies:
            lasers_in_contact = enemy.collides_with_list(self.lasers)
            if lasers_in_contact:
                enemy.kill()
                for laser in lasers_in_contact:
                    laser.kill()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.player.center_x = x
        self.player.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        laser = arcade.Sprite()
        laser.center_x = self.player.center_x
        laser.center_y = self.player.center_y
        laser.change_y = 3
        laser.texture = self.laser_texture
        laser.width = 5

        self.lasers.append(laser)


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
