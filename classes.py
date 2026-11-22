# Member 1
class Vehicle:
    MIN_BATTERY_FOR_RIDE = 15.0
    DRAIN_PER_MIN = 1.0

    def __init__(self, vehicle_id, model, rate_per_min, battery=100.0, is_available=True):
        pass

    def get_status(self):
        pass

    def can_start_ride(self):
        pass

    def max_possible_minutes(self):
        pass

    def consume_battery(self, minutes):
        pass

    def calculate_cost(self, minutes):
        pass

    def get_pricing_formula(self, minutes):
        pass

    def __str__(self):
        pass


class Scooter(Vehicle):
    UNLOCK_FEE = 1.00
    DRAIN_PER_MIN = 1.5

    def __init__(self, vehicle_id, model, rate_per_min, battery, max_speed, is_available=True):
        pass

    def calculate_cost(self, minutes):
        pass

    def get_pricing_formula(self, minutes):
        pass

    def __str__(self):
        pass


class Car(Vehicle):
    INSURANCE_FEE = 2.00
    DISCOUNT_MINUTES = 30
    DISCOUNT_MULTIPLIER = 0.85
    DRAIN_PER_MIN = 0.8

    def __init__(self, vehicle_id, model, rate_per_min, battery, seats, is_available=True):
        pass

    def calculate_cost(self, minutes):
        pass

    def get_pricing_formula(self, minutes):
        pass

    def __str__(self):
        pass


class User:
    WELCOME_BONUS = 5.00

    def __init__(self, username, password, balance=WELCOME_BONUS):
        pass

    def check_password(self, password):
        pass

    def change_password(self, new_password):
        pass

    def add_balance(self, amount):
        pass

    def deduct_balance(self, amount):
        pass

    def add_order(self, order):
        pass

    def __str__(self):
        pass


# Member 2
def validate_int(message, min_val=None, max_val=None):
    pass


def validate_float(message, min_val=None, max_val=None):
    pass


def find_vehicle_by_id(vehicles, vehicle_id):
    pass


def find_user(users, username_input):
    pass


def generate_order_id(all_orders):
    pass