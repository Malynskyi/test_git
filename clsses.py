class Car:
    def __init__(self, color, model, fuel_tank):
        self.model = model
        self.fuel_tank = fuel_tank
        self.consumption = 2
        

    def move(self, distance=0):
        if distance > 0:
            trip_consumption = distance * self.consumption
            if self.fuel_tank >= trip_consumption:
                self.fuel_tank = self.fuel_tank - trip_consumption 
                return (self.fuel_tank, distance)
        else:
            trip_distance = self.fuel_tank / self.consumption 
            self.fuel_tank = 0
            return trip_distance 
        return 0
    
first_car = Car('Green', 'BMW', 17)
second_car = Car('Red', 'Toyota', 13)
third_car = Car('Black', 'Volvo', 20)

print(f'{first_car.model} проехал {first_car.move(3)}, осталось топлива {first_car.fuel_tank}')
print(f'{second_car.model} проехал {second_car.move(2)}, осталось топлива {second_car.fuel_tank}')
print(f'{third_car.model} проехал {third_car.move(3)}, осталось топлива{third_car.fuel_tank}')
# breakpoint()