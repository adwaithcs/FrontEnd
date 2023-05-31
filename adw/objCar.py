class Car:
    def __init__(self,brand,model,year):
        self.make=brand
        self.model=model
        self.year=year
        
    def myCar(self,brand,model,year):
        cars={}
        cars['Brand']=self.make
        cars['Model']=self.model
        cars['Year']=self.year
        print(cars)
        
obj=Car('NISSAN','SKYLINE',1994)
obj.myCar('NISSAN','SKYLINE',1994)
