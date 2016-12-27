import win32gui
from PIL import ImageGrab
from PIL import Image
from PIL import ImageOps
import numpy as np

w_name = "Gems of War"
board_box = (207, 71, 595, 566)
tiles_per_row_collumn = 8

colors = {(49, 128, 203): 'blue',
          (96, 62, 63): 'brown',
          (137, 25, 189): 'purple',
          (203, 41, 52): 'red',
          (30, 117, 16): 'green',
          (228, 196, 79): 'yellow',
          (255, 255, 255): 'skull'}


tiles = {'blue': 0,
         'brown': 1,
         'purple': 2,
         'red': 3,
         'green': 4,
         'yellow': 5,
         'skull': 6}


# Checks to see if the game is opened.
def window_exists(name):
    if win32gui.FindWindow(None, name) != 0:
        return True
    else:
        return False


def move_window_to_corner(name):
    try:
        win32gui.MoveWindow(win32gui.FindWindow(None, name), 0, 0, 800, 600,
                            False)
    except win32gui.error:
        return False


def grab_board(bbox):
    board = ImageGrab.grab(bbox)
    board.save("get.png")
    return board


def crop_board(board):
    board_tiles = np.empty((tiles_per_row_collumn, tiles_per_row_collumn),
                           dtype='object')
    width = board.size[0] / tiles_per_row_collumn
    height = board.size[1] / tiles_per_row_collumn
    for y in range(0, tiles_per_row_collumn):
        for x in range(0, tiles_per_row_collumn):
            board_tiles[x, y] = board.crop((x * width,
                                            y * height,
                                            (x + 1) * width,
                                            (y + 1) * height))

    return board_tiles


def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0] and colour != (0, 0, 0):
            # Lazy fix since green was sometimes giving me the color black
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel


def board_to_array(image_tiles):
    board = np.zeros((tiles_per_row_collumn, tiles_per_row_collumn))
    x = 0
    y = 1
    for coords, value in np.ndenumerate(image_tiles):
        board[coords[x], coords[y]] = tiles[colors[most_frequent_colour(value)[1]]]
        print(coords[x], coords[y])

    return board
