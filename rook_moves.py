
def dfs(board, x, y, visited):
    visited[y][x] = True
    counts = 0
    for j in range(len(board)):
        if j != y and board[j][x] and not visited[j][x]:
            counts += dfs(board, x, j, visited)

    for i in range(len(board[y])):
        if i != x and board[y][i] and not visited[y][i]:
            counts += dfs(board, i, y, visited)
    return counts + 1

def clear_board(board, visited):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if visited[y][x]:
                board[y][x] = False

def find_max_moves(board):
    count = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]:
                visited = [[False for _ in range(len(board[j]))] for j in range(len(board))]
                count += dfs(board, x, y, visited) - 1
                clear_board(board, visited)

    return count


if __name__ == '__main__':
    board = [
        [True, False, False, True],
        [False, True, True, False],
        [False, True, True, True],
        [True, False, False, True],
    ]

    print(find_max_moves(board))
