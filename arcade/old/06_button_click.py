"""
Button Click

1. Figure out how you want to represent a button. Create global variable(s)
   for it.
2. Draw the button using the information stored in the button's variable(s).
3. In the on_mouse_press function, compare the mouse x and mouse y values to
   the values of the button to determine if there was a click or not.
"""

import arcade


WIDTH = 640
HEIGHT = 480

# Key for button index values
# This makes dealing with buttons as lists slightly easier.
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6

# You might want to Google:
# - python namedtuple
# - python classes
# Those would be better ways to store objects like our button.
button1 = [200, 200, 300, 50, False, arcade.color.BLUE, arcade.color.GREEN]


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
    window.on_mouse_release = on_mouse_release

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...

    # Select the appropriate color to draw with
    if button1[BTN_IS_CLICKED]:
        color = button1[BTN_CLICKED_COLOR]
    else:
        color = button1[BTN_COLOR]

    # Draw button1
    arcade.draw_xywh_rectangle_filled(button1[BTN_X],
                                      button1[BTN_Y],
                                      button1[BTN_WIDTH],
                                      button1[BTN_HEIGHT],
                                      color)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    print(f"Click at ({x}, {y})")

    # Check if click happened on button1 
    if (x > button1[BTN_X] and x < button1[BTN_X] + button1[BTN_WIDTH] and
            y > button1[BTN_Y] and y < button1[BTN_Y] + button1[BTN_HEIGHT]):
        button1[BTN_IS_CLICKED] = True


def on_mouse_release(x, y, button, modifiers):
    # When you let go of the mouse, all buttons should be set to False.
    button1[BTN_IS_CLICKED] = False


if __name__ == '__main__':
    setup()
