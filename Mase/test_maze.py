from solvemaze import *

if __name__ == '__main__':
    maze = build_maze("mazefile.txt")
    print(maze)
    # * * * * *
    # * _ * _ *
    # * _ _ _ *
    # * _ * _ _
    # _ _ * * *
    path_found = maze.findPath()
    print(path_found)
    # True
    print(maze)
    # * * * * *
    # * o * o *
    # * x x x *
    # * x * x x
    # _ x * * *
    maze.reset()
    print()
    print(maze)
    # * * * * *
    # * _ * _ *
    # * _ _ _ *
    # * _ * _ _
    # _ _ * * *
