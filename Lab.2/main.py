from classes import *

Human = Employee("Zach Hill", 23, "Musician", 100000)

Human.save("Human_data.json")
print("Employee information saved\n")

Test = Employee("Test", 0, "Test", 0)
Test.load("Human_data.json")
print("Emloyee information loaded\n")
Test.show_info()
