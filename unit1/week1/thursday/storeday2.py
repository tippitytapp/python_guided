from product import Equipment, Clothing

class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    
    def __str__(self):
        output = f"{self.name} \n Departments: \n"
        for id in self.departments:
            output += "   id: " + str(id) + ", name: " + self.departments[id].get_name() + "\n"
        return output

    # def init_departments(self, departments):
    #     # instances = {}
    #     # for key, value in departments.items():
    #     #     instances[key] = Department(key, value)
    #     # return instances
    #     # return [Department(i + 1, d) for i, d in enumerate(departments)]
    #     return {key: Department(key, value)for key, value in departments.items()}


class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"Department {self.id}: {self.name}"

    def get_id(self):
        return str(self.id)
    
    def get_name(self):
        return self.name
    
    def print_products(self):
        for p in self.products:
            print(p)

# departments = [ 
#     ("Running", 101).
#     ("Fishing", 103),
#     ("Baseball", 45),
#     ("Basketball", 87)
# ]

# You can easily look up a department by its id
# departments[103] => "fishing"
# So we get efficient lookup for our departments
departments = {
    101: Department("Running", [Clothing("Running Shorts", 15, "Cotton", "Black")]),
    103: Department("Fishing", [Equipment("Rod", 200, 1, "Fishing")]),
    45: Department("Baseball", [Equipment('Bat', 50, 2, "Baseball")]),
    87: "Basketball"
}

products = [
    Clothing("Football Jersey", 20, "Jersey Knit", "Red"),
    Equipment('Bat', 50, 2, "Baseball"),
    Equipment("Rod", 200, 1, "Fishing")
]
my_store = Store("The Dugout", departments)

print(my_store)

## add a way for a user to select departments

# input("Select the department number\n 1) Running    2) Fishing   3) Baseball   4) Basketball:")

selection = int(input('Select a department number:'))

print(f"You selected Department: {selection}, {my_store.departments[selection].get_name()}")

# Theres no easy wy to access some department "outside" of our Store class
# take in a list of strings to create department instances for us