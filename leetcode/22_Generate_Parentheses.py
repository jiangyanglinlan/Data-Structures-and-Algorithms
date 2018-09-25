class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n <= 0:
            return result
        s = ' ' * 2 * n
        self.helper(result, s, n, n, 0)
        return result


    def helper(self, result, s, left_remind, right_remind, index):
        if index == len(s):
            result.append(s)
        if left_remind > 0:
            s = list(s)
            s[index] = '('
            s = ''.join(s)
            self.helper(result, s, left_remind-1, right_remind, index+1)
        if right_remind > left_remind:
            s = list(s)
            s[index] = ')'
            s = ''.join(s)
            self.helper(result, s, left_remind, right_remind-1, index+1)


s = Solution()
print(s.generateParenthesis(3))