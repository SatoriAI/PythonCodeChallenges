from pprint import pprint


class SudokuSolver:
    """Class used for solving sudoku puzzles. It is capable
    of solving i^2 x i^2 puzzles, however the algorithm in fact
    allows to take i from {1, 2, 3} because of the complexity.

    The class takes a sudoku (in a form of a 2D list) or a path
    to .txt file with sudoku written inside (in a form of lines
    and numbers separated with whitespaces). The backtracking
    algorithm solves the puzzle and then the solution can be
    seen using the sudoku attribute.
    """

    def __init__(self, sudoku=None, path=None):
        if sudoku is not None:
            self.sudoku = sudoku
        if path is not None:
            self.sudoku = self._read_sudoku(path)
        self.dim = len(self.sudoku)
        self.sqrt_dim = int(self.dim**0.5)

    def solve(self):
        """Solves sudoku using backtracking algorithm.
        """
        coords = [0, 0]
        if self._is_sudoku_filled(coords):
            return True
        row, column = coords
        for number in range(1, self.dim+1):
            if self._is_field_safe(row, column, number):
                self.sudoku[row][column] = number
                if self.solve():
                    return True
                else:
                    self.sudoku[row][column] = 0
        return False

    def _is_sudoku_filled(self, coords):
        """Checks whether a sudoku is filled
        correctly.
        """
        for i in range(self.dim):
            for j in range(self.dim):
                if self.sudoku[i][j] == 0:
                    coords[0], coords[1] = i, j
                    return False
        return True

    def _is_field_safe(self, row, column, number):
        """Checks whether a digit can be written
        in a certain field on the sudoku grid.
        """
        statement1 = self._is_row_safe(row, number)
        statement2 = self._is_column_safe(column, number)
        row = row - row % self.sqrt_dim
        column = column - column % self.sqrt_dim
        statement3 = self._is_square_safe(row, column, number)
        return statement1 and statement2 and statement3

    def _is_row_safe(self, row, number):
        """Checks whether a number can be written
        in a certain row.
        """
        for i in range(self.dim):
            if self.sudoku[row][i] == number:
                return False
        return True

    def _is_column_safe(self, column, number):
        """Checks whether a number can be written
        in a certain column.
        """
        for j in range(self.dim):
            if self.sudoku[j][column] == number:
                return False
        return True

    def _is_square_safe(self, row, column, number):
        """Checks whether a number can be written
        inside a square.
        """
        for i in range(self.sqrt_dim):
            for j in range(self.sqrt_dim):
                if self.sudoku[i+row][j+column] == number:
                    return False
        return True

    @staticmethod
    def _read_sudoku(path):
        """Creates a sudoku (list of lists)
        from a .txt file. Each line of the .txt
        file should contain digits separated
        with a whitespace. Digit "0" is equal
        to en empty cell in the sudoku grid.
        """
        sudoku = []
        with open(path, 'r') as file:
            for line in file.readlines():
                sudoku.append(list(map(int, (line.strip().split()))))
        return sudoku


if __name__ == "__main__":
    solver = SudokuSolver(path='files/sudoku/hard_01.txt')
    solver.solve()
    pprint(solver.sudoku)
