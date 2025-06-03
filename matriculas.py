import random

def generar_matricula():
    numero = random.randint(1000, 9999)
    return f"A0173{numero}"

matriculas = set()
while len(matriculas) < 1000:
    matriculas.add(generar_matricula())

for i in matriculas:
    print(i)