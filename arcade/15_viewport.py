"""
Move viewport (camera) to follow player
"""


import arcade


WIDTH = 640
HEIGHT = 480

player_loc = [0, 0]
MOVEMENT_SPEED = 5

keys_pressed = {
    arcade.key.UP: False,
    arcade.key.DOWN: False,
    arcade.key.LEFT: False,
    arcade.key.RIGHT: False
}


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.set_viewport(-WIDTH/2, WIDTH/2, -HEIGHT/2, HEIGHT/2)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


def update(delta_time):
    if keys_pressed[arcade.key.RIGHT]:
        player_loc[0] += MOVEMENT_SPEED
    elif keys_pressed[arcade.key.LEFT]:
        player_loc[0] -= MOVEMENT_SPEED

    if keys_pressed[arcade.key.UP]:
        player_loc[1] += MOVEMENT_SPEED
    elif keys_pressed[arcade.key.DOWN]:
        player_loc[1] -= MOVEMENT_SPEED

    # Move the viewport according to where the player is.
    arcade.set_viewport(-WIDTH/2 + player_loc[0],
                        WIDTH/2 + player_loc[0],
                        -HEIGHT/2 + player_loc[1],
                        HEIGHT/2 + player_loc[1])


def on_draw():
    arcade.start_render()

    # Draw player
    arcade.draw_circle_filled(player_loc[0], player_loc[1], 25, arcade.color.BLUE)

    # Display specific locations. To prove the player is actually moving.
    # Notice how this text 'moves' on the screen. This might be confusing.
    # It's actually the player and the viewport (camera) that is moving.
    # The text is actually drawing at the same location every time.

    arcade.draw_text("(100, 100)", 100, 100, arcade.color.BLACK)
    arcade.draw_text("(100, -100)", 100, -100, arcade.color.BLACK)
    arcade.draw_text("(-100, -100)", -100, -100, arcade.color.BLACK)
    arcade.draw_text("(-100, 100)", -100, 100, arcade.color.BLACK)
    arcade.draw_text("(0, 0)", 0, 0, arcade.color.BLACK)


def on_key_press(key, modifiers):
    global keys_pressed
    keys_pressed[key] = True


def on_key_release(key, modifiers):
    global keys_pressed
    keys_pressed[key] = False


if __name__ == '__main__':
    setup()
