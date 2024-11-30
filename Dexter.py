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

pygame.mixer.music.load("suprise.mp3")

pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

pygame.mixer.music.queue("Dexter.mp3")
##testing






syringe = tkinter.PhotoImage(file="syringe.png")
syringe_x = 0
syringe_y = 0
syringes = []

dexter = tkinter.PhotoImage(file="Dex.png")
dexter_x = 0
dexter_y = 0

doakes = tkinter.PhotoImage(file="Doakes.png")
doakes_x = 0
doakes_y = 0
james = []


over = tkinter.PhotoImage(file="over.png")




def move(e):
    global dexter_x, dexter_y, syringe_x, syringe_y, syringes
    
    if(e.keysym == "Up"):
        dexter_y = dexter_y - (.3 * TILE_SIZE)

    elif(e.keysym == "Down"):
        dexter_y = dexter_y + (.3 * TILE_SIZE)

    elif (e.keysym == "space" ):
        syringe_x = dexter_x + 10
        syringe_y = dexter_y + 60
        syringes.append([syringe_x, syringe_y])
        
        
    

    
    
temp = 0
#0 going down
#1 going up

def draw():
    global dexter, temp, syringe_x, syringe_y
    canvas.delete("all")
    james.append([doakes_x + (23 * TILE_SIZE), doakes_y + (12 * TILE_SIZE)])

    canvas.create_image(dexter_x + (5 * TILE_SIZE) , dexter_y + (5 * TILE_SIZE), image=dexter)
    canvas.create_image(james[0][0] , james[0][1], image=doakes)

    if temp == 0 :
        james[0][1] += 1.5 * TILE_SIZE
        if james[0][1] == 637.5:
            temp = 1
    
    if temp == 1 :
        james[0][1] -= 1.5 * TILE_SIZE
        if james[0][1] == 75:
            temp = 0
    
    print("james: " + str(james[0][1]) + " Range: " + str(james[0][1] - 140) + " " + str(james[0][1] -160))
    


    for syringez in syringes:
        
        canvas.create_image(syringez[0] + (5 * TILE_SIZE) , syringez[1] + (5 * TILE_SIZE), image=syringe)
        if syringez[0] <= (19 * TILE_SIZE):
            syringez[0] += 3 * TILE_SIZE  # Move right by one tile
        if syringez[0] > (19 * TILE_SIZE):
            syringes.remove(syringez)
        print("syringe: " + str(syringez[1]))
        if (syringez[0] > 460 and 
            syringez[1] < (james[0][1] - 129) and
            syringez[1] > (james[0][1] - 181)):
        

            
            window.after(2000, end_game())
            #window.quit()
        
        

    

    
    window.after(100, draw)


    
    
    


def end_game():
    
    window.quit()
draw()
window.bind("<KeyPress>", move)
window.mainloop()