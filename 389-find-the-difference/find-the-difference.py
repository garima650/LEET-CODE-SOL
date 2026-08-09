class Solution(object):
    def findTheDifference(self, s, t):
        # Convert string s into a list to allow item removal
        s_list = list(s)
        
        for char in t:
            if char in s_list:
                s_list.remove(char)
            else:
                return char
