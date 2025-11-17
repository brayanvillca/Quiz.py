# Módulo de preguntas técnicas (hard skills) – Equipo 3
# Cada variable contiene: pregunta + opciones + marcador de respuesta correcta
# Marcador: # seguido del número de opción correcta (ej. #3)

pregunta_1 = (
    "¿Cuál es la salida del siguiente código Python?\n"
    "x = [1, 2, 3]\n"
    "y = x\n"
    "y.append(4)\n"
    "print(x)\n"
    "1) [1, 2, 3]\n"
    "2) [1, 2, 3, 4]\n"
    "3) [4]\n"
    "4) Error\n"
    "#2"
)

pregunta_2 = (
    "¿Qué método se usa para eliminar un elemento específico de una lista por su valor?\n"
    "1) list.delete(value)\n"
    "2) list.remove(value)\n"
    "3) list.pop(value)\n"
    "4) list.clear(value)\n"
    "#2"
)

pregunta_3 = (
    "¿Cuál es el resultado de: 3 * 'abc' + 'def'?\n"
    "1) 'abcabcabc'\n"
    "2) 'abcabcdef'\n"
    "3) 'abcabcabcdef'\n"
    "4) 'abcabcabc def'\n"
    "#3"
)

pregunta_4 = (
    "¿Qué estructura de control se utiliza para iterar directamente sobre los elementos de una lista?\n"
    "1) while\n"
    "2) for ... in range()\n"
    "3) for ... in lista\n"
    "4) if-elif-else\n"
    "#3"
)

pregunta_5 = (
    "¿Cuál es la forma correcta de abrir un archivo en modo lectura y escritura en Python?\n"
    "1) open('file.txt', 'r')\n"
    "2) open('file.txt', 'w+')\n"
    "3) open('file.txt', 'a')\n"
    "4) open('file.txt', 'rw')\n"
    "#2"
)

# -------------------------------------------------
# PRUEBA RÁPIDA (eliminar antes de entregar)
# -------------------------------------------------
if __name__ == "__main__":
    print(pregunta_1, end="\n\n")
    print(pregunta_2, end="\n\n")
    print(pregunta_3, end="\n\n")
    print(pregunta_4, end="\n\n")
    print(pregunta_5, end="\n\n")