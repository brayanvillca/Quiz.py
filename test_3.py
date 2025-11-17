
def evaluar_pregunta(pregunta_completa):
    
    lineas = pregunta_completa.strip().split('\n')
    
    # Encontrar el marcador de respuesta correcta (#N)
    respuesta_correcta = None
    pregunta_limpia = []
    
    for linea in lineas:
        if linea.startswith('#'):
            try:
                respuesta_correcta = int(linea[1:])  # Extrae el número
            except ValueError:
                print("Error: Marcador de respuesta incorrecto.")
                return 0
        else:
            pregunta_limpia.append(linea)
    
    if respuesta_correcta is None:
        print("Error: No se encontró la respuesta correcta.")
        return 0
    
    # Mostrar pregunta sin el marcador
    print("\n" + "="*50)
    for linea in pregunta_limpia:
        print(linea)
    print("="*50)
    
    # Pedir respuesta al usuario
    while True:
        try:
            respuesta_usuario = int(input("Tu respuesta (1-4): "))
            if 1 <= respuesta_usuario <= 4:
                break
            else:
                print("Por favor, ingresa un número entre 1 y 4.")
        except ValueError:
            print("Entrada inválida. Ingresa un número del 1 al 4.")
    
    # Comparar y devolver resultado
    return 1 if respuesta_usuario == respuesta_correcta else 0


def mostrar_resultado(correctas):
    """
    Recibe el número de respuestas correctas (0 a 5)
    y devuelve un mensaje según la puntuación.
    """
    if correctas >= 4:
        return "¡Has pasado la prueba! ¡Te estaremos esperando en la próxima etapa de la entrevista!"
    elif correctas == 3:
        return "¡Practica un poco más y vuelve a intentarlo!"
    else:  # 0, 1 o 2
        return "En este momento, no estamos listos para considerarlo como un candidato potencial para el puesto."


# correctas = 0
# correctas += evaluar_pregunta(q.pregunta_1)
# correctas += evaluar_pregunta(q.pregunta_2)
# correctas += evaluar_pregunta(q.pregunta_3)
# correctas += evaluar_pregunta(q.pregunta_4)
# correctas += evaluar_pregunta(q.pregunta_5)
    
# print("\n" + "-"*50)
# print("RESULTADO FINAL:")
# print(mostrar_resultado(correctas))
# print("-"*50)

# importar question_3 as q para prueba