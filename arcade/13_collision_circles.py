"""
Determine if two circles are close enough that
they are considered 'touching'.

Basically:
- Two circles have an (x,y) location and a radius.
- Find distance between two points.
- If the distance is less than the two radii, they are
  'touching'.
"""


import arcade


WIDTH = 640
HEIGHT = 480

# Make the circles exist. What info we we need to store about them?
# position
# radius
#         x,  y,  r
ball_1 = [50, 50, 30]
ball_2 = [100, 50, 60]


def update(delta_time):
    pass
    # check if collision
        # print message


def on_draw():
    arcade.start_render()
    # Draw ball 1
    arcade.draw_circle_filled(ball_1[0], ball_1[1], ball_1[2], arcade.color.RED)

    # Draw ball 2
    arcade.draw_circle_filled(ball_2[0], ball_2[1], ball_2[2], arcade.color.BLUE)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
