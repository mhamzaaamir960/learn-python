class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return f"{self.__brand}!!!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petorl or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_toyota = Car("Toyota","Corolla")
print(f"Toyota fuel type: {my_toyota.fuel_type()}")

# my_tesla = ElectricCar("Tesla", "Model 3", "90kwh")
# print(f"Tesls fuel type: {my_tesla.fuel_type()}")
