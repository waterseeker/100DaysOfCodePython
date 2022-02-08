# You can also make classes that have **kwargs


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        self.color = kwargs["color"]


my_car = Car(make="Nissan", model="GT-R", color="Black")
print(my_car.model)
print(my_car.make)
print(my_car.color)


# if you don't include the kwargs used in the class, it'll cause a crash
# my_crashed_car = Car(make="BMW")
#
# you can use .get() on the props instead to avoid the crash. It will just return None if there isn't a value

class CarWithGet:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")


my_car_with_get = CarWithGet()
print(my_car_with_get.color)
