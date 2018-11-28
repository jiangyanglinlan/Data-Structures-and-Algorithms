'''
使用两个队列, A 队列只保存一个元素-栈顶的元素, B 队列保存剩下的元素。
push: 如果 A 队列为空说明栈为空, 将数据添加到 A 队列中
pop: 如果 A 队列为空说明栈为空, 返回 None, 否则返回 A 队列中的元素, 然后将 B 队列的元素入到 A 队列, 再将 A 队列的元素除队尾外全部入到 B 队列
top: 如果 A 队列为空说明栈为空, 返回 None, 否则返回 A 队列队首元素值
empty:  如果 A 队列为空说明栈为空, 返回 True, 否则返回 False
'''
from queue import Queue


class MyStack:
    def __init__(self):
        self.left_stack = Queue()
        self.right_stack = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.right_stack.empty() is True:
            self.right_stack.put(x)
        else:
            self.left_stack.put(self.right_stack.get())
            self.right_stack.put(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.right_stack.empty() is True:
            return None
        else:
            element = self.right_stack.get()
            size = self.left_stack.qsize()
            while self.left_stack.empty() is False:
                self.right_stack.put(self.left_stack.get())
            for i in range(size-1):
                self.left_stack.put(self.right_stack.get())
            return element


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.right_stack.empty() is True:
            return None
        else:
            element = self.right_stack.get()
            self.right_stack.put(element)
            return element


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.right_stack.empty() is True:
            return True
        else:
            return False



        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()

s = MyStack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print(s.empty())
print(s.pop())
print(s.pop())
print(s.top())
print(s.pop())
print(s.top())
s.push(5)
print(s.top())
print(s.pop())