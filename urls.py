from faker import Faker

fake = Faker('es_MX')

nombres = set()
while len(nombres) < 1000:
    nombres.add(fake.url())

for i in nombres:
    print(i)