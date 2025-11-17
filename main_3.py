# main_3.py – Módulo principal del quiz (Equipo 3)
# Importa los módulos del equipo y ejecuta la prueba completa

import time
import questions_3 as q
from test_3 import evaluar_pregunta, mostrar_resultado


def ejecutar_prueba():
    """
    Ejecuta el quiz completo:
    - Pide nombre
    - Mide tiempo
    - Pregunta una por una
    - Muestra resultado final
    """
    # 1. Introducir el nombre del usuario
    nombre = input("Por favor, ingresa tu nombre completo: ").strip()
    if not nombre:
        nombre = "Candidato"

    print(f"\n¡Hola, {nombre}! Comenzando la prueba técnica...\n")
    time.sleep(1)

    # 2. Iniciar medición de tiempo
    inicio = time.time()

    # 3. Evaluar todas las preguntas
    correctas = 0
    preguntas = [
        q.pregunta_1,
        q.pregunta_2,
        q.pregunta_3,
        q.pregunta_4,
        q.pregunta_5
    ]

    for i, pregunta in enumerate(preguntas, 1):
        print(f"Pregunta {i} de {len(preguntas)}")
        correctas += evaluar_pregunta(pregunta)
        print()  # Línea en blanco entre preguntas

    # 4. Finalizar tiempo
    fin = time.time()
    tiempo_total = int(fin - inicio)

    # 5. Mostrar resultado final
    mensaje = mostrar_resultado(correctas)

    print("=" * 60)
    print(f"{nombre}")
    print(f"Tiempo de finalización de la prueba: {tiempo_total} segundos")
    print(f"Puntos obtenidos: {correctas}")
    print(mensaje)
    print("=" * 60)


# Ejecutar solo si este archivo es el principal
if __name__ == "__main__":
    ejecutar_prueba()