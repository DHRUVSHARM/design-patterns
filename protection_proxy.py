# generic car class
class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car being driven by {self.driver.name}')

class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        # real call 
        self.car = Car(driver)

    # proxy function
    def drive(self):
        if self.driver.age >= 16:
            self.car.drive()
        else:
            print('Driver too young')

# generic driver class
class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    basic_car = Car(Driver('abc' , 12))
    basic_car.drive()
    
    # a proxy here behaves almost like an extra layer that encapsulates part of something, basically routing it through it first
    # like a real proxy
    # request -> carproxy -> it makes some protection checks then makes the request for you to car -> drivers
    # ultimately this gives us the advantage of not changing the client side code and still being able to add functionality 
    car = CarProxy(Driver('John', 12))
    car.drive()