import tkinter as tk
import os

board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

filename_map = {
    'r': 'black-rook.png',
    'n': 'black-knight.png',
    'b': 'black-bishop.png',
    'q': 'black-queen.png',
    'k': 'black-king.png',
    'p': 'black-pawn.png',
    'R': 'white-rook.png',
    'N': 'white-knight.png',
    'B': 'white-bishop.png',
    'Q': 'white-queen.png',
    'K': 'white-king.png',
    'P': 'white-pawn.png'
}
    
class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.square_size = 64 
        self.canvas = tk.Canvas(root, width=8*self.square_size, height=8*self.square_size)
        self.canvas.pack()

        self.selected = None
        self.turn = 'White'

        self.piece_images = {}
        self.load_images()

        self.canvas.bind("<Button-1>", self.click)
        self.draw_board()

    def load_images(self):
        dir_path = "pieces-basic-png"
        for key, name in filename_map.items():
            full_path = os.path.join(dir_path, name)
            try:
                self.piece_images[key] = tk.PhotoImage(file=full_path)
            except Exception as e:
                print(f"Error loading {full_path}: {e}")
                self.piece_images[key] = None

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                color = "#DDB88C" if (row + col) % 2 == 0 else "#A66D4F"
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

                if self.selected == (row, col):
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=3)

                piece = board[row][col]
                if piece != '.':
                    img = self.piece_images.get(piece)
                    if img:
                        self.canvas.create_image(
                            x1 + self.square_size//2, 
                            y1 + self.square_size//2, 
                            image=img
                        )
                    else:
                        self.canvas.create_text(
                            x1 + self.square_size//2, 
                            y1 + self.square_size//2, 
                            text=piece, 
                            font=("Arial", 20)
                        )

    def click(self, event):
        col = event.x // self.square_size
        row = event.y // self.square_size

        if col > 7 or row > 7 or col < 0 or row < 0:
            return

        if not self.selected :
            piece = board[row][col]
            if piece != '.':
                if (self.turn == 'White' and piece.isupper()) or (self.turn == 'Black' and piece.islower()):
                    self.selected = (row, col)
            else:
                r1, c1  = self.selected
                r2, c2 = row, col

                if (r1, c1) == (r2, c2):
                    self.selected = None
                    self.draw_board()
                    return

                target = board[r2][c2]
                valid_move = True

                if target != '.':
                    if (self.turn == 'White' and target.isupper()) or (self.turn == 'Black' and target.islower()):
                        valid_move = False

                if valid_move:
                    board[r2][c2] = board[r1][c1]
                    board[r1][c1] = '.'

                    if target.lower() == 'k':
                        print(f"\n*** {self.turn} WINS! ***\n")

                    self.turn = 'Black' if self.turn == 'White' else 'White'

                self.selected =  None

            self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Interactive Python Chess")
    gui = ChessGUI(root)
    root.mainloop()
                
                
                