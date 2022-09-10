from unreliable_car import UnreliableCar

def main():
    reliable = UnreliableCar("Reliable Car", 100, 100)
    unreliable = UnreliableCar("Unreliable Car", 100, 20)

    for i in range(1, 4):
        print(f"Driving attempts {i} km")
        print(f"{reliable.name} drove {reliable.drive(i)} km")
        print(f"{unreliable.name} drove {unreliable.drive(i)} km")

    print(reliable)
    print(unreliable)

main()