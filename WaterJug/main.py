from tkinter import *
import time

width = 400
height = 400

root = Tk()

frame = Canvas(root, width=width, height=height, background="#000")
frame.pack()

label = Label(root, text="", font=(None, 16), foreground="blue")
label.pack()


def createJug(jug1, jug2):
    frame.delete('all')

    frame.create_rectangle(100, 100, 150, 100+jug1*100, fill="blue")
    frame.create_rectangle(250, 100, 300, 100+jug2*100, fill="yellow")

    label.config(text=f'Jug 1: {jug1} liters\nJug 2: {jug2} liters')
    root.update()
    time.sleep(1)


def main(capacity_jug_1, capacity_jug_2, target):
    jug1 = 0
    jug2 = 0

    while jug1 != target and jug2 != target:
        # fill jug1
        if jug1 == 0:
            jug1 = capacity_jug_1
            createJug(jug1, jug2)

        # pour water from jug1 to jug2
        amount = min(jug1, capacity_jug_2-jug2)
        jug1 -= amount
        jug2 += amount
        createJug(jug1, jug2)

        if (jug2 == capacity_jug_2):
            jug2 = 0
            createJug(jug1, jug2)
    label.config(text=f"Reached at {target}")
    root.mainloop()


main(4, 3, 2)
