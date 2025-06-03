import random

def generar_url_fakeimg(texto="Organizacion"):
    ancho = random.choice([200, 300, 400])
    alto = random.choice([150, 200, 250])
    texto = texto.replace(" ", "+")
    return f"https://fakeimg.pl/{ancho}x{alto}/?text={texto}"


urls = []
for i in range(1000):
    texto = f"Logo_{i}"
    url = generar_url_fakeimg(texto)
    urls.append(url)

for i in urls:
    print()