#Assuming maze is a matrix with 0 indicating white and 1 indicating black
def solve_maze(maze, S, E):
    #Visited
    if maze[S[0]][S[1]] == 2:
        return False

    #Mark as visited
    maze[S[0]][S[1]] = 2

    #We have reached the exit  
    if S[0] == E[0] and S[1] == E[1]:
        return True
    
    #Create a list of its adjacent blocks and traverse each of these blocks
    adj = []
    i = S[0]
    j = S[1]
    if i and j:
        adj.append((i-1, j-1))
        adj.append((i-1, j))
        adj.append((i, j-1))
        if i < len(maze)-1 and j < len(maze[0])-1:
            adj.append((i+1, j+1))
            adj.append((i, j+1))
            adj.append((i+1, j))
        elif i < len(maze)-1:
            adj.append((i+1, j))
        elif j < len(maze[0])-1:
            adj.append((i, j+1))
    elif i:
        adj.append((i-1, j)
        adj.append((i+1, j+1))
        adj.append((i, j+1))
        adj.append((i+1, j))
        elif i < len(maze)-1:
            adj.append((i+1, j))
    elif j:
        adj.append((i, j-1)

            return any(solve_maze(maze, box, E) for box in adj if adj != 1)`:w


From the book:
    map(    
