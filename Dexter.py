import tkinter
import pygame
import pygame.mixer


ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS


window = tkinter.Tk()
window.title("tonights the night")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "navy blue", width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
canvas.pack()
window.update()

pygame.mixer.init()
pygame.mixer.music.load("Dexter.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
##testing







dexter = tkinter.PhotoImage(file="Dex.png")
dexter_x = 0
dexter_y = 0

doakes = tkinter.PhotoImage(file="Doakes.png")
doakes_x = 0
doakes_y = 0

def move(e):
    global dexter_x, dexter_y
    
    if(e.keysym == "Up"):
        dexter_y = dexter_y - TILE_SIZE

    if(e.keysym == "Down"):
        dexter_y = dexter_y + TILE_SIZE

    if(e.keysym == "Left"):
        dexter_x = dexter_x - TILE_SIZE

    if(e.keysym == "Right"):
        dexter_x = dexter_x + TILE_SIZE

    
    
        



def draw():
    global dexter
    canvas.delete("all")
    canvas.create_image(dexter_x + (5 * TILE_SIZE) , dexter_y + (5 * TILE_SIZE), image=dexter)
    canvas.create_image(doakes_x + (23 * TILE_SIZE) , doakes_y + (12 * TILE_SIZE), image=doakes)
    window.after(100, draw)



draw()
window.bind("<KeyPress>", move)
window.mainloop()