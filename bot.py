import random
from tkinter import messagebox
from caro_board import BOARD_SIZE

class CaroBot:
    def __init__(self, board):
        self.board = board

    def ai_move(self):
        if self.board.game_over:
            return
        # 1. Thắng nếu có thể
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board.board[j][i] == 0:
                    self.board.board[j][i] = 2
                    if self.board.check_win(i, j, 2):
                        self.board.draw_stone(i, j, 2)
                        self.board.game_over = True
                        messagebox.showinfo("Kết thúc", "Máy thắng!")
                        return
                    self.board.board[j][i] = 0
        # 2. Chặn thắng của người
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board.board[j][i] == 0:
                    self.board.board[j][i] = 1
                    if self.board.check_win(i, j, 1):
                        self.board.board[j][i] = 2
                        self.board.draw_stone(i, j, 2)
                        self.board.turn = 1
                        return
                    self.board.board[j][i] = 0
        # 3. Đánh nước mạnh nhất (tấn công + phòng thủ)
        best_score = -float('inf')
        move = None
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.board.board[j][i] == 0:
                    score = self.evaluate(i, j)
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        if move:
            x, y = move
        else:
            empty = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if self.board.board[j][i] == 0]
            if not empty:
                messagebox.showinfo("Kết thúc", "Hòa!")
                self.board.game_over = True
                return
            x, y = random.choice(empty)
        self.board.board[y][x] = 2
        self.board.draw_stone(x, y, 2)
        if self.board.check_win(x, y, 2):
            self.board.game_over = True
            messagebox.showinfo("Kết thúc", "Máy thắng!")
            return
        self.board.turn = 1

    def evaluate(self, x, y):
        # Đánh giá điểm cho ô (x, y) dựa trên tấn công và phòng thủ
        return self.score_point(x, y, 2) + self.score_point(x, y, 1) * 0.9

    def score_point(self, x, y, player):
        # Tính điểm dựa trên số lượng quân liên tiếp và hướng mở
        directions = [(1,0), (0,1), (1,1), (1,-1)]
        score = 0
        for dx, dy in directions:
            count = 1
            open_ends = 0
            for dir in [1, -1]:
                nx, ny = x, y
                while True:
                    nx += dx * dir
                    ny += dy * dir
                    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                        if self.board.board[ny][nx] == player:
                            count += 1
                        elif self.board.board[ny][nx] == 0:
                            open_ends += 1
                            break
                        else:
                            break
                    else:
                        break
            if count >= 5:
                score += 100000
            elif count == 4 and open_ends == 2:
                score += 10000
            elif count == 4 and open_ends == 1:
                score += 1000
            elif count == 3 and open_ends == 2:
                score += 500
            elif count == 3 and open_ends == 1:
                score += 100
            elif count == 2 and open_ends == 2:
                score += 50
            elif count == 2 and open_ends == 1:
                score += 10
        return score
