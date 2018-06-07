class Vertex(object):

    def __init__(self,val,see=False):

        self.val = val
        self.connect = {}
        self.see = see
        self.dist = {}
        self.dist[self] = 0 
        self.path = {}

    def addNeighbor(self,V,weight):

        self.connect[V] = weight

    def __str__(self):

        return str(self.val) + ' ' + str([x.val for x in self.connect])

    def showPath(self,v):

        l = [v]

        while l[-1].val != self.val:
            cur_v = self.path[l[-1]]
            l.append(cur_v)

        return l


class Graph(object):

    def __init__(self):
        self.verlist = {}
        self.numVertices = 0

    def addVertex(self,val):

        self.numVertices += 1
        V = Vertex(val)
        self.verlist[val] = V
        return self.verlist

    def getVertex(self,n):

        if n in self.verlist:
            return self.verlist[n]
        else:
            return None

    def addEdge(self,f,t,cost=0):

        if f not in self.verlist:
            self.addVertex(f)
        if t not in self.verlist:
            self.addVertex(t)
        self.verlist[f].addNeighbor(self.verlist[t],cost)

    def DFS(self,vertex):

        vertex.see = True

        for v in vertex.connect:
            if not v.see:
                print(v)
                self.DFS(v)

    def BFS(self,vertex):

        queue = []
        queue.append(vertex)
        vertex.see = True

        while len(queue) != 0:
            cur_v = queue.pop(0)
            for v in cur_v.connect:
                if not v.see:
                    v.see = True
                    queue.append(v)
            print(cur_v)

    def unweighted(self,vertex):

        queue = [vertex]

        while len(queue) != 0:

            cur_v = queue.pop(0)

            for v in cur_v.connect:
                if v not in cur_v.dist and v.val != vertex.val:
                    vertex.dist[v] = vertex.dist[cur_v] + 1
                    vertex.path[v] = cur_v
                    queue.append(v)

if __name__ == '__main__':

    g = Graph()

    for i in range(5):
        g.addVertex(i)

    g.addEdge(0,1,100)
    g.addEdge(1,2,100)
    g.addEdge(2,5,100)
    g.addEdge(5,4,100)
    g.addEdge(4,3,100)
    g.addEdge(3,10,200)
    g.addEdge(10,0,200)

    # g.DFS(g.verlist[0])
    g.BFS(g.verlist[0])

    g.unweighted(g.verlist[0])

    dist = g.verlist[0].dist
    path = g.verlist[0].path

    for v in dist:
        print(v.val,'\t',dist[v])

    print(g.verlist[3])
    print(path[g.verlist[3]])

    l = (g.verlist[0].showPath(g.verlist[3]))
    print()
    for i in range(1,len(l)+1):
        print(l[-i])











