class Calculator:

    def add(self,a,b):
        return a+b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b==0:
            return 'Error:Division by 0'
        return a/b


if __name__=="__main__":
    calc=Calculator()
    print(f"2+3={calc.add(2,3)}")
    print(f"3*4={calc.multiply(3,4)}")
    print(f"10/2={calc.divide(10,2)}")