class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])
        for i in range(1,len(elements)):
            root.add_child(elements[i])
        return root

if __name__ == '__main__':
    my_name = ["G", "E", "L", "A", "M", "A", "R", "I", "C", "O", "N", "B", "S", "E", "N", "O"]
    my_name_tree = build_tree(my_name)

    print("Input letters:", my_name)
    print("Min:", my_name_tree.find_min())
    print("Max:", my_name_tree.find_max())
    print("In Order Traversal:", my_name_tree.in_order_traversal())
    print("Pre Order Traversal:", my_name_tree.pre_order_traversal())
    print("Post Order Traversal:", my_name_tree.post_order_traversal())

