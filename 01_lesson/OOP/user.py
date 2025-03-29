class User:
    
    age = 0;

    def __init__(self, name):
        print("я создался")
        print("Меня зовут: ", name)
        self.username = name

    def sayName(self):
        print("Меня зовут: ", self.username)

    def sayAge(self):
        print(self.Age)

    def setAge(self, newAge):
        self.Age = newAge


