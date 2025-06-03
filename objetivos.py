import random

# Verbos de acción comunes
verbos = [
    "Impulsar", "Mejorar", "Fortalecer", "Promover", "Desarrollar",
    "Aumentar", "Implementar", "Garantizar", "Reducir", "Apoyar"
]

# Áreas de impacto
temas = [
    "la educacion comunitaria", "el acceso a servicios de salud",
    "la participacion ciudadana", "la equidad de genero",
    "la sostenibilidad ambiental", "los derechos de grupos vulnerables",
    "la innovacion social", "la formacion de liderazgos juveniles",
    "la integracion social", "el desarrollo rural"
]

# Complementos de propósito
propositos = [
    "mediante programas locales",
    "con acciones colaborativas",
    "a traves de alianzas estrategicas",
    "por medio de capacitaciones",
    "con enfoque territorial",
    "mediante politicas publicas inclusivas",
    "en comunidades marginadas",
    "a partir de evidencia",
    "de forma sostenible",
    "con participacion activa de la comunidad"
]

# Generar 1,000 frases de objetivos
objetivos = set()
while len(objetivos) < 1000:
    objetivo = f"{random.choice(verbos)} {random.choice(temas)} {random.choice(propositos)}."
    objetivos.add(objetivo)

for objetivo in objetivos:
    print(objetivo)