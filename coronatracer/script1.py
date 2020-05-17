#The file containing the graph class
#This scrpt contains the graph class
#q2
class Graph:
    def __init__(self,edges=[]):
        self.vertexList = VertexList(edges)
        for e in edges:
            self.addEdge(e)
            self.addEdge((e[1],e[0]))
    def addEdge(self,edge):
        vertex = self.vertexList.locate(edge[0])
        edgelist = vertex.edges
        if edgelist != None:
            edgelist.add(edge[1])
        else:
            edgelist = EdgeList(edge[1])
        vertex.setEdges(edgelist)
    def __iter__(self):
        vertices = self.vertexList
        for v in vertices:
            x = vertices.locate(v)
            y = x.edges
            if y != None:
                for z in y:
                    yield (v,z)
    def insertVertex(self,item):
        if not (item in self.vertexList):
            self.vertexList.append(item)
    def deleteVertex(self,item):
        return self.vertexList.remove(item)
    def insertEdge(self,edge):
        self.vertexList.addVertex(edge)
        self.addEdge(edge)
        self.addEdge((edge[1],edge[0]))
    def deleteEdge(self,edge):
        self.__deleteEdge(edge)
        self.__deleteEdge((edge[1],edge[0]))
    def __deleteEdge(self,edge):
        if not (edge[0] in self.vertexList):
            print("There is no edge", edge)
            return False
        vertexlocation = self.vertexList.locate(edge[0])
        edgelist = vertexlocation.getEdges()
        if edgelist == None:
            print("There is no edge", edge)
            return False
        res = edgelist.remove(edge[1])
        if res == False:
            print("There is no edge", edge)
        return res
    def outgoingEdges(self,item):
        vertex = self.vertexList.locate(item)
        if vertex == None:
            print("There is no vertex", item)
            return []
        edgelist = vertex.getEdges()
        if edgelist == None:
            return []
        res = []
        for v in edgelist:
            res.append((item,v))
        return res

    def bfs(self,vertex):
        if not (vertex in self.vertexList):
            print("There is no vertex", vertex)
            return None
        length = self.vertexList.getlength()
        distance = [None] * length
        parent = [None] * length
        index = self.vertexList.index(vertex)
        distance[index] = 0
        parent[index] = vertex
        currentlayer = Fifo(length)
        currentlayer.pushback(vertex)
        nextlayer = Fifo(length)
        for l in range(length):
            for u in currentlayer:
                print(u)
                loc = self.vertexList.locate(u)
                edgelist = loc.getEdges()
                if edgelist != None:
                    for v in edgelist:
                        idx = self.vertexList.index(v)
                        if parent[idx] == None:
                            nextlayer.pushback(v)
                            distance[idx] = l + 1
                            parent[idx] = u
            currentlayer = nextlayer
            nextlayer = Fifo(length)
        return (distance,parent)
    #The modified bfs with queue
    def bfsq(self,vertex):
        if not (vertex in self.vertexList):
            print("There is no vertex", vertex)
            return None
        length = self.vertexList.getlength()
        distance = [None] * length
        parent = [None] * length
        index = self.vertexList.index(vertex)
        distance[index] = 0
        parent[index] = vertex
        q = Fifo(length)
        q.pushback(vertex)
        while not q.isEmpty():
            curr=q.popfront()
            print(curr)
            indx= self.vertexList.index(curr)
            loc = self.vertexList.locate(curr)
            edgelist = loc.getEdges()
            if edgelist != None:
                for i in edgelist:
                    idx = self.vertexList.index(i)
                    if parent[idx] == None:
                        q.pushback(i)
                        distance[idx] = distance[indx] + 1
                        parent[idx] = i
        return (distance,parent)





    def allDFS(self):
        numVertices = self.vertexList.getlength()
        initlist = [None]* numVertices
        self.tree = PyList(initlist,numVertices)
        for i in range(numVertices):
            newgraph = Graph([])
            self.tree[i] = newgraph
        for s in self.vertexList:
            self.mark = [None] * numVertices
            self.dfsPos = 1
            self.dfsNum = [1] * numVertices
            self.finishingTime = 1
            self.finishTime = [1] * numVertices
            idx = self.vertexList.index(s)
            if self.mark[idx] == None:
                self.mark[idx] = s
                self.dfsNum[idx] = self.dfsPos
                self.dfsPos += 1
                self.dfs(s,s,idx)
    def dfs(self,vertex1,vertex2,index):
        for e in self.outgoingEdges(vertex2):
            idx = self.vertexList.index(e[1])
            if self.mark[idx] != None:
                self.__traverseNontreeEdge(e)
            else:
                self.tree[index].insertEdge(e)
                self.__traverseTreeEdge(e)
                self.mark[idx] = e[1]
                self.dfs(vertex2,e[1],index)
        self.backtrack(vertex1,vertex2)
    def __traverseTreeEdge(self,e):
        idx = self.vertexList.index(e[1])
        self.dfsNum[idx] = self.dfsPos
        self.dfsPos += 1
    def __traverseNontreeEdge(self,e):
        self.dfsPos = self.dfsPos
    def backtrack(self,vertex1,vertex2):
        idx = self.vertexList.index(vertex2)
        self.finishTime[idx] = self.finishingTime
        self.finishingTime += 1

