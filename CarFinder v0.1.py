def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

def print_authorized_vehicles(allowed_vehicles_list):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)

def main():
    allowed_vehicles_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    
    while True:
        display_menu()
        user_input = input()

        if user_input == '1':
            print_authorized_vehicles(allowed_vehicles_list)
        elif user_input == '2':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input, please enter 1 or 2.")

if __name__ == "__main__":
    main()
