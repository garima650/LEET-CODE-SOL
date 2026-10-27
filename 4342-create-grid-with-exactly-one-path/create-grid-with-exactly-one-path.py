class Solution(object):
    def createGrid(self, m, n):
        result = []
        for i in range(m):
            if i == 0:
                result.append("." * n)
            else:
                result.append("#" * (n-1) + ".")
        
        return result