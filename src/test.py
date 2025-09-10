class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def showInfo(self):
        print(self.name, self.age, self.sex)

class NewPerson(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.salary = 5000
    def showInfo(self):
        super().showInfo()
        print(self.salary)

new_person = NewPerson('Abc', 20, 'Male')
print(new_person.name, new_person.age, new_person.sex, new_person.salary)
new_person.showInfo()