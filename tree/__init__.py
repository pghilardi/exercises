

# Tree algorithms

# 1: depth first search

#########################################################################################################

def dfs(root):
    if root is None:
        return

    dfs(root.left)
    print(root.data)
    dfs(root.right)


# Calculate the LCA of a three

class Tree:

    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def dfs_path(root, data):
    path = []
    to_visit = []
    to_visit.insert(0, root)
    while to_visit:
        visited = to_visit.pop(0)
        print(visited.data)

        if visited.data == data:
            return path

        path.append(visited.data)

        if visited.left:
            to_visit.append(visited.left)

        if visited.right:
            to_visit.append(visited.right)

    return None


node_4 = Tree()
node_4.data = 4

node_6 = Tree()
node_6.data = 6

node_7 = Tree()
node_7.data = 7

node_5 = Tree()
node_5.data = 5
node_5.left = node_6
node_5.right = node_7

node_2 = Tree()
node_2.data = 2
node_2.left = node_4
node_2.right = node_5

r = Tree()
r.data = 1
r.left = node_2

dfs_path(r, 5)
dfs_path(r, 2)
dfs(r)


