class Vehicle:
    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


vehicle_type = input("Type of Vehicle: ")
vehicle_year = input("Enter the year: ")
vehicle_make = input("Enter manufacture: ")
vehicle_model = input("Enter the model: ")
vehicle_doors = input("Enter the Number of doors(2 or 4): ")
vehicle_roof = input("Enter type of roof(solid or sunroof): ")

vehicle_1 = Automobile(vehicle_type, vehicle_year, vehicle_make, vehicle_model, vehicle_doors, vehicle_roof)

print("\nVehicle Type: " + vehicle_type)
print("\nYear: " + vehicle_year)
print("\nMake: " + vehicle_make)
print("\nModel: " + vehicle_model)
print("\nNumber of Doors: " + vehicle_doors)
print("\nType of Roof: " + vehicle_roof)
