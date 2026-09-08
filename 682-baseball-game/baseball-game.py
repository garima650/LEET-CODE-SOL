class Solution(object):
    def calPoints(self, operations):
        ops=[]
        for i in operations:

            if i =="D":
                ops.append(2*ops[-1])
            elif i=="C":
                ops.pop()
            elif i=="+":
                ops.append(ops[-1]+ops[-2])
            else:
                ops.append(int(i))

        return sum(ops)
        

        