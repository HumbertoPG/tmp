from faker import Faker
fake = Faker('es_MX')
Faker.seed(42)          # reproducible

def nombre_empresa():
    base = fake.company()                     # p. ej. “Soluciones Innovadoras S.A.”
    # quitamos acentos y agregamos un sufijo social
    limpio = (base
              .replace("á","a").replace("é","e")
              .replace("í","i").replace("ó","o")
              .replace("ú","u"))
    return f"{limpio} Social"

# generar 300 nombres únicos
empresas = {nombre_empresa() for _ in range(800)}   # generamos de más y nos quedamos con 300
empresas = list(empresas)[:300]

# ejemplo rápido
for e in empresas:
    print(e)
