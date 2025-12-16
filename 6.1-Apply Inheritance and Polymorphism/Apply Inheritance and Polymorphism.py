class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"car starting"
              f"make:{self.make}"
              f"\nmodel:{self.model}"
              f"\nyear:{self.year}")


class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def start(self):
        print(f"car starting"
              f"make:{self.make}"
              f"\nmodel:{self.model}"
              f"\nyear:{self.year}")


car1 = Car("toyota", "corolla", 2022)
car1.start()
ec_car1 = Electric_car("Tesla", "Model 3", 2023)
ec_car1.start()