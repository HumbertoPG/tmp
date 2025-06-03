import random

# Lista base
poblaciones = [
    "Comunidades urbano marginadas",
    "Comunidades rurales",
    "Comunidades indigenas",
    "Primera infancia (0 a 6 años)",
    "Niños y niñas de nivel primaria",
    "Niños, niñas y adolescentes",
    "Mujeres en situación vulnerable",
    "Adultos mayores",
    "Personas con discapacidad",
    "Personas con enfermedades cronicas/terminales",
    "Personas con problemas de adicciones",
    "Personas migrantes o situación de movilidad",
    "Otra"
]

# Generar 1000 organizaciones con 1–4 grupos atendidos
respuestas = []
for _ in range(1000):
    seleccionadas = random.sample(poblaciones, random.randint(1, 4))
    respuestas.append("; ".join(seleccionadas))

# Guardar en archivo

for i in respuestas:
    print(i)