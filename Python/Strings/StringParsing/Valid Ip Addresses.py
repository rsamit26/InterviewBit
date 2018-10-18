"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255.
The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""

class Solution:

    def is_valid_ip(self, string):
        ip = string.split(".")
        for i in ip:
            if len(i) >3 or int(i) < 0  or int(i) > 255:
                return False
            if len(i) >1 and int(i) == 0:
                return False
            if len(i) >1 and int(i) != 0 and i[0] == '0':
                return False
        return True

    def conver_ip(self, string):
        n, iplist, ip = len(string), [], string
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    ip = ip[:k] + "." +ip[k:]
                    ip = ip[:j] + "." +ip[j:]
                    ip = ip[:i] + "." +ip[i:]
                    if self.is_valid_ip(ip):
                        iplist.append(ip)
                    ip = string
        return iplist
s = Solution()
p = "25525511135"
print(s.conver_ip(p))
