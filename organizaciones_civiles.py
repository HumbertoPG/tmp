import random

nombres_base = [
    "Fundacion", "Asociacion", "Colectivo", "Centro", "Movimiento", "Red", "Alianza", "Consejo", "Comunidad", "Frente"
]

temas = [
    "Esperanza", "Justicia", "Tecnologia Social", "Medio Ambiente", "Educacion Abierta",
    "Salud Comunitaria", "Pueblos Originarios", "Mujeres Unidas", "Juventud Creativa",
    "Cultura Viva", "Derechos Humanos", "Diversidad e Inclusion", "Innovacion Ciudadana",
    "Igualdad", "Desarrollo Humano", "Cambio Social", "Paz y Democracia"
]

ubicaciones = [
    "de Mexico", "del Norte", "Latinoamericana", "de Occidente", "del Sur", "del Bajio",
    "del Pacifico", "Metropolitana", "Rural", "Nacional", "de los Altos", "de la Sierra"
]

# Usamos un conjunto para garantizar nombres únicos
nombres_generados = set()

while len(nombres_generados) < 300:
    nombre = f"{random.choice(nombres_base)} {random.choice(temas)} {random.choice(ubicaciones)}"
    nombres_generados.add(nombre)

for i in nombres_generados:
    print(i)