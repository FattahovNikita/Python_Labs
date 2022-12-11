import json
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("Name:", self.fullname)
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
            self.fullname = obj["name"]
            self.age = obj["age"]