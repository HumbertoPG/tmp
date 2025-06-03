import random

# Listas base para crear nombres variados
nombres_base = [
    "Fundacion", "Asociacion", "Colectivo", "Centro", "Movimiento", "Red",
    "Alianza", "Consejo", "Comunidad", "Frente", "Instituto", "Coalicion"
]

temas = [
    "Esperanza", "Justicia", "Tecnologia", "Medio Ambiente", "Educacion",
    "Salud", "Diversidad", "Juventud", "Mujeres", "Cultura", "Derechos",
    "Innovacion", "Desarrollo", "Cambio Social", "Paz", "Sostenibilidad"
]

ubicaciones = [
    "de Mexico", "Latinoamericana", "del Norte", "de Occidente", "del Sur",
    "del Bajio", "del Pacifico", "Metropolitana", "Rural", "Nacional",
    "de la Sierra", "Ciudadana", "del Sureste", "Autonoma"
]

# Generar 1,000 nombres únicos
nombres = set()
while len(nombres) < 1000:
    nombre = f"{random.choice(nombres_base)} {random.choice(temas)} {random.choice(ubicaciones)}"
    nombres.add(nombre)

# Guardar en un archivo .txt o imprimirlos
with open("nombres_organizaciones.txt", "w", encoding="utf-8") as f:
    for n in sorted(nombres):
        f.write(n + "\n")

print("Listo: 1,000 nombres generados y guardados en 'nombres_organizaciones.txt'")
