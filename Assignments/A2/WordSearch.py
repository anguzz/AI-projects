row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]

def isValid(mat, x, y, path):
	return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and (x, y) not in path

def DFS(mat, word, i, j, path=[], index=0):
    if mat[i][j] != word[index]:
        return None
    path.append((i, j))
    if index == len(word) - 1:
        print(path)
    else:
        for z in range(len(row)):
            if isValid(mat, i + row[z], j + col[z], path):
                DFS(mat, word, i + row[z], j + col[z], path, index + 1)
    path.pop()

def WordSearch(mat, word):
	# base case
	if not mat or not len(mat) or not len(word):
		return

	for i in range(len(mat)):
		for j in range(len(mat[0])):
			DFS(mat, word, i, j)


if __name__ == '__main__':

	mat = [
		['A', 'D', 'E', 'B', 'C'],
		['O', 'O', 'C', 'A', 'X'],
		['S', 'C', 'D', 'K', 'C'],
		['O', 'D', 'E', 'H', 'L']
	]
	word = 'CODE'

	WordSearch(mat, word)
