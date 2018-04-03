"""
   Execution:  python breadth_first_paths.py G s

   Data files:   https://algs4.cs.princeton.edu/41graph/tinyCG.txt
                 https://algs4.cs.princeton.edu/41graph/tinyG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumG.txt
                 https://algs4.cs.princeton.edu/41graph/largeG.txt

   Run breadth first search on an undirected graph.
   Runs in O(E + V) time.

   %  python grapy.py tinyCG.txt
   6 8
   0: 2 1 5
   1: 0 2
   2: 0 1 3 4
   3: 5 4 2
   4: 3 2
   5: 3 0

   % python breadth_first_paths.py tinyCG.txt 0
   0 to 0:  0
   0 to 1:  0-2-1
   0 to 2:  0-2
   0 to 3:  0-2-3
   0 to 4:  0-2-3-4
   0 to 5:  0-2-3-5

"""
from algs4.stack import Stack
from algs4.queue import Queue
from algs4.graph import Graph


class BreadthFirstPaths:

    def __init__(self, G, s):
        self._marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.s = s
        self.bfs(G, s)

    def bfs(self, G, s):
        self._marked[s] = True
        queue = Queue()
        queue.enqueue(s)
        while not queue.is_empty():
            v = queue.dequeue()
            for w in G.adj[v]:
                if not self._marked[w]:
                    self.edge_to[w] = v
                    self._marked[w] = True
                    queue.enqueue(w)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            x = self.edge_to[x]
        path.push(self.s)
        return path

if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    s = int(sys.argv[2])
    V = int(f.readline())
    E = int(f.readline())
    g = Graph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)
    dfs = BreadthFirstPaths(g, s)
    for v in range(g.V):
        if dfs.has_path_to(v):
            print("%d to %d: " % (s, v), end='')
            for x in dfs.path_to(v):
                if x == s:
                    print(x, end='')
                else:
                    print('-%s' % x, end='')
            print()
        else:
            print("%d and %d: not connected" % (s, v))
