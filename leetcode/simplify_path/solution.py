class Node:
    def __init__(self, parent = None):
        self.parent = parent
        self.children = []
        self.value = None

class Solution:
    def simplifyPath(self, path: str) -> str:
        deletedMultipleSlashes = self.deleteMultipleSlahes(path)
        slashesSplit = deletedMultipleSlashes.split('/')
        emptiesRemoved = [x for x in slashesSplit if x]
        root = Node()
        node = root
        for i in emptiesRemoved:
            if i == '.':
                pass
            elif i == '..':
                if node.parent:
                    node = node.parent
            else:
                found = False
                foundAt = 0
                for index, j in enumerate(node.children):
                    if j.value == i:
                        found, foundAt = True, index
                        break
                if not found:
                    n = Node(parent = node)
                    n.value = i
                    node.children.append(n)
                    node = n
                else:
                    node = node.children[foundAt]
        self.traverse(root)
        
    def traverse(self, node, indent = ""):
        print(indent + str(node.value))
        indent += " "
        for child in node.children:
            self.traverse(child, indent)

    def dfs(self, node, wanted):
        path = 
        
    def deleteMultipleSlahes(self, path: str) -> str:
        newStr = ""
        previous = None
        for item in path:
            if not (previous and previous == '/' and item == previous):
                newStr += item
            previous = item
        return newStr