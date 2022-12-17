class Person:
    def __init__(self, fullName: str, age: int):
        self.fullName = fullName
        self.age = age

    def __str__(self):
        return f'{self.fullName} {self.age}'

class Driver(Person):
    def __init__(self, fullName: str, age: int, experience: int):
        super().__init__(fullName, age)
        self.experience = experience

    def __str__(self):
        return f"{self.fullName} {self.experience}"


class Engine:
    def __init__(self, power, company):
        self.power = power
        self.company = company

    def __str__(self):
        return f'{self.power} {self.company}'

class Car:
    def __init__(self, carClass: str, engine: Engine, driver: Driver, marka: str):
        self.carClass = carClass
        self.engine = engine
        self.driver = driver
        self.marka = marka

    def start(self):
        print("Go!")

    def stop(self):
        print("Stop!")

    def turnRight(self):
        print("Go to right!")

    def turnLeft(self):
        print("Go to left!")

    def __str__(self):
        return f"{self.carClass} {self.engine} {self.driver} {self.marka}"

class Lorry(Car):
    def __init__(self, carClass: str, engine: Engine, driver: Driver, marka: str, carrying: int):
        super().__init__(carClass, engine, driver, marka)
        self.carrying = carrying

    def __str__(self):
        return f"{self.carrying}"

class SportCar(Car):
    def __init__(self, carClass: str, engine: Engine, driver: Driver, marka: str, speed: int):
        super().__init__(carClass, engine, driver, marka)
        self.speed = speed

    def __str__(self):
        return f"{self.speed}"

engine1 = Engine(power=1500, company='Yokohama')
person1 = Person(fullName="Zhassulan Issayev", age=20)
driver1 = Driver(fullName=person1.fullName,age=person1.age, experience=5)
lorry1 = Lorry(carClass="sedan",carrying=1000, driver=driver1, engine=engine1, marka="Toyota")
sport_car_1 = SportCar(carClass="sedan", engine=engine1, driver=driver1,marka="BMW", speed=130)

lorry1.start()
sport_car_1.stop()