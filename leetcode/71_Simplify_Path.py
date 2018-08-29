class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = []
        path = path.split('/')
        print(path)
        for i in path:
            if i == '.' or i == '':
                pass
            elif i == '..':
                if len(s) != 0:
                    s.pop()
            else:
                s.append(i)
        if len(s) == 0:
            return '/'
        else:
            print(s)
            result = ''
            for i in s:
                result += '/{}'.format(i)
            return result


s = Solution()
print(s.simplifyPath("/abc/..."))