# inheritance is defining hierarchical relationships

class Animal:
    def __init__(self,name, hunger, diet):
        self.name = name
        self.hunger = hunger
        self.diet = diet

    def eat(self, food):
        if food > 0 and self.hunger < 25:
            self.hunger += food


class Dog(Animal):
    def __init__(self, breed, isIndoor):
        super().__init__(self,name, hunger, diet)
        self.breed = breed
        self.isIndoor = isIndoor

    def fetch(self, ballX, ballY):
        move(ballX, ballY)
