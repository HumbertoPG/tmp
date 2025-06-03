#!/usr/bin/env python3
"""
Descarga 300 nombres de empresas distintas de Wikipedia (Fortune Global 500)
y los guarda en 'empresas.txt'.

Autor: Tú 💡
Fecha: 2025-06-03
"""

import pandas as pd
import requests

URL = "https://en.wikipedia.org/wiki/Fortune_Global_500"
NUM_EMPRESAS = 300            # cámbialo si necesitas más o menos

def obtener_empresas(url: str, n: int) -> list[str]:
    """
    Devuelve una lista con los primeros `n` nombres de empresa encontrados
    en la tabla principal de Fortune Global 500 de Wikipedia.
    """
    # 1. Descargar la página (más rápido y con headers amistosos)
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()

    # 2. Extraer todas las tablas que contengan la palabra "Rank" (clave de la tabla)
    tablas = pd.read_html(resp.text, match="Rank")

    if not tablas:
        raise ValueError("No se encontró la tabla esperada 🤔")

    df = tablas[0]            # la primera tabla es la de posiciones 1-500

    # Normalizar nombre de columna (varía a veces)
    col_empresa = next(
        (c for c in df.columns if c.lower() in {"company", "empresa", "name"}),
        None
    )
    if col_empresa is None:
        raise ValueError("No se encontró la columna de nombres de empresa")

    # 3. Limitar a los primeros n registros y quitar duplicados/NaN
    empresas = (
        df[col_empresa]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()[:n]
    )

    if len(empresas) < n:
        raise ValueError(
            f"Solo se encontraron {len(empresas)} nombres; se pidieron {n}"
        )
    return empresas

def guardar_en_archivo(lineas: list[str], ruta: str) -> None:
    with open(ruta, "w", encoding="utf-8") as f:
        for linea in lineas:
            f.write(linea + "\n")

def main() -> None:
    empresas = obtener_empresas(URL, NUM_EMPRESAS)
    guardar_en_archivo(empresas, "empresas.txt")
    print(f"✅ Se guardaron {len(empresas)} nombres en 'empresas.txt'.")

if __name__ == "__main__":
    main()
