# coding: utf-8

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node('A')
n1 = Node('B')
n2 = Node('C')
n3 = Node('D')
n4 = Node('E')

root.left = n1
root.right = n2
n1.left = n3
n1.right = n4

def pre_order(root, nodes):
    nodes.append(root.data)

    if root.left:
        pre_order(root.left, nodes)
    if root.right:
        pre_order(root.right, nodes)
    return nodes

if __name__ == "__main__":
    result = []
    pre_order(root, result)
    print(result)