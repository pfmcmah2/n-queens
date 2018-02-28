import matplotlib.pyplot as plt
import numpy as np
import math
import itertools
import copy

n = 8
k = 6

myboard = np.zeros((n,n), dtype=int)


def clear(board):
    for i in range(n):
        for j in range(n):
            board[i][j] = 0

def canplace(y, x, board):
    if(board[x][y] == 0):
        return True
    else:
        return False


def place(y, x, board):
    for i in range(n):
        if(i != x):
            board[i][y] -= 1
        if(i != y):
            board[x][i] -= 1
        if(x + i + 1 < n):
            if(y + i + 1 < n):
                board[x + i + 1][y + i + 1] -= 1
            if(y - i - 1 >= 0):
                board[x + i + 1][y - i - 1] -= 1
        if(x - i - 1 >= 0):
            if(y + i + 1 < n):
                board[x - i - 1][y + i + 1] -= 1
            if(y - i - 1 >= 0):
                board[x - i - 1][y - i - 1] -= 1
    board[x][y] += n


def isvalid(inboard, level):
    temp = copy.deepcopy(inboard)
    locations = list(itertools.permutations(range(0, n), n - level))
    for i in locations:
        valid = True
        temp = copy.deepcopy(inboard)
        for j in range(level, n):
            if(valid == True):
                if(canplace(i[j - level], j, temp)):
                    place(i[j - level], j, temp)
                else:
                    valid = False
        if(valid == True):
            return True
    return False


q_location = []
for x in itertools.product(range(n), repeat = k):
    q_location.append(x)
#print(q_location)

total = n**k
#print(total)

outlist = []
count = 0
n_valid = 0
for i in q_location:
    clear(myboard)
    valid = True
    for j in range(k):
        if(valid == True):
            if(canplace(i[j], j, myboard)):
                place(i[j], j, myboard)
            else:
                valid = False
    if(valid == True):
        num_empty = 0
        for a in range(n):
            for b in range(n):
                if(myboard[a][b] == 0):
                    num_empty += 1
        if(isvalid(myboard, k) == True):
            print(count, abs((total-1)/2 - count))
            outlist.append(1)
            n_valid += 1
        else:
            outlist.append(0)
    else:
        outlist.append(0)
    count += 1
print("total = ", count)
print("total valid = ", n_valid)

T = np.arange(0, count, 1)
plt.xlabel("Permutation Number")
plt.ylabel("Valid")
plt.title("n-queens")
plt.plot(T, outlist, 'ro')
plt.ylim([0,1])
plt.legend()
plt.show()
