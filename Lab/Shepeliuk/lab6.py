#Task 1
class Car:
    mark = ''
    color = ''
    engineCapacity = ''

    def driveBack(self):
        return print('Drive back')
    
    def driveForward(self):
        return print('Drive forward')

mers=Car()
# mers.driveForward()

#Task 2
class NewCar(Car):
    def turnRight(self):
        return print('Turn Right')
    
    def turnLeft(self):
        return print('Turn Left')

obj = NewCar()
# obj.driveForward()

#Task 3
class Plane():
    model = ''

    def fly(self):
        return print('Fly')

obj2 = Plane()
# obj2.fly()

#Task 4 
class Gibrid(NewCar,Plane):
    model=''

obj3 = Gibrid()
obj3.driveForward()
obj3.turnLeft()
obj3.fly()