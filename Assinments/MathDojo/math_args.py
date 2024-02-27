class MathDojo:
    def __init__(self):
        self.result = 0
        

    def add(self , num , *nums):
        theSum = num
        for n in nums:
            theSum += n
        self.result += theSum
        return self

    def subtract(self , num , *nums):
        theSub = num
        for n in nums:
            theSub -= n
        self.result = theSub
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).add(3,2).result
print(x)

y = md.subtract(10).subtract(7,3,1).subtract(4,4).result
print (y)
f= md.subtract(4,2,5,6,7,8).result
print (f)