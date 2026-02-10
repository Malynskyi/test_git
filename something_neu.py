class Car:
    def __init__ (
        self,
        color: str,
        model: str,
        fuel_tank: int = 10
        ):


        self.color = color
        self.model = model
        self.fuel_tank = fuel_tank
        self.__consumption = 2
        self.__total_distance = 0 
        

    def move(self, distance: int = 0):
        if distance > 0:
            trip_consumption = distance * self.__consumption
            if self.fuel_tank >= trip_consumption:
                self.fuel_tank = self.fuel_tank - trip_consumption 
                self._service_check(trip_consumption)
                return distance
        else:
            trip_distance = self.fuel_tank / self.__consumption 
            self.fuel_tank = 0
            self._service_check(trip_distance)
            return trip_distance 
        return 0
    
    def _service_check(self, distance: int|float = 0):
        self.__total_distance += distance
        above_period_distance = self._total_distance // 100
        if above_period_distance >= 1:
            self.__consumption += above_period_distance 
    

first_car = Car('Green', 'BMW', 17)
second_car = Car('Red', 'Toyota', 13)
third_car = Car('Black', 'Volvo', 20)

# def refill(self, value):
#     if hasattr(self, 'fuel_tank') and value:
#         self.fuel_tank = value

# first_car.refill_tank = refill
breakpoint()

print(f'{first_car.model} проехал {first_car.move(20)}, осталось топлива {first_car.fuel_tank}')
first_car.refill_tank(first_car, 60)
print(first_car.fuel_tank)
# print(f'{second_car.model} проехал {second_car.move(2)}, осталось топлива {second_car.fuel_tank}')
# print(f'{third_car.model} проехал {third_car.move(3)}, осталось топлива{third_car.fuel_tank}')
# print(f'{second_car.model} проехал {second_car.move(15)}, осталось топлива {second_car.fuel_tank}')
# print(f'{third_car.model} проехал {third_car.move(25)}, осталось топлива {third_car.fuel_tank}')