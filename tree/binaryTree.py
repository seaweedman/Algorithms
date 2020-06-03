class Node():
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

class BinaryTree():
    def __init__(self, root):
        self._root = root
        
    # 先序遍历 根左右
    def pre_order(self, tree):
        if tree == None:
            return False
        print(tree._data)
        self.pre_order(tree._left)
        self.pre_order(tree._right)

    # 后序遍历 左右根
    def pos_order(self, tree):
        if tree == None:
            return False
        self.pos_order(tree._left)
        self.pos_order(tree._right)
        print(tree._data)

    # 中序遍历 左根右
    def mid_order(self, tree):
        if tree == None:
            return False
        self.mid_order(tree._left)
        print(tree._data)
        self.mid_order(tree._right)

    # 层次遍历
    def row_order(self):
        queue = [self._root]
        while queue:
            node = queue.pop(0)
            print(node._data)
            if node._left:
                queue.append(node._left)
            if node._right:
                queue.append(node._right)
 
if __name__ == "__main__":
    root = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F')))
    tree = BinaryTree(root)
    print("- 先序遍历 -")
    tree.pre_order(tree._root)
    print("- 后序遍历 -")
    tree.pos_order(tree._root)
    print("- 中序遍历 -")
    tree.mid_order(tree._root)
    print("- 层次遍历 -")
    tree.row_order()
