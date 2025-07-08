import tkinter as tk
from caro_board import CaroBoard
from bot import CaroBot

def main():
    root = tk.Tk()
    root.title("Caro 15x15 - Người vs Máy")
    board = CaroBoard(root)
    bot = CaroBot(board)
    board.set_bot(bot)
    root.mainloop()

if __name__ == "__main__":
    main()
