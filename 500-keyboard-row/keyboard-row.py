class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l=[]
        for i in words:
            f=s=t=0
            for j in i:
                if j.lower() in "qwertyuiop":
                    f+=1
                elif j.lower() in "asdfghjkl":
                    s+=1
                else:
                    t+=1
            if((f>0 and s==0 and t==0 ) or (f==0 and s>0 and t==0) or (f==0 and s==0 and t>0)):
                l.append(i)
        return(l)

        