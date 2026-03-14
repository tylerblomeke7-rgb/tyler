class car:
    def __init__(self, make, model, year):
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

class sedan(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)   # calls the parent constructor
        self.numDoors = 4

class coupe(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)   # calls the parent constructor
        self.numDoors = 2
        self.topOpen = False

    def openTop(self):
        if not self.topOpen:
            self.topOpen = True
            print(f"The {self.year} {self.make} {self.model} top is now open.")
        else:
            print(f"The {self.year} {self.make} {self.model} top is already open.")

    def closeTop(self):
        if self.topOpen:
            self.topOpen = False
            print(f"The {self.year} {self.make} {self.model} top is now closed.")
        else:
            print(f"The {self.year} {self.make} {self.model} top is already closed.")

    


tylers_car = coupe("Mazda", "Miata", 1997)
shazaibs_car = sedan("Honda", "Civic", 2020)

tylers_car.start()
shazaibs_car.start()

tylers_car.openTop()
tylers_car.closeTop()   

shazaibs_car.getTires()
shazaibs_car.setTires("summer")
shazaibs_car.getcolor()
shazaibs_car.setcolor("blue")

tylers_car.stop()
tylers_car.getTires()
tylers_car.setTires("all-season")
tylers_car.getcolor()
tylers_car.setcolor("black")