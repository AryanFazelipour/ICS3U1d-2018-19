import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions

def draw_clouds():
    arcade.draw_rectangle_filled(300,400, 100, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 400, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(250, 410, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(340, 410, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 440, 30, arcade.color.WHITE)

def draw_rollinghills():
    arcade.draw_ellipse_filled(0 , 300, 300, 300, arcade.color.BRIGHT_GREEN)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()
    draw_clouds()
    draw_rollinghills()
   # call your draw functions

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()