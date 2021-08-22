import numpy as np
import math

def makeMagicSquare(n):
    n = int(n)

    if n % 2 == 1:
        makeOddSquare(n)
    elif n % 4 == 0:
        makeQuadrupleMagicSquare(n)
    else:
        makeEvenMagicSquare(n)

    print("\nmagic number = ", int(n * (n ** 2 + 1) / 2))

def makeEvenMagicSquare(n):
    print()


def makeQuadrupleMagicSquare(n):
    print(f"\ncreating {n} x {n} even magic square...")

    # step1. init ms1, ms2
    arr = np.arange(1, n*n+1)
    ms1 = np.reshape(arr, (n, n))
    ms2 = np.reshape(-np.sort(-arr), (n, n))
    row = 0
    col = 0

    # step2. init diagonal
    while True:
        # need next row?
        if col == n:
            col = 0
            row += 1

        # invalid row?
        if row == n:
            break

        # is diagonal?
        if row == col or row == n-1-col:
            ms2[row][col] = 0
            col += 1
            continue

        # normal case
        ms1[row][col] = 0
        col += 1

    print("\n", ms1)
    print("\n", ms2)
    print("\n", ms1 + ms2)
    #
    # # step3. set values
    # row = n - 1
    # col = n - 1
    # while True:
    #     # invalid col?
    #     if col < 0:
    #         row -= 1
    #         col = n - 1
    #         continue
    #
    #     # invalid row?
    #     if row < 0:
    #         break
    #
    #     # exist value?
    #     if ms[row][col] != 0:
    #         col -= 1
    #         continue
    #
    #     # set magic value
    #     ms[row][col] = vector.pop(0)
    #     col -= 1
    #
    # print("\n", ms)

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
