class sudokuSolver:
    def __init__(this, grid):
        this.grid = grid

    def printGrid(this):
        for row in this.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

    def isSafe(this, row, col, num):
        for x in range(9):
            if this.grid[row][x] == num:
                return False

        for x in range(9):
            if this.grid[x][col] == num:
                return False

        sRow = row-row % 3
        sCol = col-col % 3
        for i in range(3):
            for j in range(3):
                if this.grid[i+sRow][j+sCol] == num:
                    return False
        return True

    def solver(this):
        emptyCell = this.empty_location()
        if not emptyCell:
            return True

        row, col = emptyCell

        for num in range(1, 10):
            if this.isSafe(row, col, num):
                this.grid[row][col] = num

                if this.solver():
                    return True

                this.grid[row][col] = 0
        return False

    def empty_location(this):
        for i in range(9):
            for j in range(9):
                if this.grid[i][j] == 0:
                    return (i, j)
        return None


sudoku_grid = [
    [6, 8, 0, 4, 7, 0, 0, 0, 0],
    [7, 3, 4, 0, 6, 2, 5, 0, 0],
    [2, 0, 0, 5, 0, 8, 7, 0, 4],
    [0, 0, 0, 2, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 1, 0],
    [5, 6, 0, 9, 1, 3, 0, 0, 7],
    [0, 0, 1, 7, 2, 0, 3, 0, 0],
    [9, 2, 0, 0, 4, 0, 8, 0, 1],
    [0, 7, 0, 0, 0, 1, 0, 5, 6]
]

solve = sudokuSolver(sudoku_grid)
if solve.solver():
    print("puzzle solved")
    solve.printGrid()
else:
    print("solution doesnot exist")
