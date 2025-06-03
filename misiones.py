import random

inicios = [
    "Promover", "Fomentar", "Contribuir a", "Desarrollar", "Impulsar",
    "Defender", "Fortalecer", "Garantizar", "Apoyar", "Transformar"
]

enfoques = [
    "el desarrollo social", "la educacion inclusiva", "la justicia ambiental",
    "los derechos humanos", "la participacion ciudadana", "la equidad de genero",
    "el acceso a la salud", "la sostenibilidad", "la innovacion comunitaria",
    "el bienestar de las comunidades vulnerables"
]

modos = [
    "a traves de programas colaborativos", "mediante la capacitacion continua",
    "por medio del activismo local", "a partir de proyectos de impacto",
    "con enfoque de derechos", "desde una perspectiva sostenible",
    "mediante alianzas estrategicas", "a traves de la investigacion aplicada",
    "usando tecnologia social", "en coordinacion con actores clave"
]

misiones = set()
while len(misiones) < 1000:
    mision = f"{random.choice(inicios)} {random.choice(enfoques)} {random.choice(modos)}."
    misiones.add(mision)

for mision in misiones:
    print(mision)