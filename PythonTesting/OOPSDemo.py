#class are users defined blueprint or prototype

class Calculator:
    num = 100 ##class variable
    #Construct is a method that is automatically called
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def sums(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.sums())

obj1 = Calculator(4,5) #syntax to create objects in python
obj1.getData()
print(obj1.num)