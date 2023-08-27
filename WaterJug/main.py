from tkinter import *
import time
from collections import deque

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


def water_jug_bfs(capacity_jug1, capacity_jug2, target_amount):
    # Initialize the visited set to keep track of visited states
    visited = set()

    # Create a queue for BFS
    queue = deque()

    # Initialize with the initial state (0, 0)
    queue.append((0, 0))

    while queue:
        # Get the current state from the queue
        current_state = queue.popleft()
        jug1, jug2 = current_state

        # Check if the goal is reached
        if jug1 == target_amount or jug2 == target_amount:
            print("Goal reached!")
            return

        # Generate possible next states
        next_states = []

        # Fill jug 1 if it's empty
        if jug1 < capacity_jug1:
            next_states.append((capacity_jug1, jug2))

        # Fill jug 2 if it's empty
        if jug2 < capacity_jug2:
            next_states.append((jug1, capacity_jug2))

        # Empty jug 1
        if jug1 > 0:
            next_states.append((0, jug2))

        # Empty jug 2
        if jug2 > 0:
            next_states.append((jug1, 0))

        # Pour from jug 1 to jug 2
        pour_amount = min(jug1, capacity_jug2 - jug2)
        next_states.append((jug1 - pour_amount, jug2 + pour_amount))

        # Pour from jug 2 to jug 1
        pour_amount = min(jug2, capacity_jug1 - jug1)
        next_states.append((jug1 + pour_amount, jug2 - pour_amount))

        # Add unvisited next states to the queue
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution found!")


# Example usage:
water_jug_bfs(4, 3, 2)

# main(4, 3, 2)
