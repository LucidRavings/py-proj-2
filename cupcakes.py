class Cupcake:
    def __init__(self, name, price, flavor, frosting, filling, size):
        self.name = name
        self.price = float(price)
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        self.size = size

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, flavor: {self.flavor}, frosting: {self.frosting}, filling: {self.filling}, sprinkles: {self.sprinkles}, size: {self.size}"

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

cupcake1 = Cupcake("Chocolate Chip", 1.99, "vanilla", "chocolate", "chocolate chips", "regular")
print(cupcake1)

cupcake1.size = "mini"
print(cupcake1)

cupcake1.contains_nuts = False
print(cupcake1.contains_nuts)

cupcake1.add_sprinkles("Red", "White", "Blue")
print(cupcake1.sprinkles)
