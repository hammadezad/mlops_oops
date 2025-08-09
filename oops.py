# initiate a class



class employee:
    def __init__(self, name, id, departmnet, salary, designation):
        print("1. This is the first print for the class")
        self.name = name
        self.id = id
        self.departmnet = departmnet
        self.salary = salary
        self.designation = designation
        print("2. this is the second print")
    def travel(self, destination, name):
        print(f"My name is {name}")
        print(f"Employee is now travelling to {destination}")


first = employee("sam", 123, "engineering", 50000, "ml")  

# print(first.designation)

first.travel("Sahiwal", "Hammad")

print(type(first))