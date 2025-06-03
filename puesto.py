import random

# Lista de posibles puestos
puestos_responsables = [
    "Director General", "Presidenta", "Coordinador de Proyectos",
    "Responsable de Vinculacion", "Gerente de Operaciones",
    "Coordinador de Programas Sociales", "Subdirectora Ejecutiva",
    "Jefe de Area Social", "Enlace Institucional", "Encargada de Comunidad",
    "Representante Legal", "Administradora", "Coordinador General",
    "Lider de Impacto Social", "Responsable de Educacion",
    "Directora de Desarrollo", "Promotor Comunitario",
    "Responsable de Alianzas", "Gestora de Proyectos", "Titular de Organizacion",
    "Oficial de Programas", "Gerente de Responsabilidad Social",
    "Supervisor Operativo", "Asesora de Direccion", "Enlace con Gobierno",
    "Director Ejecutivo", "Coordinador de Voluntariado",
    "Encargado de Capacitacion", "Lider de Comunidad", "Jefa de Planeacion"
]

# Generar 1,000 aleatorios
puestos = [random.choice(puestos_responsables) for _ in range(1000)]

for i in puestos:
    print(i)