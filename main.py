from faker import Faker

fake = Faker('es_MX')

for _ in range(300):
    print(fake.url())