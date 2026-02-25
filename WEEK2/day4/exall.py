import string
import random
from datetime import date, datetime
from faker import Faker

# ==================== Exercise 1: Currencies ====================
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        raise TypeError("Unsupported type")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            raise TypeError("Unsupported type")
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
print(c1)
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
c1 += 5
print(c1)
c1 += c2
print(c1)
try:
    print(c1 + c3)
except TypeError as e:
    print(e)

# ==================== Exercise 2: Import ====================
def sum_two(a, b):
    print(a + b)

sum_two(3, 7)

# ==================== Exercise 3: String Module ====================
all_letters = string.ascii_letters
random_string = ""
for _ in range(5):
    random_string += random.choice(all_letters)
print(random_string)

# ==================== Exercise 4: Current Date ====================
def display_current_date():
    print(date.today())

display_current_date()

# ==================== Exercise 5: Time Until January 1st ====================
def time_until_new_year():
    now = datetime.now()
    print(datetime(now.year + 1, 1, 1) - now)

time_until_new_year()

# ==================== Exercise 6: Birthday And Minutes ====================
def minutes_lived(birthdate_str):
    diff = datetime.now() - datetime.strptime(birthdate_str, "%Y-%m-%d")
    print(f"You have lived approximately {int(diff.total_seconds() / 60)} minutes!")

minutes_lived("1995-06-15")

# ==================== Exercise 7: Faker Module ====================
faker = Faker()
users = []

def add_users(count):
    for _ in range(count):
        users.append({
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code()
        })

add_users(5)
for user in users:
    print(user)