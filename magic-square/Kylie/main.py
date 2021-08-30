import numpy as np
import math


def check(n ,magic_square=None):

    if magic_square is not None:
        sum_value = sum(magic_square[0])
        diagonal_ascending = []
        diagonal_descending = []

        for i in range(0,n):
            if sum_value == sum(magic_square[i]) and sum_value == sum(magic_square[:][i]):
                diagonal_ascending.append(magic_square[i][i])
                diagonal_descending.append(magic_square[i][(n-1)-i])

        if sum(diagonal_ascending) == sum_value and sum(diagonal_descending) == sum_value:
            print("magic square value is ({})".format(int(sum_value)))
            print(" ")
            print(magic_square.astype(int))
    else:
        print('It is not yet')

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

        return magic_square, n


    elif n%4==0:
        ascending_array = np.array(range(0+1, n**2+1))
        descending_array = np.array(range(n**2, 0, -1))

        ascending_matrix = np.reshape(ascending_array, (-1,n))
        descending_matrix = np.reshape(descending_array, (-1,n))

        magic_square = np.zeros(shape=(n,n))
        
        if n/4==1:
            for x in range(0,n):
                for y in range(0,n):
                    if x == y or x+y == n-1:
                        magic_square[x][y] = ascending_matrix[x][y]
                    else:
                        magic_square[x][y] = descending_matrix[x][y]        
            # magic_square.astype(int)
            # print(magic_square.astype(int))
            return magic_square, n
        elif n/4>1:
            origin_matrix = [[(n*y)+x+1 for x in range(n)]for y in range(n)]
            origin_matrix = np.array(origin_matrix) 
            
            # print("origin matrix")
            # print(origin_matrix)

            # Corners of order (n/4)*(n/4)
            # 1. Top left corner
            for i in range(0,int(n/4)):
                for j in range(0,int(n/4)):
                    origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]
            
            # 2. Top right corner
            for i in range(0,int(n/4)):
                for j in range(int(3 * (n/4)),n):
                    origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]
        
            # 3. Bottom Left corner
            for i in range(int(3 * (n/4)),n):
                for j in range(0,int(n/4)):
                    origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]
            
            # 4. Bottom Right corner
            for i in range(int(3 * (n/4)),n):
                for j in range(int(3 * (n/4)),n):
                    origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]
                    
            # 5. Centre of matrix,order (n/2)*(n/2)
            for i in range(int(n/4),int(3 * (n/4))):
                for j in range(int(n/4),int(3 * (n/4))):
                    origin_matrix[i][j] = (n*n + 1) - origin_matrix[i][j]

            # print("=====================================================")
            # print("magic square matrix")
            magic_square = origin_matrix

            return magic_square, n
            # print(magic_square)

    else:
        
        return None, None

def main(args):
    number = args.number
    magic_square, n = make_magic_square(n=int(number))
    # print(magic_square)
    # print(n)
    check(n, magic_square)

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
