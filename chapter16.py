# CHAPTER 16: MODERATE PROBLEMS

from chapter2 import*


def trailing_zeros(n: int):
    total = 0
    divisor = 5

    while divisor <= n:
        total += n // divisor
        divisor *= 5

    return total


def number_swapper(a: Node, b: Node):
    a.data = a.data + b.data
    b.data = a.data - b.data
    a.data = a.data - b.data


def intersection_point(A0: list, A1: list, X0: list, X1: list):
    a0,b0 = A0[0],A0[1]
    a1,b1 = A1[0],A1[1]
    x0,y0 = X0[0],X0[1]
    x1,y1 = X1[0],X1[1]

    c11 = a1-a0
    c12 = -1*(b1-b0)
    c21 = x1-x0
    c22 = -1*(y1-y0)

    det = c11*c22 - c12*c21

    #Check if the slopes match
    if det == 0:
        # Check if the lines coincide
        if (x1-x0)*b0 == (y1-y0)*(a0-x0) + y0*(x1-x0):
            return A0
        else:
            return "No intersection found"
    else:
        d1 = c11*b0 + c12*a0
        d2 = c21*y0 + c22*x0

        s1 = (c22*d1 - c12*d2)/det
        s0 = (-c21*d1 + c11*d2)/det

        return [s0,s1]


def tic_tac_win(A: list):
    if len(A) != len(A[0]):
        print("Invalid board size")
        return
    else:
        board_size = len(A)
        x_count = 0
        o_count = 0
        for i in range(0,board_size):
            for j in range(0,board_size):
                if A[i][j]=='X':
                    x_count += 1
                elif A[i][j]=='O':
                    o_count  += 1
        if x_count != o_count + board_size%2:
            print("Invalid game")
            return

        #Check rows
        for i in range(0,board_size):
            start = A[i][0]
            current = 0
            while current<board_size and A[i][current]==start:
                current+=1
            if current==board_size:
                winner = "The winner is " + A[i][0] + '!'
                print(winner)
                return

        #Check columns
        for j in range(0,board_size):
            start = A[0][j]
            current = 0
            while current<board_size and A[current][j]==start:
                current+=1
            if current==board_size:
                winner = "The winner is " + A[0][j] + '!'
                print(winner)
                return

        #Check diagonals
        start = A[0][0]
        current = 0
        while current<board_size and A[current][current]==start:
            current+=1
        if current==board_size:
            winner = "The winner is " + A[0][0] + '!'
            print(winner)
            return

        start = A[board_size-1][0]
        current = 0
        while current < board_size and A[board_size-1-current][current] == start:
            current += 1
        if current == board_size:
            winner = "The winner is " + A[0][0] + '!'
            print(winner)
            return

        print("Draw")
        return