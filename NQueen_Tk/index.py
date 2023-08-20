# import tkinter as tk
# import time
# from itertools import cycle
# from threading import Thread
# from queue import Queue

# class NQueensVisualizer:
#     def __init__(self, root, n):
#         self.root = root
#         self.n = n
#         self.board = [[0 for _ in range(n)] for _ in range(n)]
#         self.solutions = []
#         self.solution_index = 0

#         self.canvas = tk.Canvas(root, width=n*50, height=n*50)
#         self.canvas.pack()
#         self.queue = Queue()

#         self.solve_n_queens()
#         self.display_solutions()

#     def is_safe(self, row, col):
#         for i in range(col):
#             if self.board[row][i] == 1:
#                 return False

#         for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
#             if self.board[i][j] == 1:
#                 return False

#         for i, j in zip(range(row, self.n), range(col, -1, -1)):
#             if self.board[i][j] == 1:
#                 return False

#         return True

#     def solve_n_queens_util(self, col):
#         if col >= self.n:
#             self.solutions.append([row[:] for row in self.board])
#             return

#         for i in range(self.n):
#             if self.is_safe(i, col):
#                 self.board[i][col] = 1
#                 self.solve_n_queens_util(col + 1)
#                 self.board[i][col] = 0

#     def solve_n_queens(self):
#         self.solve_n_queens_util(0)

#     def display_solution(self, solution):
#         self.canvas.delete("all")
#         cell_size = 50

#         for row in range(self.n):
#             for col in range(self.n):
#                 color = "white" if (row + col) % 2 == 0 else "black"
#                 self.canvas.create_rectangle(col * cell_size, row * cell_size,
#                                              (col + 1) * cell_size, (row + 1) * cell_size,
#                                              fill=color)

#                 if solution[row][col] == 1:
#                     self.canvas.create_oval(col * cell_size, row * cell_size,
#                                             (col + 1) * cell_size, (row + 1) * cell_size,
#                                             fill="red")

#         self.root.update()

#     def display_solutions(self):
#         for solution in self.solutions:
#             self.queue.put(solution)

#         def display_worker():
#             for solution in cycle(self.solutions):
#                 self.display_solution(solution)
#                 time.sleep(0.3)

#         Thread(target=display_worker, daemon=True).start()

# def main():
#     n = 8
#     root = tk.Tk()
#     root.title(f"N-Queens Solver (N = {n})")
#     app = NQueensVisualizer(root, n)
#     root.mainloop()

# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import messagebox


class NQueensSolver:
    def __init__(self, root, n):
        self.root = root
        self.n = n
        self.canvas = tk.Canvas(root, width=n * 50, height=n * 50)
        self.canvas.pack()
        self.solutions = []
        self.board = [[0] * n for _ in range(n)]  # Initialize the board
        self.find_solutions(0)

    def is_safe(self, board, row, col):
        # Check if it's safe to place a queen at board[row][col]
        for i in range(col):
            if board[row][i] == 1:
                return False
            if row - i >= 0 and board[row - i][col - i] == 1:
                return False
            if row + i < self.n and board[row + i][col - i] == 1:
                return False
        return True

    def find_solutions(self, col):
        if col == self.n:
            # Found a solution, add it to the list
            self.solutions.append([row[:] for row in self.board])
            return

        for row in range(self.n):
            if self.is_safe(self.board, row, col):
                self.board[row][col] = 1
                self.find_solutions(col + 1)
                self.board[row][col] = 0

    def show_solutions(self):
        for solution in self.solutions:
            self.canvas.delete("queen")
            for row in range(self.n):
                for col in range(self.n):
                    color = "white" if (row + col) % 2 == 0 else "black"
                    self.canvas.create_rectangle(col * 50, row * 50,
                                                 (col + 1) * 50, (row + 1) * 50,
                                                 fill=color)
                    if solution[row][col] == 1:
                        self.canvas.create_oval(col * 50, row * 50,
                                                (col + 1) * 50, (row + 1) * 50,
                                                fill="red", tags="queen")
            self.root.update()
            self.root.after(1000)  # Pause for visualization (1 second)


def main():
    n = 4  # Change this value to the desired N
    root = tk.Tk()
    root.title(f"N-Queens Solver (N={n})")

    solver = NQueensSolver(root, n)
    solver.show_solutions()  # Show solutions after finding them

    root.mainloop()


if __name__ == "__main__":
    main()
