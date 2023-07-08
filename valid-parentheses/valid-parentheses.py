class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tumpuk = []
        for c in s:
            if c in '([{':
                tumpuk.append(c)
            else:
                if not tumpuk or \
                    (c == ')' and tumpuk[-1] != '(') or \
                    (c == '}' and tumpuk[-1] != '{') or \
                    (c == ']' and tumpuk[-1] != '['):
                    return False
                tumpuk.pop()
        return not tumpuk 