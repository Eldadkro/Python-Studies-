class testing:
    def __init__(self,num):
        self.num = num
    
    @property
    def squre(self):
        return self.num**2
    @squre.setter
    def squre(self,num):
        self.num = num**0.5
    @property
    def sqrt(self):
        return self.num**(0.5)
    @sqrt.setter
    def sqrt(self,num):
        self.num = num
if __name__ == "__main__":
    a = testing(4)
    b = testing(4)
    a.squre = 2
    print(a.squre)
