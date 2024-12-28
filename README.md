# Task 1. Pattern factory

The following code represents a simple system for creating vehicles. We have two classes: `Car` and `Motorcycle`. Each class has a `start_engine()` method that simulates the engine start of the corresponding vehicle. For now, to create a new vehicle, we simply create an instance of the corresponding class with the specified make and model.

```Python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

# Using
vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = Motorcyc ("Harley-Davidson", "Sportster")
vehicle2.start_engine()
```

The next step is to create vehicles based on the specifications of different regions, for example, for the US `US Spec` and the EU `EU Spec`.

Your task is to implement a factory pattern that will allow you to create vehicles with different regional specifications without changing the basic vehicle classes.

- Create an abstract base class `Vehicle` with the `start_engine()` method.
- Change the `Car` and `Motorcycle` classes so that they inherit from `Vehicle`.
- Create an abstract `VehicleFactory` class with the `create_car()` and `create_motorcycle()` methods.
- Implement two classes of the factory: `USVehicleFactory` and `EUVehicleFactory`. These factories should create cars and motorcycles with a region designation, for example, `Ford Mustang (US Spec)` for the United States, respectively.
- Modify the source code so that it uses the factories to create the vehicles.

## Expected result.

Code that allows you to easily create vehicles for different regions using the appropriate factories.

---

---
