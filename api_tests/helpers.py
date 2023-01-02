from faker import Faker


def get_random_id(min_value, max_value):
    faker = Faker()
    random_int = faker.random_int(min_value, max_value)
    return random_int
