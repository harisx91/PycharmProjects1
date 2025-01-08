class myfirstclass():

    def __init__(self,a,b):
        self.firsta = a
        self.firstb = b
        print("Hello World")

    def add_numb(self):
        print(self.firsta + self.firstb)

    def ok_string(self):
        print("string")


obj = myfirstclass(4,5)
obj.add_numb()
obj.ok_string()