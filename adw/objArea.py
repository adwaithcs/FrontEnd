class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
        
    def myArea(self,l,b):
        area=l*b
        print('Area=',area)
        
obj=Rectangle(20,5)

obj.myArea(20,5)
    
        