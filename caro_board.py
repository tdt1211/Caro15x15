import tkinter as tk
from tkinter import messagebox

BOARD_SIZE = 15
CELL_SIZE = 32
STONE_RADIUS = 12

class CaroBoard:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=BOARD_SIZE*CELL_SIZE, height=BOARD_SIZE*CELL_SIZE, bg='bisque')
        self.canvas.pack()
        self.board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.turn = 1  # 1: Người, 2: Máy
        self.game_over = False
        self.bot = None
        self.draw_board()
        self.canvas.bind("<Button-1>", self.human_move)

    def set_bot(self, bot):
        self.bot = bot

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
            if self.bot:
                self.root.after(300, self.bot.ai_move)

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

    def reset(self):
        self.canvas.delete("all")
        self.board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.turn = 1
        self.game_over = False
        self.draw_board()
