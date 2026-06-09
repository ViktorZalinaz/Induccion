# =========================================================
# [1] IMPORTACIONES
# =========================================================
import os
import re

# =========================================================
# [2] CONFIGURACIÓN GENERAL
# =========================================================

# Carpeta donde está el script (mismo lugar de imágenes)
carpeta = os.path.dirname(os.path.abspath(__file__))

# Expresión regular para extraer número
patron = re.compile(r'(\d+)')


# =========================================================
# [3] FUNCIÓN: EXTRAER NÚMERO DE ARCHIVO
# =========================================================
def obtener_numero(nombre):
    match = patron.search(nombre)
    if match:
        return int(match.group(1))
    return None


# =========================================================
# [4] FUNCIÓN: RENOMBRADO AUTOMÁTICO
# =========================================================
def renombrar_todo():

    print("\n[MODO AUTOMÁTICO ACTIVADO]\n")

    for archivo in os.listdir(carpeta):
        
        if archivo.endswith(".png"):

            numero = obtener_numero(archivo)

            if numero is None:
                continue

            # ✅ quitar ceros a la izquierda
            nuevo_nombre = f"{numero}.png"

            ruta_vieja = os.path.join(carpeta, archivo)
            ruta_nueva = os.path.join(carpeta, nuevo_nombre)

            os.rename(ruta_vieja, ruta_nueva)

            print(f"{archivo} → {nuevo_nombre}")


# =========================================================
# [5] FUNCIÓN: RENOMBRADO POR RANGO
# =========================================================
def renombrar_rango(inicio_real, fin_real):

    print("\n[MODO RANGO ACTIVADO]\n")

    archivos = sorted([f for f in os.listdir(carpeta) if f.endswith(".png")])

    contador = 0

    for archivo in archivos:

        numero = obtener_numero(archivo)

        if numero is None:
            continue

        # ===============================
        # CASO 1: YA TIENE NUMERO REAL
        # ===============================
        if inicio_real <= numero <= fin_real:

            nuevo_nombre = f"{numero}.png"

        # ===============================
        # CASO 2: VIENE COMO 001, 002...
        # ===============================
        else:
            nuevo_numero = inicio_real + contador

            if nuevo_numero > fin_real:
                break

            nuevo_nombre = f"{nuevo_numero}.png"
            contador += 1

        ruta_vieja = os.path.join(carpeta, archivo)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)

        os.rename(ruta_vieja, ruta_nueva)

        print(f"{archivo} → {nuevo_nombre}")


# =========================================================
# [6] MENÚ PRINCIPAL
# =========================================================
def main():

    print("=================================")
    print("   RENOMBRADOR DE IMÁGENES")
    print("=================================")
    print("1. Renombrar TODO automáticamente")
    print("2. Renombrar por RANGO")
    print("=================================")

    opcion = input("Selecciona una opción (1 o 2): ")

    # ===============================
    # OPCIÓN 1
    # ===============================
    if opcion == "1":
        renombrar_todo()

    # ===============================
    # OPCIÓN 2
    # ===============================
    elif opcion == "2":

        inicio = int(input("Página inicial real (ej: 50): "))
        fin = int(input("Página final real (ej: 60): "))

        renombrar_rango(inicio, fin)

    else:
        print("Opción inválida")


# =========================================================
# [7] EJECUCIÓN
# =========================================================
if __name__ == "__main__":
    main()