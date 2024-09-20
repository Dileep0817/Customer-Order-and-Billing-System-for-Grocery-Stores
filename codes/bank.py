class Bank:

    def __init__(self,name,p,t,r):
        self.name=name
        self.principle=p
        self.tenure=t
        self.roi=r
        
    def info(self):
        print(self.name,self.principle)

    def sinterest(self):
        return (self.principle * self.tenure * self.roi)//100
    
    
