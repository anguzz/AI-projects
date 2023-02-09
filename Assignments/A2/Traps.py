
from collections import deque


def isValid(i, j, Y, X):
	return (0 <= i < X) and (0 <= j < Y)

def check(i, j, mat, ans):
    return mat[i][j] == 'O' and ans[i][j] == -1

def shortestDistanceToTraps(mat):   
    #initialize 
    (X, Y) = (len(mat), len(mat[0])) #matrix
    ans = [[0 for x in range(Y)] for y in range(X)]
    dq = deque() #queue
   
    r = [0, -1, 0, 1] #adjacent cells
    c = [-1, 0, 1, 0]

    #base
    if not mat or not len(mat):
        return []
   
    #add traps to dq
    for i in range(X):
        for j in range(Y):
            if mat[i][j] == 'T':
                dq.append((i, j, 0))
                ans[i][j] = 0 #update
            
            else:
                ans[i][j] = -1  #set trap=-1
    
    while dq:
        x, y, distance = dq.popleft() #remove front
        for i in range(len(r)):
            if isValid(x + r[i], y + c[i], Y, X) and check(x + r[i], y + c[i], mat, ans):
                ans[x + r[i]][y + c[i]] = distance + 1
                dq.append((x + r[i], y + c[i], distance + 1))
    return ans
	


if __name__ == '__main__':
	mat = [
		['O', 'O', 'T', 'O', 'O'],
		['O', 'W', 'O', 'T', 'O'],
		['W', 'T', 'O', 'O', 'W'],
		['O', 'O', 'O', 'O', 'O']
	]

	result = shortestDistanceToTraps(mat)

	# print results
	for r in result:
		print(r)
