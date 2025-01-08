from OOPSDemo import Calculator


class Childclass(Calculator):
    num2 = 200

    def __int__(self,a, b):
        Calculator.__init__(self,2,10)


    def getCompleteData(self):
        return self.num2 + self.num + self.sums()


obj = Childclass()

print(obj.getCompleteData())