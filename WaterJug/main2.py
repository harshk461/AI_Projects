import tkinter as tk
from collections import deque

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
JUG_COLOR = 'blue'
BACKGROUND_COLOR = 'white'
FONT_COLOR = 'black'
FONT_SIZE = 16

# Create the main window
root = tk.Tk()
root.title('Water Jug Problem Solver')

# Create a canvas for drawing
canvas = tk.Canvas(root, width=CANVAS_WIDTH,
                   height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

# Create a label for displaying text
label = tk.Label(root, text='', font=(None, FONT_SIZE), fg=FONT_COLOR)
label.pack()


def draw_jugs(jug1, jug2):
    canvas.delete('all')

    # Draw jug 1
    canvas.create_rectangle(100, 100, 150, 100 + jug1 * 100, fill=JUG_COLOR)

    # Draw jug 2
    canvas.create_rectangle(250, 100, 300, 100 + jug2 * 100, fill=JUG_COLOR)

    # Display text
    label.config(text=f'Jug 1: {jug1} liters\nJug 2: {jug2} liters')
    root.update()


def water_jug_bfs(capacity_jug1, capacity_jug2, target_amount):
    visited = set()
    queue = deque()

    queue.append((0, 0))

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        if jug1 == target_amount or jug2 == target_amount:
            label.config(text='Goal reached!')
            root.update()
            return

        next_states = []

        if jug1 < capacity_jug1:
            next_states.append((capacity_jug1, jug2))

        if jug2 < capacity_jug2:
            next_states.append((jug1, capacity_jug2))

        if jug1 > 0:
            next_states.append((0, jug2))

        if jug2 > 0:
            next_states.append((jug1, 0))

        pour_amount = min(jug1, capacity_jug2 - jug2)
        next_states.append((jug1 - pour_amount, jug2 + pour_amount))

        pour_amount = min(jug2, capacity_jug1 - jug1)
        next_states.append((jug1 + pour_amount, jug2 - pour_amount))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                draw_jugs(state[0], state[1])
                root.update()
                root.after(1000)  # Delay for 1 second

    label.config(text='No solution found!')

# Function to start the solving process


def start_solving():
    jug1_capacity = int(jug1_entry.get())
    jug2_capacity = int(jug2_entry.get())
    target_amount = int(target_entry.get())

    water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)


# Create input fields and a solve button
jug1_label = tk.Label(root, text='Jug 1 Capacity:')
jug1_label.pack()
jug1_entry = tk.Entry(root)
jug1_entry.pack()

jug2_label = tk.Label(root, text='Jug 2 Capacity:')
jug2_label.pack()
jug2_entry = tk.Entry(root)
jug2_entry.pack()

target_label = tk.Label(root, text='Target Amount:')
target_label.pack()
target_entry = tk.Entry(root)
target_entry.pack()

solve_button = tk.Button(root, text='Solve', command=start_solving)
solve_button.pack()

root.mainloop()
