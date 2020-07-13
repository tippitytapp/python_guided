class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = self.init_departments(departments)
    
    def __str__(self):
        output = f"{self.name} \n Departments: \n"
        for d in self.departments:
            output += "   id: " + d.get_id() + ", name: " + d.get_name() + "\n"
        return output

    def init_departments(self, departments):
        # instances = []
        # for i,d in enumerate(departments_:
        #     instances.append(Department(i + 1, d))
        # return instances
        return [Department(i + 1, d) for i, d in enumerate(departments)]


class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Department {self.id}: {self.name}"

    def get_id(self):
        return str(self.id)
    
    def get_name(self):
        return self.name

departments = [ "Running", "Fishing", "Baseball", "Basketball"]
my_store = Store("The Dugout", departments)

print(my_store)

## add a way for a user to select departments

# input("Select the department number\n 1) Running    2) Fishing   3) Baseball   4) Basketball:")

selection = int(input('Select a department number:'))

print(f"You selected Department: {selection}, {my_store.departments[selection-1].get_name()}")

# Theres no easy wy to access some department "outside" of our Store class
# take in a list of strings to create department instances for us