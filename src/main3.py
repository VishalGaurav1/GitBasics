class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

if __name__ == "__main__":
    patient1 = Patient("John Doe", 30, "Male")
    patient1.display_info()