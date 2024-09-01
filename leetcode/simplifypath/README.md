# Intuition
This would be far better solved by a linked list, as each time we specify a directory, we need to name it again. However... I used a tree, cuz why not

# Approach
We do a little cleanup first, then build a tree based on the paths specified. We then traverse the tree to find the last node we added to the tree, building a route along the way. What's returned is simply concatenated with '/' and returned.

# Complexity
- Time complexity: O(log(n))

- Space complexity: O(n)

# Code
```python3 []
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

        print(node.value)
        route = self.dfs(root, node)
        route = '/'.join(['' if not x else x for x in route])
        if route:
            return route
        else:
            return '/'

    def traverse(self, node, indent = ""):
        print(indent + str(node.value))
        indent += " "
        for child in node.children:
            self.traverse(child, indent)

    def dfs(self, node, wanted, route=[]):
        if node is None:  # Handle the case where node is None
            return None

        route = route + [node.value]
        if wanted == node:
            return route
        else:
            for i in node.children:
                result = self.dfs(i, wanted, route)
                if result:
                    return result
            return None  # Explicitly return None if not found in any child
    
    def deleteMultipleSlahes(self, path: str) -> str:
        newStr = ""
        previous = None
        for item in path:
            if not (previous and previous == '/' and item == previous):
                newStr += item
            previous = item
        return newStr
```