class VertexList:
    class  __Vertex:
        def __init__(self,item,next=None,previous=None):
            self.item=item
            self.next=next
            self.previous=previous
            self.edges=None
        def getItem(self):
            return self.item
        def getNext(self):
            return self.next
        def getPrevious(self):
            return self.previous
        def getEdges(self):
            return self.edges
        def setItem(self,item):
            self.item = item
        def setNext(self,next):
            self.next = next
        def setPrevious(self,previous):
            self.previous = previous
        def setEdges(self,edge):
            self.edges = edge

    def __init__(self,edges=[]):
        self.dummy = VertexList.__Vertex(None,None,None)
        self.numVertices = 0
        self.dummy.setNext(self.dummy)
        self.dummy.setPrevious(self.dummy)
        for e in edges:
            self.addVertex(e)
    def __iter__(self):
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            yield cursor.getItem()
    def append(self,item):
        lastVertex = self.dummy.getPrevious()
        newVertex = VertexList.__Vertex(item,self.dummy,lastVertex)
        lastVertex.setNext(newVertex)
        self.dummy.setPrevious(newVertex)
        self.numVertices += 1
    def __contains__(self,item):
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            vertex = cursor.getItem()
            if vertex == item:
                return True
        return False
    def locate(self,vertex):
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            item = cursor.getItem()
            if vertex == item:
                return cursor
    def addVertex(self,edge):
        node1 = edge[0]
        node2 = edge[1]
        if not (node1 in self):
            self.append(node1)
        if not (node2 in self):
            self.append(node2)
    def remove(self,item):
        cursor = self.dummy
        location = None
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            vertex = cursor.getItem()
            edgelist = cursor.edges
            if edgelist != None:
                if item in edgelist:
                    print(item, "cannot be deleted, as it appears in an edge.")
                    return False
            if vertex == item:
                location = cursor
        if location == None:
            print(item, "is not a vertex.")
            return False
        nextVertex = location.getNext()
        prevVertex = location.getPrevious()
        prevVertex.setNext(nextVertex)
        nextVertex.setPrevious(prevVertex)
        self.numVertices -= 1
        return True
    def index(self,item):
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            if cursor.getItem() == item:
                return i
        return -1
    def getlength(self):
        return self.numVertices
