import random
# Create Car class

class Car:
    # Create an initializer function
    def __init__(self, make, model, color, driver, max_speed, handling):
        self.make = make 
        self.model = model
        self.color = color
        self.color = color
        self.driver = driver
        self.max_speed = max_speed 
        self.handling = handling
        self.miles_driven = 0

    def show_car_info(self):
        print(f"The {self.color} {self.make} {self.model} is driven by {self.driver} ")

    
    
    def drive_car(self):
        self.miles_driven += random.randint(5,self.max_speed) + self.handling

    
    def show_stats(self, miles_to_win):
        print(f"{self.driver}'s car advanced {self.miles_driven} mph")
        print()
        if self.miles_driven >= miles_to_win:
            print(f"{self.driver} won the race !!!!")
        
    def hit_maxwell(self):
        hit = random.randint(1,3)
        if hit == 1:
            print(f"🔥🔥🔥🙀 Maxwell was hit by {self.driver}")
            reduce_speed = random.randint(5,20)
            self.max_speed -= reduce_speed
            print(f"Max speed reduced by {reduce_speed}")
            print()
        else:
            print("Maxwell managed to save himself")
        







def main():
    miles_to_win = 100
    # Create a car object
    muskCar = Car("Mazda", "Miata", "orange", "Elon Musk", 60, 11)
    # Create a second car
    bezoCar = Car("Nissan", "Sentra", "silver", "Jeff Bezos", 50, 12)
    
    print("The race is beginning.......")
    print("🏁🏁🏁")
    print()
     # Call  the instance function show_car_info
    muskCar.show_car_info()
    print()
    bezoCar.show_car_info()
    while muskCar.miles_driven < 100 and bezoCar.miles_driven:
        # Drive both Cars one time
        muskCar.drive_car()
        bezoCar.drive_car()

        # Show the updated status of the car
        print()
        muskCar.show_stats(miles_to_win)
        bezoCar.show_stats(miles_to_win)

        # Call the hit_maxwell method on both car onjects
        muskCar.hit_maxwell()
        bezoCar.hit_maxwell()
        
        
    


if __name__ == "__main__":
    main()

