from abc import ABC, abstractmethod
from pprint import pprint
import csv



class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    # def __str__(self):
    #     return f"name: {self.name}, price: {self.price}, flavor: {self.flavor}, frosting: {self.frosting}, filling: {self.filling}, sprinkles: {self.sprinkles}, size: {self.size}"
    
    # @abstractmethod
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
    
    # @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price
    


class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

class Regular(Cupcake):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

class Large(Cupcake):
    size = "large"
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        

cupcake3 = Mini("Berry Blast",3.95,"mixed berry","purple")
cupcake3.add_sprinkles("blue","red")
cupcake4 = Regular("Chocolate Crisis",5.97,"chocolate","chocolate","chocolate")
cupcake4.add_sprinkles("chocolate","white chocolate")
cupcake5 = Large("Poppyseed Punisher",9.95,"vanilla","white")

cupcake_seed = [
    cupcake3,
    cupcake4,
    cupcake5
]

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

# read_csv("sample.csv")

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size,"name": cupcake.name,"price": cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting,"sprinkles":cupcake.sprinkles,"filling":cupcake.filling})
            elif hasattr(cupcake,"sprinkles"):
                writer.writerow({"size": cupcake.size,"name": cupcake.name,"price": cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting,"sprinkles":cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size,"name": cupcake.name,"price": cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting})

# write_new_csv("new_sample.csv", cupcake_seed)
# read_csv("new_sample.csv")

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None


def add_cupcake(file, cupcake):
    with open(file,"a",newline="\n") as csvfile:
        fieldnames = ["size","name","price","flavor","frosting","sprinkles","filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake,"filling"):
            writer.writerow({"size": cupcake.size,"name": cupcake.name,"price": cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting,"sprinkles":cupcake.sprinkles,"filling":cupcake.filling})
        elif hasattr(cupcake,"sprinkles"):
            writer.writerow({"size": cupcake.size,"name": cupcake.name,"price": cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting,"sprinkles":cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size,"name": cupcake.name,"price": cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting})


def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
    
    



# cupcake1 = Cupcake("Chocolate Chip", 1.99, "vanilla", "chocolate", "chocolate chips", "regular")
# print(cupcake1)

# cupcake1.size = "mini"
# print(cupcake1)

# cupcake1.contains_nuts = False
# print(cupcake1.contains_nuts)

# cupcake1.add_sprinkles("Red", "White", "Blue")
# print(cupcake1.sprinkles)

# cupcake2 = Mini("Strawberry Burst", 0.99, "strawberry", "pink")
# print(cupcake2.size)
# print(cupcake2.name)
# print(cupcake2.filling)

