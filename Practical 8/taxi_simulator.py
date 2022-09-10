from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "(Q)uit, (C)hoose taxi, (D)rive"

def main():

    total = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi:"))

            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

            print(f"Bill to date: ${total}")
            print(MENU)
            choice = input(">>>").upper()

        elif choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)

                if current_taxi == taxis[0]:
                    trip_fare = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_fare}")
                    total += trip_fare

                elif current_taxi == taxis[1] or current_taxi == taxis[2]:
                    trip_fare = current_taxi.get_price()
                    print(f"Your {current_taxi.name} trip cost you ${trip_fare}")
                    total += trip_fare

                print(f"Bill to date: ${total}")
                print(MENU)
                choice = input(">>>").upper()
            else:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${total}")
                print(MENU)
                choice = input(">>>").upper()
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>>").upper()

    print(f"Total trip cost: ${total}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()

