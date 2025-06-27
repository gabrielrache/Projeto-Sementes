from faker import Faker

faker = Faker()

class Usuario:

    def __init__(self):
        self.id = 0
        self.first_name = faker.first_name()
        self.last_name = faker.last_name()
        self.username = self.first_name.lower() + self.last_name.lower()
        self.email = faker.email()
        self.password = faker.password()
        self.phone = faker.phone_number()
        self.userStatus = faker.random_int(0, 10, 1)

    def get_username(self):
        return self.username