class EdgeList:
    class __Edge:
        def __init__(self,item,next=None,previous=None):
            self.item=item
            self.next=next
            self.previous=previous
        def getItem(self):
            return self.item
        def getNext(self):
            return self.next
        def getPrevious(self):
            return self.previous
        def setItem(self,item):
            self.item = item
        def setNext(self,next):
            self.next = next
        def setPrevious(self,previous):
            self.previous = previous

    def __init__(self,edge):
        self.first = EdgeList.__Edge(edge,None,None)
        self.first.setNext(self.first)
        self.first.setPrevious(self.first)
        self.numEdges = 1
    def add(self,edge):
        lastEdge = self.first.getPrevious()
        newEdge = EdgeList.__Edge(edge,self.first,lastEdge)
        lastEdge.setNext(newEdge)
        self.first.setPrevious(newEdge)
        self.numEdges += 1
    def __iter__(self):
        cursor = self.first
        for i in range(self.numEdges):
            yield cursor.getItem()
            cursor = cursor.getNext()
    def __contains__(self,item):
        cursor = self.first
        for i in range(self.numEdges):
            vertex = cursor.getItem()
            if vertex == item:
                return True
            cursor = cursor.getNext()
        return False
    def insertEdge(self,edge):
        self.vertexList.addVertex(edge)
        self.addEdge(edge)
        self.addEdge((edge[1],edge[0]))
    def deleteEdge(self,edge):
        self.__deleteEdge(edge)
        self.__deleteEdge((edge[1],edge[0]))
    def __deleteEdge(self,edge):
        if not (edge[0] in self.vertexList):
            print("There is no edge", edge)
            return False
        vertexlocation = self.vertexList.locate(edge[0])
        edgelist = vertexlocation.getEdges()
        if edgelist == None:
            print("There is no edge", edge)
            return False
        res = edgelist.remove(edge[1])
        if res == False:
            print("There is no edge", edge)
            return res


    def remove(self,item):
        cursor = self.first
        for i in range(self.numEdges):
            vertex = cursor.getItem()
            if vertex == item:
                nextVertex = cursor.getNext()
                prevVertex = cursor.getPrevious()
                prevVertex.setNext(nextVertex)
                nextVertex.setPrevious(prevVertex)
                self.numEdges -= 1
                if (cursor == self.first):
                    self.first = nextVertex
                return True
            cursor = cursor.getNext()
        return False
class Fifo:
    def __init__(self,size=20):
        self.items = [None] * size
        self.first = 0
        self.last = -1
        self.size = size
        self.length = 0
    def isEmpty(self):
        if self.length != 0:
            return False
        return True
    def front(self):
        if self.length != 0:
            return self.items[self.first]
        raise ValueError("Queue is empty")
    def back(self):
        if self.length != 0:
            return self.items[self.last]
        raise ValueError("Queue is empty")
    def pushback(self,item):
        if self.length == self.size:
            self.allocate()
        self.last = (self.last + 1) % self.size
        self.items[self.last] = item
        self.length += 1
    def popfront(self):
        if self.size > 20 and self.length == self.size / 4:
            self.deallocate()
        if self.length != 0:
            frontelement = self.items[self.first]
            self.first = (self.first + 1) % self.size
            self.length -= 1
            return frontelement
        raise ValueError("Queue is empty")
    def __iter__(self):
        rlast = self.first + self.length
        for i in range(self.first,rlast):
            yield self.items[i % self.size]
    def allocate(self):
        newlength = 2 * self.size
        length = self.length
        newQueue = [None] * newlength
        for i in range(self.size):
            pos = (i + self.first) % self.size
            newQueue[i] = self.items[pos]
        self.items = newQueue
        self.first = 0
        self.last = self.size - 1
        self.size = newlength
        self.length = length
    def deallocate(self):
        newlength = self.size // 2
        length = self.length
        newQueue = [None] * newlength
        length = self.length
        for i in range(length):
            pos = (i + self.first) % self.size
            newQueue[i] = self.items[pos]
        self.items = newQueue
        self.first = 0
        self.last = length - 1
        self.size = newlength
        self.length = length
    
