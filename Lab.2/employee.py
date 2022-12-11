import json

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

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

    def show_info(self):
        super().show_info()
        print("Profession:", self.profession)
        print("Salary:", self.salary)

    def save(self, json_filepath: str):
        to_json = {
            "name": self.fullname,
            "age": self.age,
            "profession": self.profession
            "salary": self.salary
        }
        with open(json_filepath, 'w') as file:
            json.dump(to_json, file)

    def load(self, json_filepath: str):
        with open(json_filepath) as file:
            obj = json.load(file)
            self.fullname = obj["fullname"]
            self.age = obj["age"]
            self.profession = obj["profession"]
            self.salary = obj["salary"]

