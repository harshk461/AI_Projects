from tkinter import *
from tkinter import messagebox

# O->human chance->1
# X->Computer chance->0

root = Tk()
root.resizable(0, 0)

chance = True

def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))

def clear():
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            btn_array[i][j].config(state=ACTIVE)
            btn_array[i][j].configure(text=" ")

def evaluate(board):
    if winner(board, 'X'):
        return 1
    elif winner(board, 'O'):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if winner(board, 'X'):
        return 1
    if winner(board, 'O'):
        return -1
    if isfull():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move():
    best_score = -float("inf")
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def nextMove():
    global chance
    if isfull():
        return
    row, col = find_best_move()
    board[row][col] = "X"
    btn_array[row][col].config(text='X', state=DISABLED)
    chance = not chance

def isFree(i, j):
    return board[i][j] == " "

def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag

def click(r, c):
    global chance

    if (chance == True and board[r][c] == " "):
        board[r][c] = 'O'
        btn_array[r][c].configure(text='O', state=DISABLED)
        chance = not chance
        if (winner(board, 'O')):
            clear()
            return messagebox.showinfo("Winner O", "Winnnnnnerrrr")

    if (chance == False):
        nextMove()
        if (winner(board, 'X')):
            clear()
            return messagebox.showinfo("Winner X", "Winnnnnnerrrr")

    if (isfull()):
        clear()
        return messagebox.showinfo("Tie", "Tieee")

btn_array = []
board = [[" " for i in range(3)] for j in range(3)]

for i in range(3):
    btn_array.append(i)
    btn_array[i] = []
    for j in range(3):
        btn_array[i].append(j)
        btn_array[i][j] = Button(
            root,
            height=4,
            width=6,
            font=("Times New Roman", 14),
            command=lambda r=i, c=j: click(r, c))
        btn_array[i][j].grid(row=i, column=j)

if (__name__ == '__main__'):
    root.mainloop()
