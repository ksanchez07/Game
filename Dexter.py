import tkinter
import pygame
import pygame.mixer

ROWS = 25
COLS = 25
TITLE_SIZE = 25

WINDOW_WIDTH = TITLE_SIZE * ROWS
WINDOW_HEIGHT = TITLE_SIZE * COLS


window = tkinter.Tk()
window.title("tonights the night")
window.resizable(False, False)


##the lines above are code online to make the window, after this it is our work
canvas = tkinter.Canvas(window, bg = "navy blue", width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
canvas.pack()
window.update()
pygame.mixer.init()
pygame.mixer.music.load("Dexter.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()


window.mainloop()
