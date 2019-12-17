"""
Arcade Sprites are created to use images. Often times, you do not have images
and drawing shapes can be really slow. One work around is to create a texture
with one of arcade's built-in functions and assign that texture to a sprite
you create.
"""
import random

import arcade

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        circle_texture = arcade.make_circle_texture(50, arcade.color.BLUE)
        square_texture = arcade.make_soft_square_texture(50,
                                                         arcade.color.ORANGE,
                                                         outer_alpha=255)

        self.sprites = arcade.SpriteList()
        for _ in range(1000):
            x, y = random.randrange(WIDTH), random.randrange(HEIGHT)
            sprite = arcade.Sprite(center_x=x, center_y=y)
            dx = random.randrange(-3, 3)
            dy = random.randrange(-3, 3)
            sprite.change_x = dx
            sprite.change_y = dy
            if random.randrange(2) == 0:  # circle texture
                sprite.texture = circle_texture
            else:  # square texture
                sprite.texture = square_texture
            self.sprites.append(sprite)

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        self.sprites.draw()

    def update(self, delta_time):
        self.sprites.update()

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
