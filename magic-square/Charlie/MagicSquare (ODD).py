def generateSquare(n):
  magicSquare = [[0 for x in range(n)]
                 for y in range(n)]
# create matrix of dimension n by n with value 0

  i = n / 2
  j = n - 1
  num = 0
# define position of 1 with "first numner" formula.
  while num <= (n*n):
# apply the loop as long as the number to fill out is below or equal to square dimension (n^2)
    if i == -1 and j == n:
                     j = n-2
                     i = 0
#condition 3 - if (-1;n)...

    else:
      if j == n:
          j = 0
      if i < 0:
          i = n - 1
#condition 1.2

    if magicSquare[int(i)][int(j)]:
      j = j - 2
      i = i + 1
      continue
#condition 2 - if magicsquare already has number assigned at position
    else :
      magicSquare[int(i)][int(j)] = num
#assign number to place
      num = num + 1
#switch to next number to place
    j = j + 1
    i = i - 1
#continue the pattern normally (condition1)
  print("Printing a magic square of size ", n)
  print("Sum of rows, columns is ", n * (n * n + 1) / 2, "\n")

  for i in range(0, n):
    for j in range(0, n):
      print('%2d ' % (magicSquare[i][j]),
            end='')
#print the square in matrix format
      if j == n - 1:
        print()

n = input("Choose the size of the Square (odd number only): \n")
n = int(n)
print(f'Generating a magic square of size {n} \n...')
generateSquare(n)