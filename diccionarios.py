# ------------------------------------------
# 1. ¿Qué es un diccionario?
# ------------------------------------------
# Es una estructura que almacena pares clave:valor
# Se define con llaves { } y cada elemento tiene una clave única

persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

print("Diccionario persona:", persona)

# ------------------------------------------
# 2. Acceder a elementos
print("Nombre:", persona["nombre"])         # Acceso directo
print("Edad:", persona.get("edad"))         # Acceso con .get()

# ------------------------------------------
# 3. Modificar y agregar elementos
persona["edad"] = 31                        # Modificar valor
persona["profesion"] = "Ingeniera"         # Agregar nuevo par
print("Diccionario modificado:", persona)

# ------------------------------------------
# 4. Eliminar elementos
del persona["ciudad"]                      # Usando del
persona.pop("nombre")                      # Usando pop()
print("Después de eliminar:", persona)

# ------------------------------------------
# 5. Recorrer un diccionario
print("Recorriendo claves y valores:")
for clave, valor in persona.items():
    print(clave, "=>", valor)

# ------------------------------------------
# 6. Métodos útiles de diccionarios
print("Claves:", list(persona.keys()))
print("Valores:", list(persona.values()))
print("Items:", list(persona.items()))

# ------------------------------------------
# 7. Diccionarios con listas dentro
# Ideal para representar datos más complejos
estudiante = {
    "nombre": "Luis",
    "cursos": ["Matemáticas", "Física", "Programación"],
    "notas": [9.0, 8.5, 10]
}

print("Estudiante:", estudiante)
print("Cursos del estudiante:", estudiante["cursos"])
print("Primera nota:", estudiante["notas"][0])

# Agregar otro curso y nota
estudiante["cursos"].append("Química")
estudiante["notas"].append(8.0)

print("Estudiante actualizado:", estudiante)

# ------------------------------------------
# 8. Recorrer lista dentro de diccionario
print("Notas del estudiante:")
for i in range(len(estudiante["cursos"])):
    curso = estudiante["cursos"][i]
    nota = estudiante["notas"][i]
    print(f"{curso}: {nota}")

# ------------------------------------------
# 9. Diccionario dentro de una lista (estructura aún más compleja)
# Lista de varios estudiantes
clase = [
    {"nombre": "Luis", "nota": 9.5},
    {"nombre": "Ana", "nota": 8.0},
    {"nombre": "Carlos", "nota": 7.2}
]

print("Notas de la clase:")
for alumno in clase:
    print(f"{alumno['nombre']} tiene una nota de {alumno['nota']}")

# ------------------------------------------
# 10. Bonus: Diccionario con valores que son otros diccionarios
agenda = {
    "Pedro": {"tel": "123456", "email": "pedro@mail.com"},
    "Marta": {"tel": "789012", "email": "marta@mail.com"}
}

print("Agenda:")
for nombre, datos in agenda.items():
    print(f"{nombre} -> Tel: {datos['tel']}, Email: {datos['email']}")
