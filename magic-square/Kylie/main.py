import numpy as np
import math

def make_magic_square(n):
    if n%2==1:
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
        sum_value = sum(magic_square[0])
        diagonal_ascending = []
        diagonal_descending = []

        for i in range(0,n):
            if sum_value == sum(magic_square[i]) and sum_value == sum(magic_square[:][i]):
                diagonal_ascending.append(magic_square[i][i])
                diagonal_descending.append(magic_square[i][(n-1)-i])

        if sum(diagonal_ascending) == sum_value and sum(diagonal_descending) == sum_value:
            print(magic_square)

    elif n%4==0:
        ascending_matrix = np.array(range(0+1, n**2+1))
        descending_matrix = np.array(range(n**2, 0, -1))

        ascending_matrix = np.reshape(ascending_matrix, (-1,n))
        descending_matrix = np.reshape(descending_matrix, (-1,n))

        magic_square = np.zeros(shape=(n,n))
        if n/4==1:
            for i in range(0,n):
                for j in range(0,n):
                    if i == j or i+j == n:
                        magic_square[i][j] = ascending_matrix[i][j]
                    else:
                        magic_square[i][j] = descending_matrix[i][j]        
            print(magic_square)

        elif n/4>1:
            print('It is not yet')
    else:
        print('It is not yet')

def main(args):
    number = args.number
    make_magic_square(n=int(number))

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
