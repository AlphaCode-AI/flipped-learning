import numpy as np
import math


def check_validation(n ,magic_square):
    sum_value = sum(magic_square[0])
    diagonal_ascending = []
    diagonal_descending = []

    for i in range(0,n):
        if sum_value == sum(magic_square[i]) and sum_value == sum(magic_square[:][i]):
            diagonal_ascending.append(magic_square[i][i])
            diagonal_descending.append(magic_square[i][(n-1)-i])

    if sum(diagonal_ascending) == sum_value and sum(diagonal_descending) == sum_value:
        print("target number is ({})".format(n))
        print("magic square value is ({})".format(int(sum_value)))
        print(magic_square.astype(int))

def make_odd_oder(n):
    magic_square = np.zeros(shape=(n,n))
    
    x = 0
    y = math.floor(n/2)

    for i in range(0+1, n**2+1):
        if 0 <= x < n and 0 <= y < n:
            magic_square[x][y] = i
        elif x < 0 and 0 <= y < n:
            x = n-1
            magic_square[x][y] = i
        elif 0 <= x <n and y >= n:
            y = 0
            magic_square[x][y] = i
        elif x >= n and 0<= y <n:
            x = 0 
            magic_square[x][y] = i
        else:
            x = n-1
            y = 0
            magic_square[x][y] = i
        if i%n == 0:
            x = x+1
        else:
            x = x-1
            y = y+1

    return magic_square, n

def make_doubly_even_order(n):
    origin_matrix = [[(n*y)+x+1 for x in range(n)]for y in range(n)]
    origin_matrix = np.array(origin_matrix) 
    
    for i in range(0,int(n/4)):
        for j in range(0,int(n/4)):
            origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]
    
    for i in range(0,int(n/4)):
        for j in range(int(3 * (n/4)),n):
            origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]

    for i in range(int(3 * (n/4)),n):
        for j in range(0,int(n/4)):
            origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]
    
    for i in range(int(3 * (n/4)),n):
        for j in range(int(3 * (n/4)),n):
            origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]
            
    for i in range(int(n/4),int(3 * (n/4))):
        for j in range(int(n/4),int(3 * (n/4))):
            origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]

    magic_square = origin_matrix

    return magic_square, n


def make_single_evne_oder(n):
    magic_square = [[0 for j in range(n)] for i in range(n)]

    half_of_n = int(n // 2)
    square_of_half_of_n = half_of_n * half_of_n
    target_number = square_of_half_of_n
    twice_of_target= 2 * square_of_half_of_n
    three_times_of_target = 3 * square_of_half_of_n

    magic_square_of_half_of_n = make_magic_square(half_of_n)
    magic_square_of_half_of_n = magic_square_of_half_of_n[0]

    for j in range(0, half_of_n):
        for i in range(0, half_of_n):
            main_magic_square = magic_square_of_half_of_n[i][j]
            magic_square[i][j] = main_magic_square
            magic_square[i + half_of_n][j + half_of_n] = main_magic_square + square_of_half_of_n
            magic_square[i + half_of_n][j] = main_magic_square + twice_of_target
            magic_square[i][j + half_of_n] = main_magic_square + three_times_of_target

    double_half_of_n = half_of_n // 2

    for j in range(0, half_of_n):
        for i in range(0, n): 
            if i < double_half_of_n or i > n - double_half_of_n or (i == double_half_of_n and j == double_half_of_n):
                if not (i == 0 and j == double_half_of_n):
                    magic_square_to_replace = magic_square[i][j]
                    magic_square[i][j] = magic_square[i][j + half_of_n]
                    magic_square[i][j + half_of_n] = magic_square_to_replace
    
    return np.array(magic_square), n


def make_magic_square(n):
    if n%2==1:
        magic_square, n = make_odd_oder(n)
    elif n%4==0:
        magic_square, n = make_doubly_even_order(n)
    else:
        magic_square, n = make_single_evne_oder(n)

    return magic_square, n


def main(args):
    number = args.number
    n = int(number)
    magic_square, n = make_magic_square(n)
    check_validation(n=n, magic_square=magic_square)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="make magic square")
    parser.add_argument(
        "--number",
        default=3,
        help="input number"
    )
    args = parser.parse_args()

    main(args)
