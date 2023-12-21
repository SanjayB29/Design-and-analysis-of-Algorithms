direction = "DLRU"
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

def is_valid(r, c, n, maze):
    return 0 <= r < n and 0 <= c < n and maze[r][c] == 1  # Check maze[r][c] == 1

def findPath(r, c, maze, n, ans, current_path):
    if r == n - 1 and c == n - 1:
        ans.append(current_path)
        return

    maze[r][c] = 0

    for i in range(4):
        nextr = r + dr[i]
        nextc = c + dc[i]
        if is_valid(nextr, nextc, n, maze):
            current_path += direction[i]
            findPath(nextr, nextc, maze, n, ans, current_path)
            current_path = current_path[:-1]

    maze[r][c] = 1


n = 4
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

result = []
current_path = ""
findPath(0, 0, maze, n, result, current_path)

if len(result) == 0:
    print(-1)
else:
    for path in result:
        print(path, end=" ")
    print()
