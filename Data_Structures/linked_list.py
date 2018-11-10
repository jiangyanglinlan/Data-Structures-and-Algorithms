class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, list_node=None):
        self.head = list_node

    def is_empty(self):
        '''
        判断链表是否为空
        '''
        return self.head is None

    def get_length(self):
        '''
        得到链表长度
        '''
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index

    def get_node(self, index):
        '''
        得到指定下标的节点
        '''
        node = self.head
        for i in range(0, index):
            node = node.next
        return node

    def get(self, index):
        '''
        得到指定 index 的值
        '''
        self.pre_check(index)
        return self.get(index).data

    def set(self, index, value):
        '''
        设置指定 index 的值
        '''
        self.pre_check(index)
        current_node = self.get_node(index)
        current_node.data = value

    def insert(self, index, value):
        '''
        指定下标插入值
        '''
        self.pre_check(index)
        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        pre_node = self.get_node(index - 1)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def remove(self, index):
        self.pre_check(index)
        if index == 0:
            self.head = self.head.next
            return
        pre_node = self.get_node(index - 1)
        pre_node.next = pre_node.next.next

    def pre_check(self, index):
        '''
        检查 index 是否越界
        :param index: 
        :return: 
        '''
        length = self.get_length()
        if (index < 0) or (index > length - 1):
            raise IndexError('index is invalid')

    def get_last_node(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head.next = new_node
        else:
            last_node = self.get_last_node()
            last_node.next = new_node

    def _node_at_index(self, index):
        i = 0
        node = self.head
        while node is not None:
            if i == index:
                return node
            node = node.next
            i += 1
        return None

    def get_all_nodes(self):
        node = self.head
        all_nodes = []
        while node is not None:
            all_nodes.append(node)
            node = node.next
        return all_nodes


l = LinkedList(ListNode(1))
l.append(2)
l.append(3)
l.append(4)
l.append(4)
l.append(5)
l.append(6)

l.remove(3)

all_nodes = l.get_all_nodes()
for node in all_nodes:
    print(node.data)