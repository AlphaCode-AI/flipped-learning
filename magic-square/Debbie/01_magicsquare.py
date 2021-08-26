import sys

NUMBER = int(sys.argv[1])

def findidx(count,board,turn,num):
    row = turn[0]
    col = turn[1]
    row += 1
    col += 1
            
    if count == 1:
        row = num
        col = (num//2)+1

    elif board[row][col] == False:
        
        if (row>num)&(col>num):
            row = turn[0]-1
            col = turn[1]
        elif row > num:
            if board[1][col] == 0:
                row = 1
        elif col > num:
            if board[row][1] == 0:
                col = 1                


    elif board[row][col]!=0:
        row = turn[0]-1
        col = turn[1]       

    return [row,col]

def check(board,num):
    checknum = num*((num*num)+1)//2
    for b in range(len(board)):
        if (sum(board[b]) != checknum) or (sum([board[i][b] for i in range(len(board))]) != checknum):
            return False
    if (sum([board[i][i] for i in range(len(board))]) != checknum) or (sum(board[i][len(board)-1-i] for i in range(len(board))) != checknum):
        return False

    return True

if __name__=="__main__":

    if NUMBER%2 == 1:
        board = []
        for num01 in range(NUMBER+2):
            miniboard = []
            for num02 in range(NUMBER+2):
                miniboard.append(False)
            board.append(miniboard)
            
        for num01 in range(1,NUMBER+1):
            for num02 in range(1,NUMBER+1):
                board[num01][num02] = 0
        turn = [0,0]
        total = NUMBER*NUMBER
        count = 1     
        while(count<=total):
            turn = findidx(count, board, turn, NUMBER)
            board[turn[0]][turn[1]] = count
            count+=1
        
        board = board[1:-1]
        board = [board[i][1:-1] for i in range(len(board))]

    else:
        
        if NUMBER%4 == 0:
            miniboard_side = NUMBER//4
            miniboard_count = (miniboard_side)*(miniboard_side)
            indexboard=[]
            for i in range(NUMBER):
                indexboard.append([])
            board=[]
            for count in range(len(indexboard)):
                indexboard[count] = [(miniboard_side*count)+i for i in range(1,miniboard_side+1)]

            while len(indexboard)>0:
                thisturn = list()

                for j in range(miniboard_side):
                    thisturn.append([indexboard[rows][j] for rows in range(4)])

                board.append(thisturn)

                indexboard = indexboard[4:]

            for count01 in range(miniboard_side):
                for count02 in range(miniboard_side):
                    for count03 in range(4):
                        board[count01][count02][count03]=[(board[count01][count02][count03] * 4)-i for i in range(3,-1,-1)]

            changelist=[[0,1],[0,2],[1,0],[1,3],[2,0],[2,3],[3,1],[3,2]]
            for i in range(miniboard_side//2):
                for j in range(miniboard_side-1, -1, -1):
                    for idx in range(len(changelist)):
                        temp = board[i][j][changelist[idx][0]][changelist[idx][1]]
                        board[i][j][changelist[idx][0]][changelist[idx][1]] = board[miniboard_side-1-i][miniboard_side-1-j][changelist[7-idx][0]][changelist[7-idx][1]]
                        board[miniboard_side-1-i][miniboard_side-1-j][changelist[7-idx][0]][changelist[7-idx][1]] = temp

            if miniboard_side%2 != 0:
                last = list(range(miniboard_side))                 
                while len(last)>1:
                    for idx in range(len(changelist)):

                        temp = board[miniboard_side//2][last[0]][changelist[idx][0]][changelist[idx][1]]
                        board[miniboard_side//2][last[0]][changelist[idx][0]][changelist[idx][1]] = board[miniboard_side//2][last[-1]][changelist[7-idx][0]][changelist[7-idx][1]]
                        board[miniboard_side//2][last[-1]][changelist[7-idx][0]][changelist[7-idx][1]] = temp
                        
                    last = last[1:-1]
                    
                for idx in range(len(changelist)//2):
                    temp = board[miniboard_side//2][miniboard_side//2][changelist[idx][0]][changelist[idx][1]]
                    board[miniboard_side//2][miniboard_side//2][changelist[idx][0]][changelist[idx][1]] = board[miniboard_side//2][miniboard_side//2][changelist[7-idx][0]][changelist[7-idx][1]]
                    board[miniboard_side//2][miniboard_side//2][changelist[7-idx][0]][changelist[7-idx][1]] = temp


            for s in range(miniboard_side):
                for i in range(4):
                    for j in range(1,miniboard_side):
                        board[s][0][i].extend(board[s][j][i])

            for i in range(1,miniboard_side):
                board[0][0].extend(board[i][0])
                
            board = board[0][0]

        else:
            n = NUMBER//4
            num = NUMBER//2
            realboard=[[],[],[],[]]
            for i in range(4):
                board = []
                for num01 in range(num+2):
                    miniboard = []
                    for num02 in range(num+2):
                        miniboard.append(False)
                    board.append(miniboard)

                for num01 in range(1,num+1):
                    for num02 in range(1,num+1):
                        board[num01][num02] = 0
                count = 1
                total = num*num
                turn = [0,0]
                while(count<=total):

                    turn = findidx(count, board, turn, num)
                    board[turn[0]][turn[1]] = count + (total*i)
                    count+=1

                realboard[i] = board

            orderlist = [0,3,1,2]
            board=[[],[],[],[]]
            for i in range(4):
                board[orderlist[i]]=[j[1:-1] for j in realboard[i][1:-1]]

            for i in range(num):
                board[0][i].extend(board[1][i])
                board[2][i].extend(board[3][i])

            board[0].extend(board[2])
            board = board[0]

            for i in range(num):
                for j in range(n):
                    temp = board[i][j]
                    board[i][j] = board[i+num][j]
                    board[i+num][j] = temp


            for i in range(num):
                for j in range(NUMBER-1,NUMBER-n,-1):
                    temp = board[i][j]
                    board[i][j] = board[i+num][j]
                    board[i+num][j] = temp

            for i in range(2):
                temp = board[num//2][n-1+i]
                board[num//2][n-1+i] = board[(num//2)+num][n-1+i]
                board[(num//2)+num][n-1+i] = temp

    for b in board:
        print(b)
    print(check(board,NUMBER))