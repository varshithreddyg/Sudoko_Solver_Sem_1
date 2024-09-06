import tkinter as tk
from src.gui.sudoku_gui import GUI

def main():
    root = tk.Tk()
    root.geometry("720x455")
    root.configure(background='white')
    root.title("Sudoku")

    try:
        root.iconbitmap("icon\\sudoku.ico")
    except: pass

    Game = GUI(root)
    Game.generate_sudoku_board()
    Game.right_side_option_block()

    root.mainloop()

if __name__ == '__main__':
    main()