from datetime import datetime

from classes import (
    Car,
    Scooter,
    User,
    Vehicle,
    find_user,
    find_vehicle_by_id,
    generate_order_id,
    validate_float,
    validate_int,
)

# Member 3
def sign_in(users):
    pass


def create_account(users):
    pass


def user_menu(vehicles, current_user, all_orders):
    pass


def top_up_balance(current_user):
    pass


def change_password(current_user):
    pass


# Member 4
def show_my_orders(current_user):
    pass


def show_scooters_catalog(vehicles):
    pass


def show_cars_catalog(vehicles):
    pass


def print_receipt(order, battery_used, remaining_battery, updated_balance):
    pass


# Member 1
def rent_scooter(vehicles, current_user, all_orders):
    show_cars_catalog(vehicles)
    process_rental(vehicles, current_user, all_orders, Scooter)


def rent_car(vehicles, current_user, all_orders):
    show_cars_catalog(vehicles)
    process_rental(vehicles, current_user, all_orders, Car)


def process_rental(vehicles: list[Vehicle], current_user: User, all_orders: list, vehicle_class: Scooter | Car):
    vehicle_type = "Scooter" if vehicle_class is Scooter else "Car"
    vehicle_id = validate_int(f"Enter {vehicle_type} ID to rent (or 0 to go back) > ", 0)
    if vehicle_id == 0: return

    vehicle: Vehicle = find_vehicle_by_id(vehicles, vehicle_id)

    if vehicle is None or not isinstance(vehicle, vehicle_class):
        print('This vehicle does not exist!')
        return
    elif not vehicle.is_available():
        print('This vehicle is not available!')
        return
    elif vehicle.battery < Vehicle.MIN_BATTERY_FOR_RIDE:
        print(f"This vehicle does not have enough battery for ride!")
        return
    
    max_min = vehicle.max_possible_minutes()
    minutes = validate_int(f"Enter ride duration in minutes (1 - {max_min}), or 0 to cancel) > ", 0, max_min)

    if minutes == 0: return
    if minutes > max_min:
        print(f"Maximum duration for this vehicle is {max_min}")
        return
    
    cost = vehicle.calculate_cost(minutes) 
    formula = vehicle.get_pricing_formula(minutes)

    if current_user.balance < cost:
        print(f"You dont have enough money! You're short by {cost - current_user.balance}$")
        return

    print(f"Estimated cost: {cost}$")
    confirm = input("Confirm ride and payment? (y/n)> ").lower()
    if confirm != 'y': return

    current_user.deduct_balance(cost)
    battery_used = vehicle.consume_battery(minutes)
    order_id = generate_order_id(all_orders)

    order = {
        "order_id": order_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "user": current_user.username,
        "category": vehicle_type,
        "model": vehicle.model,
        "vehicle_id": vehicle.vehicle_id,
        "minutes": minutes,
        "formula": formula,
        "cost": cost
    }

    current_user.add_order(order)
    all_orders.append(order)
    print(order, battery_used, vehicle.battery, current_user.balance)




