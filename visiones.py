import random

inicio = [
    "Ser", "Convertirnos en", "Consolidarnos como", "Establecernos como",
    "Llegar a ser", "Ser reconocidos como"
]

tipo_org = [
    "una organizacion lider", "una referencia regional", "un modelo a seguir",
    "una entidad de impacto", "un agente de cambio", "una red solida",
    "un centro de excelencia", "un catalizador social"
]

foco = [
    "en el fortalecimiento comunitario", "en educacion transformadora",
    "en inclusion social", "en la sostenibilidad ambiental",
    "en la defensa de derechos", "en el desarrollo humano integral",
    "en la participacion ciudadana", "en la innovacion social"
]

tiempo = [
    "para el ano 2030", "en la proxima decada", "a largo plazo",
    "para las futuras generaciones", "en el futuro cercano",
    "dentro del ambito nacional", "a nivel local y global"
]

visiones = set()
while len(visiones) < 1000:
    vision = f"{random.choice(inicio)} {random.choice(tipo_org)} {random.choice(foco)} {random.choice(tiempo)}."
    visiones.add(vision)

for vision in visiones:
    print(vision)