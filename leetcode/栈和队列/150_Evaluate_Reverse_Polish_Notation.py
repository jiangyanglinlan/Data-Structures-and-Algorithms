'''
这题如果遍历到数字就入栈，遍历到运算符就出栈两次计算出结果并入栈。
'''

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                second_num = int(s.pop())
                first_num = int(s.pop())
                if i == '+':
                    sum = first_num + second_num
                elif i == '-':
                    sum = first_num - second_num
                elif i == '*':
                    sum = first_num * second_num
                else:
                    sum = int(first_num / second_num)
                s.append(sum)
            else:
                s.append(i)
        return int(s.pop())


s = Solution()
print(s.evalRPN(["18"]))
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))