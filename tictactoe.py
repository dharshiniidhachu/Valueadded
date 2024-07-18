import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text='', font='Arial 20', width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.update_button(row, col)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def update_button(self, row, col):
        button = self.buttons[row][col]
        button.config(text=self.current_player, state='disabled')
        if self.current_player == 'X':
            button.config(bg='pink')
        else:
            button.config(bg='light blue')

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]              
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def reset_board(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for row in self.buttons:
            for button in row:
                button.config(text='', bg='SystemButtonFace', state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
