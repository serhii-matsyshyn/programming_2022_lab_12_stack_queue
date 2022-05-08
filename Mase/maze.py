"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def findPath(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        return self.find_path()

    def find_path(self, row: int = None, col: int = None):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        # If no parameters are given, use the stored starting cell.
        if row is None:
            row = self._start_cell.row
        if col is None:
            col = self._start_cell.col

        if self._valid_move(row, col):
            self._mark_path(row, col)

            if self._exit_found(row, col):
                # If the current cell is the exit, we're done.
                return True
            if self.find_path(row - 1, col):
                # path found to the top
                return True
            if self.find_path(row, col + 1):
                # path found to the right
                return True
            if self.find_path(row + 1, col):
                # path found to the bottom
                return True
            if self.find_path(row, col - 1):
                # path found to the left
                return True

            self._mark_tried(row, col)

        return False

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if (self._maze_cells[row, col] == self.PATH_TOKEN or
                        self._maze_cells[row, col] == self.TRIED_TOKEN):
                    self._maze_cells[row, col] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        str_repr = ""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] is None:
                    str_repr += "_ "
                else:
                    str_repr += self._maze_cells[row, col]
                    str_repr += " "
            str_repr += "\n"
        return str_repr

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return (0 <= row < self.num_rows() and
                0 <= col < self.num_cols() and
                self._maze_cells[row, col] is None)

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""

    def __init__(self, row, col):
        self.row = row
        self.col = col


if __name__ == '__main__':
    maze = Maze(5, 5)
    maze.reset()

    print(maze)
