# CHAPTER 8: RECURSION AND DYNAMIC PROGRAMMING

def triple_step(n: int):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)


def triple_step_iterative(n: int):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        first = 1
        second = 1
        third = 2

        for i in range(3,n+1):
            current = third + second + first
            first = second
            second = third
            third = current

    return current


def triple_step_memo(n: int):
    pass


def robot(grid, cp = [0,0], path = []):
    #print(path)
    col_size = len(grid)
    row_size = len(grid[0])

    if cp[1] + 1 < row_size and grid[cp[0]][cp[1] + 1] != 'x':
        path.append('r')
        #print(path)
        return robot(grid, [cp[0],cp[1] + 1], path)

    elif cp[0] + 1 < col_size and grid[cp[0] + 1][cp[1]] != 'x':
        path.append('d')
        #print(path)
        return robot(grid, [cp[0] + 1, cp[1]], path)

    elif cp[0] == col_size - 1 and cp[1] == row_size - 1:
        return path

    else:
        grid[cp[0]][cp[1]] = 'x'
        if path[len(path) - 1] == 'r':
            cp[1] -= 1
        elif path[len(path) - 1] == 'd':
            cp[0] -= 1

        path.pop()
        return robot(grid, [cp[0],cp[1]], path)


def power_set(arr: list):
    if len(arr) == 0:
        return [[]]
    else:
        last = arr[len(arr) - 1]
        arr.pop()

        first = power_set(arr)
        second = []
        for x in first:
            second.append(x + [last])

        return first + second

