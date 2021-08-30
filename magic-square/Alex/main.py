import numpy as np
import math

def makeMagicSquare(n):
    n = int(n)

    if n % 2 == 1:
        makeOddSquare(n)
    elif n % 4 == 0:
        makeQuadrupleSquare(n)
    else:
        makeEvenSquare(n)

    print("\nmagic number = ", int(n * (n ** 2 + 1) / 2))

def makeEvenSquare(n):
    print(n)

def makeQuadrupleSquare(n):
    print(f"\ncreating {n} x {n} even magic square...")

    # step1. init ms1, ms2
    share = n // 4
    arr = np.arange(1, n*n+1)
    ms1 = np.reshape(arr, (n, n))
    ms2 = np.reshape(-np.sort(-arr), (n, n))

    # step2. init 4 corner (1:2:1)
    top = ms1[:share, share:share*3]
    bottom = ms1[share*3:share*4, share:share*3]
    left = ms1[share:share*3:, :share]
    right = ms1[share:share*3:, share*3:]

    top.fill(0)
    bottom.fill(0)
    left.fill(0)
    right.fill(0)

    leftTop = ms2[:share, :share]
    rightTop = ms2[:share, share*3:]
    leftBottom = ms2[share*3:, :share]
    rightBottom = ms2[share*3:, share*3:]
    center = ms2[share:share*3, share:share*3]

    leftTop.fill(0)
    rightTop.fill(0)
    leftBottom.fill(0)
    rightBottom.fill(0)
    center.fill(0)

    print('\n', ms1)
    print('\n', ms2)
    print('\n', ms1 + ms2)

def makeOddSquare(n):
    print(f"\ncreating {n} x {n} odd magic square...")
    ms = np.full((n, n), 0)

    # init
    value = 1
    row = n - 1
    col = math.trunc(len(ms) / 2)
    ms[row][col] = value
    value += 1
    print(ms)

    while value < n*n+1:
        # next value and position
        newRow = row + 1
        newCol = col + 1

        # invalid newRow ?
        if newRow == n and newCol < n:
            row = 0
            col = newCol
            ms[row][col] = value

        # invalid newCol ?
        elif newRow < n and newCol == n:
            row = newRow
            col = 0
            ms[row][col] = value

        # invalid newRow and newCol ?
        elif newRow == n and newCol == n:
            row = row - 1
            col = col
            ms[row][col] = value

        # value exist ?
        elif ms[newRow][newCol] != 0:
            row = row - 1
            col = col
            ms[row][col] = value

        # normal case
        else:
            row = newRow
            col = newCol
            ms[row][col] = value

        print("\n", ms)
        value += 1

def main():
    # magic square range
    squareMin = 3
    squareMax = 18

    print("magic square builder !!")
    while True:
        n = input(f"please input N ({squareMin} ~ {squareMax}): ")
        if n.isnumeric() and (squareMin <= int(n) <= squareMax):
            break

    while True:
        confirm = input(f"{n} 👈 are you sure? (Y/n) : ")

        if confirm.upper() == "N":
            print("\nbye bye!")
            break

        if confirm.upper() == "Y" or confirm == "":
            makeMagicSquare(n)
            break

if __name__ == "__main__":
    main()
