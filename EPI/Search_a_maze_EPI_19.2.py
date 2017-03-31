class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    __repr__ = __str__

    # refer to http://stackoverflow.com/questions/12448175/confused-about-str
    # -in-python

class Search:

    def SearchMaze(self, maze, start, end):
        '''

        :param maze: input of 1's and 0's
        :param start: starting coordinate
        :param end:  ending coordinate
        :return: a path of coordinates

        '''

        def isValid(x, y, maze):
            if x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and \
                            maze[
                                x][y] == 0:
                return True

        # helper that performs DFS on the maze
        def search_maze_helper(s, e, maze):
            if s == e:
                # reached the destination
                return True

            # list of directions N , S , E, W
            directions = [[-1,0 ], [1,0], [0,1], [0, -1]]

            for d in directions:
                next = Coordinate(s.x + d[0], s.y + d[1])

                if isValid(next.x, next.y, maze):
                    maze[next.x][next.y] = 1
                    path.append(next)

                    if search_maze_helper(next, e, maze):
                        return True
                    path.pop()
            return False


        path = []
        maze[start.x][start.y] = 1 # to mark that cell done
        path.append(start)

        if not search_maze_helper(start, end, maze):
            path.pop() # so that we return an empty path

        return path


source = Coordinate(0,0)
dest = Coordinate(3,3)

maze = [
    [0,0,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [1,0,0,0]
]

print(Search().SearchMaze(maze, source, dest))