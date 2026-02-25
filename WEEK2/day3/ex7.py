from faker import Faker

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