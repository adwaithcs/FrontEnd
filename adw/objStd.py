class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        
    def Grade(self,name,mark):
        if mark>90:
            mark="A+"
        elif mark>80 and mark<90:
            mark='A'
        elif mark>70 and mark<80:
            mark='B+'
        elif mark>60 and mark<70:
            mark='B'
        print('Name:',name,'\nGrade:',mark)
        
obj=Student("Arun",85)
obj.Grade('Arun',85)