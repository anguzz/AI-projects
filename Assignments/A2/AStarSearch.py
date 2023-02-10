class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 1,
            'H': 1,
            'I': 1,
            'J': 1,
            'K': 1
        }

        return H[n]

    def a_star_algorithm(self, start, stop):
        currDist,parent = {}, {}
        currDist[start] = 0
        parent[start] = start

        open = set([start])
        closed = set([])

        while len(open) > 0:
            n = None

            for v in open: #get lowest
                if n == None or currDist[v] + self.h(v) < currDist[n] + self.h(n):
                    n = v;

            if n == None: #base
                print('Path does not exist!')
                return None

            if n == stop: #if curr is stop we go down path
                path = []
                while parent[n] != n:
                    path.append(n)
                    n = parent[n]
                path.append(start)
                path.reverse()
                print('Path found: {}'.format(path))
                return path

            for (m, w) in self.get_neighbors(n): #go through neighbors
                if m not in open and m not in closed:
                    open.add(m)
                    parent[m] = n
                    currDist[m] = currDist[n] + w
                else: #check which path is quicker
                    if currDist[m] > currDist[n] + w:
                        currDist[m] = currDist[n] + w
                        parent[m] = n

                        if m in closed:
                            closed.remove(m)
                            open.add(m)
            open.remove(n) #remove n from open and add to closed off
            closed.add(n)

        print('Path does not exist!')
        return None

if __name__ == '__main__':

	adjacency_list1 = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

adjacency_list2 = {
    'A': [('B', 1)],
    'B': [('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 5), ('K', 11)],
    'E': [('G', 7), ('F', 8)],
    'F': [('I', 4), ('J', 9)],
    'G': [('H', 11), ('I', 8)],
    'H': [('I', 4)],
    'J': [('I', 13)],
    'K': [('J', 3)]
}

graph1 = Graph(adjacency_list1)
graph1.a_star_algorithm('A', 'D')

graph1 = Graph(adjacency_list2)
graph1.a_star_algorithm('A', 'I')