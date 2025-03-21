class Car:
    def start(self):
        self.__check_engine()
        self.__ignite_fuel()
        print("Car Started!")

    def __check_engine(self):
        print("Checking engine...")

    def __ignite_fuel(self):
        print("Igniting fuel...")

car1 = Car()
car1.start()