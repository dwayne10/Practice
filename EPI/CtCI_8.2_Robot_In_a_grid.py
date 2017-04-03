def get_path(maze):
    if not maze:
        return None

    path = []
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    start_row = len(maze) - 1
    start_col = len(maze[0]) - 1

    # we're starting from the dest i.e the bottom-right cell
    # the robot can only move rightways or downwards
    if solve_maze(maze, start_row, start_col, path, visited):
        return path

    else:
        return -1


def isValid(r, c, visited):
    if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]) or visited[r][c]:
        return False
    return True


def solve_maze(maze, row, col, path):

    if isValid(row, col, visited):
        visited[row][col] = True
        is_done = True if row == 0 and col == 0 else False

        if is_done or solve_maze(maze, row - 1, col, path, visited)
            or solve_maze(maze, row, col - 1, path, visited):
            path.append([row, col])
            return True
        else:
            return False

    visited[row][col] = True
    return False
