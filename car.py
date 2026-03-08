class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.tires = "winter"
        self.color = "red"
        self.engine ="V8"
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model} is now running.")

    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.make} {self.model} has stopped.")

    def drive(self, distance):
        if self.is_running:
            print(f"Driving {distance} miles.")
        else:
            print("The car is not running. Start the car first.")

    def getTires(self):
        print(f"Tire is: {self.tires}")

    def setTires(self, newTires):
        self.tires = newTires
        print(f"Tires set to: {newTires}")

    def getcolor(self):
        print(f"get color:{self.color}")

    def setcolor(self, newcolor):
        self.color = newcolor
        print(f"set color:{self.color}")
        

    


tylers_car = car("Chevrolet", "Tahoe", 2024)


tylers_car.start()
tylers_car.drive(10)
tylers_car.stop()

tylers_car.getTires()
tylers_car.setTires("spring")
tylers_car.getTires()

    