class inventions:
    def __init__(self, inventor):
        self.inventor = inventor

class light(inventions):
    def __init__(self, inventor, typeoflight, color):
        super().__init__(inventor = "Thomas Edison")
        self.color = color
        self.typeoflight = typeoflight

class vehicle(inventions):
    def __init__(self, inventor, topspeed, steering, lights, navigation, engine):
        super().__init__(inventor)
        self.topspeed = topspeed
        self.steering = steering
        self.lights = lights
        self.navigation = navigation
        self.engine = engine

    def getengine(self):
        print(f"get engine:{self.engine}")    
    
    def setengine(self, newengine):
        self.engine = newengine
        print(f"set engine:{self.engine}")

    def startvehicle(self):
        if self.navigation == "land":
            print("Starting on land")
        elif self.navigation == "sea":
            print("Sailing on sea")
        elif self.navigation == "air":
            print("Flying in the air")


class car(vehicle):
    def __init__(self, make, model, year, inventor, topspeed=100, steering="car", lights="LED", navigation="land", engine="V8"):
        super().__init__(inventor, topspeed, steering, lights, navigation, engine)
        self.make = make
        self.model = model
        self.year = year
        self.tires = "winter"
        self.color = "red"
        
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

    