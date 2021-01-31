# class Person:
#     def __init__(self,name,height,weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.blood_color = "RED"

#     # def get_height(self):
#     #     return self.__height
    
#     def get_weight(self):
#         return self.weight

#     def get_BMI(self):
#         return (self.weight*self.weight)/self.__height

#     def get_bloodcolor(self):
#         return self.blood_color

# p1 = Person("Nikhil",163,50)
# p2 = Person("Mou",140,40)
# print(p1.height)

# class car:
#     __maxspeed=0
#     __name=""
#     def __init__(self):
#         self.__maxspeed=200
#         self.__name="supercar"
#     def drive(self):
#         print("driving")
#         print(self.__maxspeed)
#     def setspeed(self,speed):
#         self.__maxspeed=speed
#         print(self.__maxspeed)
# redcar=car()
# redcar.drive()
# redcar.setspeed(100)  

# class dog:
#     def sound(self):
#         print("bow bow")
# class cat:
#     def sound(self):
#         print("meow")
# #def makesound(animaltype):
    
#     #animaltype.sound()
# catobj=cat()
# dogobj=dog()
# catobj.sound()
# dogobj.sound()

class pow(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def pow(self):
        return self.x**self.y
    def __str__(self):
        return "[" + str(self.x)+"^"+str(self.y) + "]"
pr=pow(3,4)
print(pr.pow())
pr2=pow(9,2)
print(pr2.pow())
print(pr)
print(pr2)
print(pr.pow()==pr2.pow())