class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in s:
            if i.isdigit():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        