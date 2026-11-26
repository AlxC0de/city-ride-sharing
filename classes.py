# Member 1
class Vehicle:
    MIN_BATTERY_FOR_RIDE = 15.0
    DRAIN_PER_MIN = 1.0

    def __init__(
        self, vehicle_id, model, rate_per_min, battery=100.0, is_available=True
    ):
        self.vehicle_id = vehicle_id
        self.model = model
        self.rate_per_min = rate_per_min
        self.battery = battery
        self.is_available = is_available

    def get_status(self):
        if not self.is_available: return "MAINTENANCE"
        elif self.battery < self.MIN_BATTERY_FOR_RIDE: return "LOW BATTERY"
        else: return "AVAILABLE"

    def can_start_ride(self):
        return self.is_available and self.battery >= self.MIN_BATTERY_FOR_RIDE

    def max_possible_minutes(self):
        return int(self.battery // self.DRAIN_PER_MIN)

    def consume_battery(self, minutes):
        used = round(minutes * self.DRAIN_PER_MIN, 1)
        self.battery = max(0, round(self.battery - used, 1))
        return used

    def calculate_cost(self, minutes):
        return round(minutes * self.rate_per_min, 2)

    def get_pricing_formula(self, minutes):
        return f"{minutes} min * ${self.rate_per_min:.2f}/min"

    def __str__(self):
        return f"{self.model} (ID: {self.vehicle_id}) | Battery: {self.battery:.0f}% | Rate: ${self.rate_per_min:.2f}/min | Status: {self.get_status()}"


class Scooter(Vehicle):
    UNLOCK_FEE = 1.00
    DRAIN_PER_MIN = 1.5

    def __init__(
        self, vehicle_id, model, rate_per_min, battery, max_speed, is_available=True
    ):
        super().__init__(vehicle_id, model, rate_per_min, battery, is_available)
        self.max_speed = max_speed

    def calculate_cost(self, minutes):
        return round(self.UNLOCK_FEE + (minutes * self.rate_per_min), 2)

    def get_pricing_formula(self, minutes):
        return f"${self.UNLOCK_FEE:.2f} unlock + ({minutes} min * ${self.rate_per_min:.2f}/min)"

    def __str__(self):
        return f"[Scooter] {super().__str__()} | Max Speed: {self.max_speed} km/h"


class Car(Vehicle):
    INSURANCE_FEE = 2.00
    DISCOUNT_MINUTES = 30
    DISCOUNT_MULTIPLIER = 0.85
    DRAIN_PER_MIN = 0.8

    def __init__(
        self, vehicle_id, model, rate_per_min, battery, seats, is_available=True
    ):
        super().__init__(vehicle_id, model, rate_per_min, battery, is_available)
        self.seats = seats

    def calculate_cost(self, minutes):
        cost = self.INSURANCE_FEE + (minutes * self.rate_per_min)
        if minutes >= self.DISCOUNT_MINUTES:
            cost = cost * self.DISCOUNT_MULTIPLIER
        return round(cost, 2)

        
    def get_pricing_formula(self, minutes):
        formula = f"${self.INSURANCE_FEE:.2f} insurance + ({minutes} min * ${self.rate_per_min:.2f}/min)"

        if minutes >= self.DISCOUNT_MINUTES:
            return f"{formula} - 15% Long-Ride Discount"

        return formula

    def __str__(self):
        return f"[Car] {super().__str__()} | Seats: {self.seats}"


class User:
    WELCOME_BONUS = 5.00

    def __init__(self, username, password, balance=WELCOME_BONUS):
        self.username = username
        self.password = password
        self.orders = []
        self.balance = round(float(balance), 2)

    def check_password(self, password):
        return self.password == password

    def change_password(self, new_password):
        self.password = new_password

    def add_balance(self, amount):
        self.balance = round(self.balance + amount, 2)

    def deduct_balance(self, amount):
        self.balance = round(self.balance - amount, 2)

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"User: {self.username} | Balance: ${self.balance:.2f} | Rides: {len(self.orders)}"


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
