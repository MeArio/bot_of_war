import win32gui
from PIL import ImageGrab
from PIL import Image
from PIL import ImageOps
from numpy import *

w_name = "Gems of War"
board_box = (207, 71, 595, 566)
tiles_per_row_collumn = 8
colors = {'blue': (49, 208, 103), 'brown': (96, 62, 63),
          'purple': (137, 25, 189), 'red': (203, 41, 52),
          'green': (30, 117, 16), 'yellow': (228, 196, 79)}


# Checks to see if the game is opened.
def window_exists(name):
    if win32gui.FindWindow(None, name) != 0:
        return True
    else:
        return False


def move_window_to_corner(name):
    if win32gui.FindWindow(None, name) != 0:
        win32gui.MoveWindow(hwnd, 0, 0, 800, 600, False)
    else:
        return False


def grab_board(bbox):
    board = ImageGrab.grab(bbox)
    board.save("get.png")
    return board


def crop_board(board):
    width = board.size[0] / tiles_per_row_collumn
    height = board.size[1] / tiles_per_row_collumn
    for y in range(0, tiles_per_row_collumn):
        for x in range(0, tiles_per_row_collumn):
            board.crop((x * width,
                        y * height,
                        (x + 1) * width,
                        (y + 1) * height)).save(str(x) + "," + str(y) + ".png")


def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0] and colour != (0, 0, 0):
            # Lazy fix since green was sometimes giving me the color black
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel


def board_to_array:



'''if window_exists(w_name):
    print("Yeah it does")
    hwnd = win32gui.FindWindow(None, w_name)
    win32gui.MoveWindow(hwnd, 0, 0, 800, 600, False)
    board = grab_board(board_box)
    crop_board(board)
else:
    print("It doesn't or you fucked up")
'''
