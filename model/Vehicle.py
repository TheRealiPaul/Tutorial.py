class Vehicle:
    brand = ""
    model = ""
    color = ""
    price = 10000

    def description(self):
        result = "%s is model of %s and the color is %s" %(self.brand, self.model, self.color)
        return result

my_car = Vehicle()
my_car.brand = "Toyota"
my_car.color = "red"
my_car.model = "RAV4"

print(my_car.description())