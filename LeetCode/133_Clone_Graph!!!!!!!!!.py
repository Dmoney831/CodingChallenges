'''
Given a reference of a node in a connected undirected graph.
return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
'Hash Map'

'''

''''''
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


    def cloneGraph(node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val) 
            oldToNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node) if node else None
