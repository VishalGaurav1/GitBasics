class Person:

    def __init__(self,name,hometown):
        self.name=name
        self.hometown=hometown

    def intro(self,age):
        return f'Hello.My name is {self.name} and I am from {self.hometown}.I am {age}years old'

if __name__=="__main__":
    person1=Person('Ravi','Muz')
    print(person1.intro(30))