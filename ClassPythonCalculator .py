from math import sqrt
class Calculator:
    def __init__(self, side, hyp):
        self.side = side
        self.hyp = hyp
    def getInput(self):
        print("Welcome! Please start by choosing which side of the right triangle you want to calculate")
        while True:
            try:
                options = int(input("Which side of the right triangle do you want to solve? \nType 0 to quit, Type 1 for Side, Type 2 for Hypotenuse: "))
                while options < 0 or options > 2:
                    print("Enter a valid number!")
                    options = int(input("Which side of the right triangle do you want to solve? \nType 0 to quit, Type 1 for Side, Type 2 for Hypotenuse: "))
                break
            except ValueError:
                print("Enter a valid number!")
        if options == 0:
            quit()
        if options == 1:
            self.side = float(input("Enter the side value: "))
            self.hyp = float(input("Enter the hypotenuse value: "))
            sideOBJ = SideCalculator(self.side, self.hyp)
            sideOBJ.side_calculator()
            print(sideOBJ.__str__())
        if options == 2:
            self.side = float(input("Enter a side value: "))
            hypOBJ = HypCalculator(self.side, None)
            hypOBJ.hyp_calculator()
            print(hypOBJ.__str__())

class SideCalculator(Calculator):
    def __init__(self, side, hyp):
        super().__init__(side, hyp)
    def side_calculator(self):
        self.answer = round(sqrt(self.hyp **2 - self.side ** 2 ), 2)
    def __str__(self):
        return f"The side is {self.answer}"

class HypCalculator(Calculator):
    def __init__(self, side, side2):
        super().__init__(side, None)
        self.side2 = side2
    def hyp_calculator(self):
        self.side2 = float(input("Enter another side value: "))
        self.answer = round(sqrt(self.side **2 + self.side2 ** 2), 2)
    def __str__(self):
        return f"The hypotenuse is {self.answer} "
        
calOBJ = Calculator(None, None)
calOBJ.getInput()