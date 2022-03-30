# This program moves a character fully throughout a 2D list.
# First component is the x dimension and the second is the y dimension both starting from bottom left and 0

import tkinter as tk
from tkinter import ttk
from Prandom import prandom
import tkinter.font as tkFont


def cmd_enemytoggle():
    global enemyToggleBtn
    global enemyToggle

    if enemyToggle == 0:
        enemyToggle = 1
        enemyToggleBtn.config(text="Enemy Off ")
    elif enemyToggle == 1:
        enemyToggle = 0
        enemyToggleBtn.config(text="Enemy On")


def cmd_left():
    if (char_location[0 and 1] >= 0) and (char_location[0 and 1] <= 9):
        if char_location[1] != 0:
            char_location[1] = char_location[1] - 1
            update_list()
            if gameOver == 0:
                print_2d()


def cmd_right():
    if (char_location[0 and 1] >= 0) and (char_location[0 and 1] <= 9):
        if char_location[1] != 9:
            char_location[1] = char_location[1] + 1
            update_list()
            if gameOver == 0:
                print_2d()


def cmd_up():
    if (char_location[0 and 1] >= 0) and (char_location[0 and 1] <= 9):
        if char_location[0] != 0:
            char_location[0] = char_location[0] - 1
            update_list()
            if gameOver == 0:
                print_2d()


def cmd_down():
    if (char_location[0 and 1] >= 0) and (char_location[0 and 1] <= 9):
        if char_location[0] != 9:
            char_location[0] = char_location[0] + 1
            update_list()
            if gameOver == 0:
                print_2d()


def update_list():
    global game_list
    global gameOver
    game_list = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    if char_location[0 or 1] > 9 or char_location[0 or 1] < 0:
        print("Game Over!")
        root.destroy()
        intro.destroy()
        gameview.destroy()
        gameOver = 1

    if char_location[0] == enemy_location[0] and char_location[1] == enemy_location[1]:
        print("Game Over!")
        root.destroy()
        intro.destroy()
        gameview.destroy()

    if char_location[0] > enemy_location[0] and char_location[1] > enemy_location[1]:
        print("Enemy Top-left of char")
#        if (char_location[0] - enemy_location[0]):


    if char_location[0] < enemy_location[0] and char_location[1] > enemy_location[1]:
        print("Enemy Bottom-left of char")
        if (char_location[0] - enemy_location[0]) < (enemy_location[1] - char_location[1]):
            print("Enemy Going Up")
            if enemyToggle == 1:
                enemy_location[0] = enemy_location[0] - 1
        if (enemy_location[0] - char_location[0]) > (enemy_location[1] - char_location[1]):
            print("Enemy Going Right")
            if enemyToggle == 1:
                enemy_location[1] = enemy_location[1] + 1

    if char_location[0] > enemy_location[0] and char_location[1] < enemy_location[1]:
        print("Enemy Top-right of char")

    if char_location[0] < enemy_location[0] and char_location[1] < enemy_location[1]:
        print("Enemy Bottom-right of char")

    if char_location[0] == enemy_location[0] and char_location[1] < enemy_location[1]:
        print("Enemy Middle-right of char")

    if char_location[0] == enemy_location[0] and char_location[1] > enemy_location[1]:
        print("Enemy Middle-left of char")

    if char_location[1] == enemy_location[1] and char_location[0] < enemy_location[0]:
        print("Enemy Middle-bottom of char")

    if char_location[1] == enemy_location[1] and char_location[0] > enemy_location[0]:
        print("Enemy Middle-top of char")

    if gameOver == 0:
        game_list[char_location[0]][char_location[1]] = '@'
        game_list[enemy_location[0]][enemy_location[1]] = 'C'


def print_2d():
    global gameViewList
    global gameLabel
    gameViewList = ""
    for x in range(0, 10):
        gameViewList = gameViewList + str(game_list[x]) + "\n"
    gameLabel.config(text=gameViewList)


char_location = [1, 4]
enemy_location = [3, 4]
gameOver = 0
gameViewList = ""
enemyToggle = 0

game_list = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '@', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]


intro = tk.Tk()
intro.title("ASCII Dash")
intro.geometry("355x204+500+25")
intro.resizable(False, False)
intro.attributes("-alpha", 1)
intro.attributes("-topmost", 1)
# Make the background image
introBgImageTemp = tk.PhotoImage(file="/home/eduard/Documents/Code/Python/2Dgame/mybackground.gif")
introBgImage = tk.Label(intro, image=introBgImageTemp).place(x="1", y="1")
# Make the label containing the name
nameLabelFont = tkFont.Font(family="Ubuntu Mono", slant="italic", weight="bold", size=22)
nameLabel = tk.Label(intro, text="Welcome To ASCII Dash", bg="green4", font=nameLabelFont).place(x="20", y="30")
# Make the introductory label
introLabelFont = tkFont.Font(family="Ubuntu Mono", size=12)
introLabel = tk.Label(intro, text="Welcome to ASCII Dash. An ascii\ntext based game featuring your player\nand a full functioning enemy.", font=introLabelFont, bg="green4").place(x="30", y="80")


root = tk.Tk()
root.title("ASCII Dash Controls")
root.geometry("200x200+600+350")
root.resizable(False, False)
root.attributes("-alpha", 1)
root.attributes("-topmost", 1)
# Make the buttons
left = ttk.Button(root, text="Left", command=cmd_left)
right = ttk.Button(root, text="Right", command=cmd_right)
up = ttk.Button(root, text="A", command=cmd_up)
down = ttk.Button(root, text="Down", command=cmd_down)
enemyToggleBtn = ttk.Button(root, text="Enemy On", command=cmd_enemytoggle)
enemyToggleBtn.place(x="60", y="165")
left.place(x="15", y="80")
right.place(x="100", y="80")
up.place(x="60", y="50")
down.place(x="60", y="110")


gameview = tk.Tk()
gameview.title("ASCII Dash Game View")
gameview.geometry("400x400+50+250")
gameview.resizable(False, False)
gameview.attributes("-alpha", 1)
gameview.attributes("-topmost", 1)
gameLabelFont = tkFont.Font(family="Ubuntu Mono", size=60)
gameLabel = tk.Label(gameview, text=gameViewList, font=gameLabelFont, height=60, width=50)
gameLabel.pack()

print_2d()

root.mainloop()
intro.mainloop()
gameview.mainloop()