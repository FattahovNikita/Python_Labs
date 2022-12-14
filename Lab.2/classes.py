import json

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def Name(self):
        return self.name

    @property
    def Age(self):
        return self.age

    def __str__(self):
        return f"Person name is  {self.name}, age is {self.age}"
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


    def save(self, json_filepath: str):
        to_json = {
            "name": self.name,
            "age": self.age,
        }
        with open(json_filepath, 'w') as file:
            json.dump(to_json, file)

    def load(self, json_filepath: str):
        with open(json_filepath) as file:
            obj = json.load(file)
            self.name = obj["name"]
            self.age = obj["age"]

class Employee(Person):

    def __init__(self, name, age, profession, salary):
        super().__init__(name, age)
        self.profession = profession
        self.salary = salary
    @property
    def Profession(self):
        return self.profession

    @property
    def Salary(self):
        return self.salary

    def __str__(self):
        return f"Employee name is {self.name}, age is {self.age}, profession is {self.profession}, salary is {self.salary}"

    def __repr__(self):
        return f"Employee(name='{self.name}', age={self.age}, profession='{self.profession}', salary={self.salary})"

    def save(self, json_filepath: str):
        to_json = {
            "name": self.name,
            "age": self.age,
            "profession": self.profession,
            "salary": self.salary
        }
        with open(json_filepath, 'w') as file:
            json.dump(to_json, file)

    def load(self, json_filepath: str):
        with open(json_filepath) as file:
            obj = json.load(file)
            self.name = obj["name"]
            self.age = obj["age"]
            self.profession = obj["profession"]
            self.salary = obj["salary"]