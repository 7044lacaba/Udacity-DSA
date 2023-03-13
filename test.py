class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Set up tree
start = Node(4)
start.left = Node(2)

print(start.right)
print(start.right.value)
