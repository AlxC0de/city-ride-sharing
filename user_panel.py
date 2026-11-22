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
    pass


def rent_car(vehicles, current_user, all_orders):
    pass


def process_rental(vehicles, current_user, all_orders, vehicle_class):
    pass