

class Solution:
    def calPoints(self, operations):
        rec = []
        
        for op in operations:
            if op == "+":
                # Add the sum of the last two scores
                rec.append(rec[-1] + rec[-2])
            elif op == "D":
                # Double the last score
                rec.append(2 * rec[-1])
            elif op == "C":
                # Invalidate/remove the last score
                rec.pop()
            else:
                # Value is an integer string, convert and add it
                rec.append(int(op))
                
        return sum(rec)
