from collections import namedtuple

Coordinate = namedtuple('Coordinate', ('x', 'y'))

BLACK, WHITE=range(2)

def search_maze(maze, S, E):
    if not (0 <= R.x <= len(maze) and 0 <= E.y <= len(maze[E.x]):)
        return []
    def search_maze_helper(S):
        #if a square we are visiting is not white or x and y coordinates or S or E are out of range,
        #We return false : there is no point in continuing further.
        if not (0 <= S.x <= len(maze) and 0 <= S.y <= len(maze[S.x]) 
                and maze[S.x][S.y] != WHITE):
            return False
        
        #If not, then this is a valid white node which can be included in the result path
        #Mark it as visited by changing it to black.
        #Add the node to the path
        #Check if S==E which shows we have found a path. If so, return true.
        path.append(S)
        maze[S.x][S.y] = BLACK
        if S == E:
            return True
        #Keep doing this as long as one of the combinations of x and y combinations for the adjacent blocks for current lock gets True.
        #If we loop through all possibilities and then did not reach anything, we just remove the current S from the path and return false.
        if not any(map(search_maze, map(Coordinate, (S.x+1, S.x-1, S.x, S.x), (S.y, S.y, S.y-1, S.y+1)))):
            del path[-1]
            return False
        return path

    search_maze_helper(S)
