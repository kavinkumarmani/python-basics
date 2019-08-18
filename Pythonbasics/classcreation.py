
class car:
    
    wheels=4
    
    def __init__(self,colour):
        print("parent class constructor")
        self.colour=colour
    
    def test(self):
        print("test method")
    
    def setprice(self,price):
        self.price=price
    
    def getprice(self):
        return self.price

c1=car("red")
print(c1.wheels)
print(car.wheels)
c1.test()
c1.setprice(900)
c1.getprice()