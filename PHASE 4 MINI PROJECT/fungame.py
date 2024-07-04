class TicTacToe3D:
    def __init__(self):
        self.grid = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_grid(self):
        for z in range(3):
            print(f"Level {z+1}")
            for y in range(3):
                for x in range(3):
                    cell = self.grid[z][y][x]
                    if cell is None:
                        print('.', end=' ')
                    else:
                        print(cell, end=' ')
                print()
            print()

    def is_valid_move(self, z, y, x):
        return self.grid[z][y][x] is None

    def make_move(self, z, y, x):
        if self.is_valid_move(z, y, x):
            self.grid[z][y][x] = self.current_player
            if self.check_win():
                print(f"Player {self.current_player} wins!")
                return True
            self.current_player = "O" if self.current_player == "X" else "X"
            return False
        else:
            print("Invalid move, try again.")
            return False

    def check_win(self):
        # Check all lines in the 3D grid
        lines = []

        # Rows, Columns, and Depths
        for i in range(3):
            for j in range(3):
                lines.append([(i, j, k) for k in range(3)])  # Depth
                lines.append([(i, k, j) for k in range(3)])  # Columns
                lines.append([(k, i, j) for k in range(3)])  # Rows

        # Main Diagonals in each plane
        for i in range(3):
            lines.append([(i, k, k) for k in range(3)])
            lines.append([(i, k, 2-k) for k in range(3)])
            lines.append([(k, i, k) for k in range(3)])
            lines.append([(k, i, 2-k) for k in range(3)])
            lines.append([(k, k, i) for k in range(3)])
            lines.append([(k, 2-k, i) for k in range(3)])

        # Cross Diagonals
        lines.append([(k, k, k) for k in range(3)])
        lines.append([(k, k, 2-k) for k in range(3)])
        lines.append([(k, 2-k, k) for k in range(3)])
        lines.append([(2-k, k, k) for k in range(3)])

        for line in lines:
            if all(self.grid[z][y][x] == self.current_player for z, y, x in line):
                return True

        return False

    def play(self):
        self.display_grid()
        while True:
            try:
                z, y, x = map(int, input(f"Player {self.current_player}, enter your move (z y x): ").split())
                if self.make_move(z-1, y-1, x-1):
                    break
                self.display_grid()
            except ValueError:
                print("Invalid input. Please enter three integers separated by spaces.")

if __name__ == "__main__":
    game = TicTacToe3D()
    game.play()
