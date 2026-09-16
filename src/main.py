class Calculator:

    def add(self,a,b):
        return a+b

    def multiply(self,a,b):
        return a*b


if __name__=="__main__":
    calc=Calculator()
    print(f"2+3={calc.add(2,3)}")
    print(f"3*4={calc.multiply(3,4)}")