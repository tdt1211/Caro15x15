import tkinter as tk
from tkinter import messagebox
import random

BOARD_SIZE = 15
CELL_SIZE = 32
STONE_RADIUS = 12

class CaroGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Caro 15x15 - Người vs Máy")
        self.canvas = tk.Canvas(root, width=BOARD_SIZE*CELL_SIZE, height=BOARD_SIZE*CELL_SIZE, bg='bisque')
        self.canvas.pack()
        self.board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.turn = 1  # 1: Người, 2: Máy
        self.game_over = False
        self.draw_board()
        self.canvas.bind("<Button-1>", self.human_move)
        self.add_restart_button()

    def draw_board(self):
        for i in range(BOARD_SIZE):
            self.canvas.create_line(CELL_SIZE//2, CELL_SIZE//2 + i*CELL_SIZE,
                                    CELL_SIZE//2 + (BOARD_SIZE-1)*CELL_SIZE, CELL_SIZE//2 + i*CELL_SIZE)
            self.canvas.create_line(CELL_SIZE//2 + i*CELL_SIZE, CELL_SIZE//2,
                                    CELL_SIZE//2 + i*CELL_SIZE, CELL_SIZE//2 + (BOARD_SIZE-1)*CELL_SIZE)

    def draw_stone(self, x, y, player):
        color = 'black' if player == 1 else 'white'
        self.canvas.create_oval(
            CELL_SIZE//2 + x*CELL_SIZE - STONE_RADIUS,
            CELL_SIZE//2 + y*CELL_SIZE - STONE_RADIUS,
            CELL_SIZE//2 + x*CELL_SIZE + STONE_RADIUS,
            CELL_SIZE//2 + y*CELL_SIZE + STONE_RADIUS,
            fill=color, outline='gray')

    def human_move(self, event):
        if self.game_over or self.turn != 1:
            return
        x = (event.x - CELL_SIZE//2 + CELL_SIZE//2) // CELL_SIZE
        y = (event.y - CELL_SIZE//2 + CELL_SIZE//2) // CELL_SIZE
        if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and self.board[y][x] == 0:
            self.board[y][x] = 1
            self.draw_stone(x, y, 1)
            if self.check_win(x, y, 1):
                self.game_over = True
                messagebox.showinfo("Kết thúc", "Bạn thắng!")
                return
            self.turn = 2
            self.root.after(500, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return
        # 1. Tìm nước thắng cho bot
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[j][i] == 0:
                    self.board[j][i] = 2
                    if self.check_win(i, j, 2):
                        self.draw_stone(i, j, 2)
                        self.game_over = True
                        messagebox.showinfo("Kết thúc", "Máy thắng!")
                        return
                    self.board[j][i] = 0
        # 2. Chặn nước thắng của người chơi
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[j][i] == 0:
                    self.board[j][i] = 1
                    if self.check_win(i, j, 1):
                        self.board[j][i] = 2
                        self.draw_stone(i, j, 2)
                        self.turn = 1
                        return
                    self.board[j][i] = 0
        # 3. Đánh gần quân người nhất
        max_score = -1
        move = None
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board[j][i] == 0:
                    score = self.count_nearby(i, j, 1)
                    if score > max_score:
                        max_score = score
                        move = (i, j)
        if move:
            x, y = move
        else:
            # fallback random nếu không tìm được
            empty = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if self.board[j][i] == 0]
            if not empty:
                messagebox.showinfo("Kết thúc", "Hòa!")
                self.game_over = True
                return
            x, y = random.choice(empty)
        self.board[y][x] = 2
        self.draw_stone(x, y, 2)
        if self.check_win(x, y, 2):
            self.game_over = True
            messagebox.showinfo("Kết thúc", "Máy thắng!")
            return
        self.turn = 1

    def count_nearby(self, x, y, player):
        # Đếm số quân player xung quanh ô (x, y) trong phạm vi 2 ô
        count = 0
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                nx, ny = x + dx, y + dy
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                    if self.board[ny][nx] == player:
                        count += 1
        return count

    def check_win(self, x, y, player):
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for dx, dy in directions:
            count = 1
            for dir in [1, -1]:
                nx, ny = x, y
                while True:
                    nx += dx * dir
                    ny += dy * dir
                    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and self.board[ny][nx] == player:
                        count += 1
                    else:
                        break
            if count >= 5:
                return True
        return False

    def add_restart_button(self):
        self.restart_btn = tk.Button(self.root, text="Chơi lại", command=self.reset_game)
        self.restart_btn.pack(pady=5)

    def reset_game(self):
        self.canvas.delete("all")
        self.board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.turn = 1
        self.game_over = False
        self.draw_board()

def main():
    root = tk.Tk()
    game = CaroGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
