class NodeWithFlag(object):
    def __init__(self, node, value):
        self.node = node
        self.flag = value


class BinaryTree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def traversal_with_recursion(self):
        """
        前序遍历(递归实现)
        """
        print(self.data)
        if self.left is not None:
            self.left.traversal_with_recursion()
        if self.right is not None:
            self.right.traversal_with_recursion()

    def traversal_with_stack(self):
        '''
        前序遍历(栈实现)
        '''
        node_stack = list()
        node_stack.append(self)
        while len(node_stack) != 0:
            node = node_stack.pop()
            print(node.data)
            if node.right is not None:
                node_stack.append(node.right)
            if node.left is not None:
                node_stack.append(node.left)

    def traversal_with_stack2(self):
        '''
        前序遍历 2(栈实现, 不需要将左节点压栈)
        '''
        node_stack = list()
        node_stack.append(self)
        node = self
        while len(node_stack) != 0:
            print(node.data)
            if node.right is not None:
                node_stack.append(node.right)
            if node.left is not None:
                node = node.left
            else:
                node = node_stack.pop()

    def in_order_traversal_with_stack(self):
        '''
        中序遍历(栈实现)
        :return:
        '''
        node_stack = list()
        node = self
        while len(node_stack) != 0 or node is not None:
            if node is not None:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                print(node.data)
                node = node.right

    def post_order_traversal_with_two_stacks(self):
        '''
        后序遍历(使用两个栈实现)
        :return:
        '''
        s1 = list()
        s2 = list()
        if self is None:
            return
        s1.append(self)
        while len(s1) != 0:
            node = s1.pop()
            s2.append(node)
            if node.left is not None:
                s1.append(node.left)
            if node.right is not None:
                s1.append(node.right)

        while len(s2) != 0:
            current_node = s2.pop()
            print(current_node.data)

    def post_order_traversal_with_one_stack(self):
        '''
        后续遍历(使用一个栈实现)
        '''
        node_stack = list()
        current_node = self
        new_node = NodeWithFlag(None, None)
        while len(node_stack) != 0 or current_node is not None:
            while current_node is not None:
                new_node = NodeWithFlag(current_node, False)
                node_stack.append(new_node)
                current_node = current_node.left

            new_node = node_stack.pop()
            current_node = new_node.node

            if new_node.flag is False:
                new_node.flag = True
                node_stack.append(new_node)
                current_node = current_node.right
            else:
                print(current_node.data)
                current_node = None

    def reverse(self):
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()


if __name__ == '__main__':
    t = BinaryTree(0)
    left = BinaryTree(1)
    right = BinaryTree(2)
    t.left = left
    t.right = right
    # 遍历
    t.traversal_with_recursion()
    t.post_order_traversal_with_two_stacks()
    print('------')
    t.post_order_traversal_with_one_stack()