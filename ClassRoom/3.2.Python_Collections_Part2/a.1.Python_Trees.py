# Basic Tree in Python

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(TreeNode(child_node))

    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()

# Usage
root = TreeNode('Root')
root.add_child('Child1')
root.add_child('Child2')
root.children[0].add_child('Grandchild1')
root.print_tree()
