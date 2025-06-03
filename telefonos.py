import random

cantidad  = 1000
telefonos = random.sample(range(2_000_000_000, 10_000_000_000), cantidad)

with open("telefonos.txt", "w") as f:
    for t in telefonos:
        f.write(f"{t}\n")

print("Listo, 1000 teléfonos únicos en 'telefonos.txt'")
