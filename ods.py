import random

ods = [
    "1. Fin de la pobreza",
    "2. Hambre cero",
    "3. Salud y bienestar",
    "4. Educacion de calidad",
    "5. Igualdad de genero",
    "6. Agua limpia y saneamiento",
    "7. Energia asequible y no contaminante",
    "8. Trabajo decente y crecimiento economico",
    "9. Industria, innovacion e infraestructura",
    "10. Reduccion de las desigualdades",
    "11. Ciudades y comunidades sostenibles",
    "12. Produccion y consumo responsable",
    "13. Accion por el clima",
    "14. Vida submarina",
    "15. Vida de ecosistemas terrestres",
    "16. Paz, justicia e instituciones solidas",
    "17. Alianzas para lograr los objetivos"
]

# Generar 1,000 respuestas aleatorias
ods_seleccionados = [random.choice(ods) for _ in range(1000)]

for i in ods_seleccionados:
    print(i)
