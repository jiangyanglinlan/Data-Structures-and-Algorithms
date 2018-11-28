'''
设计链表, 此题有一个坑点, addAtIndex(index,val) 方法如果 index 等于链表的长度，则该节点将附加到链表的末尾。
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self, val=None):
        """
        Initialize your data structure here.
        """
        self.head = Node(val)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        pre_check = self.pre_check(index)
        if pre_check is False:
            return -1
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        if node.val is None:
            return -1
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked lrist. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head.val is None:
            self.head.val = val
            return
        new_head_node = Node(val)
        new_head_node.next = self.head
        self.head = new_head_node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        head = self.head
        if head.val is None:
            head.val = val
            return
        new_node = Node(val)
        last_node = self.get_last_node()
        node = self.head
        last_node.next = new_node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        pre_check = self.pre_check(index)
        if pre_check is False and index != self.get_length():
            return None
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        pre_node = self.get_node(index - 1)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        pre_check = self.pre_check(index)
        if pre_check is False:
            return None
        node = self.head
        if index == 0:
            self.head = node.next
            return
        pre_node = self.get_node(index - 1)
        pre_node.next = pre_node.next.next

    def get_length(self):
        index = 0
        node = self.head
        if node.val is None:
            return 0
        while node is not None:
            index += 1
            node = node.next
        return index

    def get_last_node(self):
        '''
        得到最后一个元素
        '''
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    def pre_check(self, index):
        '''
        检查 index 是否越界
        '''
        length = self.get_length()
        if (index < 0) or (index > length - 1):
            return False
        return True

    def get_node(self, index):
        pre_check = self.pre_check(index)
        if pre_check is False:
            return None
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        return node