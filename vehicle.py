import math

# Base Vehicle class
class Vehicle:
    def init(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._mileage = 0  # Encapsulated attribute
    
    def move(self, distance):
        raise NotImplementedError("Subclasses must implement move() method")
    
    def get_mileage(self):
        return self._mileage
    
    def describe(self):
        return f"{self.year} {self.make} {self.model} in {self.color}"
    
    def str(self):
        return self.describe()

# Car class inheriting from Vehicle
class Car(Vehicle):
    def init(self, make, model, year, color, fuel_type):
        super().init(make, model, year, color)
        self.fuel_type = fuel_type
        self.doors = 4  # Default value
    
    def move(self, distance):
        self._mileage += distance
        return f"Driving 🚗 for {distance} miles"
    
    def honk(self):
        return "Beep beep! 🎺"
    
    def describe(self):
        return f"{super().describe()} running on {self.fuel_type}"

# Airplane class inheriting from Vehicle
class Airplane(Vehicle):
    def init(self, make, model, year, color, wingspan, max_altitude):
        super().init(make, model, year, color)
        self.wingspan = wingspan
        self.max_altitude = max_altitude
        self.altitude = 0
    
    def move(self, distance):
        self._mileage += distance
        return f"Flying ✈️ for {distance} miles at {self.altitude} feet"
    
    def take_off(self):
        self.altitude = 10000
        return "Taking off! 🛫"
    
    def land(self):
        self.altitude = 0
        return "Landing! 🛬"
    
    def describe(self):
        return f"{super().describe()} with {self.wingspan}ft wingspan"

# Boat class inheriting from Vehicle
class Boat(Vehicle):
    def init(self, make, model, year, color, length, displacement):
        super().init(make, model, year, color)
        self.length = length
        self.displacement = displacement
        self.anchored = True
    
    def move(self, distance):
        if self.anchored:
            return "Can't move - anchor is down! ⚓"
        self._mileage += distance
        return f"Sailing 🚢 for {distance} nautical miles"
    
    def raise_anchor(self):
        self.anchored = False
        return "Anchor raised! ⚓"
    
    def drop_anchor(self):
        self.anchored = True
        return "Anchor dropped! ⚓"
    
    def describe(self):
        return f"{super().describe()} measuring {self.length}ft"

# Electric car specialization
class ElectricCar(Car):
    def init(self, make, model, year, color, battery_capacity):
        super().init(make, model, year, color, "electricity")
        self.battery_capacity = battery_capacity  # in kWh
        self.charge_level = 100  # percentage
    
    def charge(self, amount):
        self.charge_level = min(100, self.charge_level + amount)
        return f"Charged to {self.charge_level}% 🔌"
    
    def move(self, distance):
        # Electric cars consume about 0.3 kWh per mile
        energy_used = distance * 0.3
        if energy_used > self.battery_capacity * (self.charge_level / 100):
            return "Not enough charge! Please recharge. ⚡"
        
        self.charge_level -= (energy_used / self.battery_capacity) * 100
        self._mileage += distance
        return f"Silently driving 🔇 for {distance} miles, {self.charge_level:.1f}% charge remaining"

# Demonstration function
def demonstrate_vehicles():
    print("=== VEHICLE DEMONSTRATION ===\n")
    
    # Create various vehicles
    my_car = Car("Toyota", "Camry", 2022, "blue", "gasoline")
    my_plane = Airplane("Boeing", "737", 2018, "white", 117, 41000)
    my_boat = Boat("Bayliner", "Element", 2020, "red", 16, 1450)
  my_tesla = ElectricCar("Tesla", "Model 3", 2023, "black", 75)
    
    vehicles = [my_car, my_plane, my_boat, my_tesla]
    
    # Demonstrate polymorphism
    for vehicle in vehicles:
        print(f"{vehicle.describe()}")
        
        # Special actions based on vehicle type
        if isinstance(vehicle, Airplane):
            print(f"  - {vehicle.take_off()}")
        elif isinstance(vehicle, Boat):
            print(f"  - {vehicle.raise_anchor()}")
        
        # All vehicles can move (polymorphism)
        move_result = vehicle.move(50)
        print(f"  - {move_result}")
        
        # Show mileage (encapsulation)
        print(f"  - Mileage: {vehicle.get_mileage()} miles")
        
        # Special actions based on vehicle type
        if isinstance(vehicle, Car) and not isinstance(vehicle, ElectricCar):
            print(f"  - {vehicle.honk()}")
        elif isinstance(vehicle, ElectricCar):
            print(f"  - {vehicle.charge(25)}")
        
        print()

if name == "main":
    demonstrate_vehicles()
