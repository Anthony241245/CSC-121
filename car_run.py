import random

# Create Car class
class Car:
    # Create an initializer function
    def __init__(self, make, model, color, driver, max_speed, handling):
        self.make = make 
        self.model = model
        self.color = color
        self.driver = driver
        self.max_speed = max_speed 
        self.handling = handling
        self.miles_driven = 0

    def show_car_info(self):
        print(f"The {self.color} {self.make} {self.model} is driven by {self.driver}")

    def drive_car(self):
        self.miles_driven += random.randint(5, self.max_speed) + self.handling

    def show_stats(self, miles_to_win):
        print(f"{self.driver}'s car advanced {self.miles_driven} miles")
        print()
        if self.miles_driven >= miles_to_win:
            print(f"{self.driver} won the race !!!!")
        
    def hit_maxwell(self):
        hit = random.randint(1, 3)
        if hit == 1:
            print(f"🔥🔥🔥🙀 Maxwell was hit by {self.driver}")
            reduce_speed = random.randint(5, 20)
            self.max_speed -= reduce_speed
            print(f"Max speed reduced by {reduce_speed}")
            print()
        else:
            print("Maxwell managed to save himself")


def main():
    miles_to_win = 100
    # Create car objects
    muskCar = Car("Mazda", "Miata", "orange", "Elon Musk", 60, 11)
    bezoCar = Car("Nissan", "Sentra", "silver", "Jeff Bezos", 50, 12)

    print("The race is beginning.......")
    print("🏁🏁🏁")
    print()

    # Call the instance function show_car_info
    muskCar.show_car_info()
    print()
    bezoCar.show_car_info()

    while muskCar.miles_driven < miles_to_win and bezoCar.miles_driven < miles_to_win:
        # Drive both cars one time
        muskCar.drive_car()
        bezoCar.drive_car()

        # Show the updated status of the car
        print()
        muskCar.show_stats(miles_to_win)
        print()
        bezoCar.show_stats(miles_to_win)

        # Call the hit_maxwell method on both car objects
        muskCar.hit_maxwell()
        print()
        bezoCar.hit_maxwell()
        print()

    # After the loop ends, check who won
    if muskCar.miles_driven >= miles_to_win and bezoCar.miles_driven >= miles_to_win:
        print("It's a tie")
    elif muskCar.miles_driven >= miles_to_win:
        print("Elon Musk wins the race")
    else:
        print("Jeff Bezos wins the race")

    # Ask the player if they want to try again
    retry = input("Do you want to try again? (yes or no): ").lower()
    if retry != "yes":
        print("Thank you for playing!")


if __name__ == "__main__":
    main()


