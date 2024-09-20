class Calculator:
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def addition(self):
        return self.x+self.y
    
    def sub(self):
        return self.y-self.x

    def multi(self):
        return self.x*self.y

    def divi(self):
        return self.x//self.y

obj=Calculator(10,20)
res=obj.addition()
print(res)
