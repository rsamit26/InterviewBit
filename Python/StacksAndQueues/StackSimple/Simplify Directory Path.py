"""
Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
"""


class Solution:

    def directory_path(self, path):
        curr, stack = '', []
        path = path + "/"
        for p in path:  # use sentinal value to simplify the logic
            if p != '/':
                curr += p
            elif curr:
                if curr == '..' and stack:  # execute ".." operation
                    stack.pop()
                elif curr not in ('.', '..'):  # add result to stack when curr is not an operator
                    stack.append(curr)
                curr = ''
        return '/' + '/'.join(stack)


s = Solution()
string = "/../"
print(s.directory_path(string))
