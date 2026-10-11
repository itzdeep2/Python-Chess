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

def display():
    print(". a b c d e f g h")
    for i, row in enumerate(board):
        print(f"{8 - i} {' '.join(row)} {8 - i}")
        print(". a b c d e f g h\n")


def parse_move(pos):
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    return row, col

def play():
    while True:
        display()
        move = input("Enter move (e.g., e2 e4) or q to quit: ")
        if move == 'q':
            break
        try:
            start, end = move.split()
            r1, c1 = parse_move(start)
            r2, c2 = parse_move(end)
            board[r2][c2] = board[r1][c1]
            board[r1][c1] = '.'
        except:
            pass
        
if __name__ == "__main__":
    play()