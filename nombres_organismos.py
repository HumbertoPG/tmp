import random

# Prefijos típicos de organismos
niveles = [
    "Secretaría de", "Dirección General de", "Coordinación de",
    "Instituto Nacional de", "Agencia Estatal de", "Comisión de",
    "Unidad de", "Delegación de", "Oficina de", "Subsecretaría de"
]

# Temas comunes de políticas públicas
temas = [
    "Salud Pública", "Educación Básica", "Movilidad y Transporte",
    "Seguridad Ciudadana", "Desarrollo Social", "Cultura y Artes",
    "Protección Civil", "Gestión Ambiental", "Tecnología e Innovación",
    "Derechos Humanos", "Juventud", "Deporte", "Planeación Urbana",
    "Finanzas Públicas", "Turismo", "Vivienda", "Atención a Víctimas",
    "Inclusión Social", "Asuntos Indígenas", "Trabajo y Previsión Social"
]

# Generar nombres combinados
def crear_nombre_gob():
    return f"{random.choice(niveles)} {random.choice(temas)}"

nombres_gob = {crear_nombre_gob() for _ in range(1000)}
nombres_gob = list(nombres_gob)[:300]

# Guardar en archivo .txt
with open("organismos_gubernamentales.txt", "w", encoding="utf-8") as f:
    for nombre in nombres_gob:
        f.write(nombre + "\n")

print("Listo: 300 nombres guardados en 'organismos_gubernamentales.txt'")
