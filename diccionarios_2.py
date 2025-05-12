# Creamos un diccionario de ejemplo
auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

print("Diccionario original:", auto)

# ------------------------------------------
# 1. MÉTODOS ÚTILES
# ------------------------------------------

# keys(): devuelve todas las claves del diccionario
print("\nMétodo keys():")
for clave in auto.keys():
    print("Clave:", clave)

# values(): devuelve todos los valores del diccionario
print("\nMétodo values():")
for valor in auto.values():
    print("Valor:", valor)

# items(): devuelve pares (clave, valor)
print("\nMétodo items():")
for clave, valor in auto.items():
    print(f"{clave}: {valor}")

# get(clave, valor_por_defecto): busca una clave y evita errores si no existe
print("\nMétodo get():")
print("Color:", auto.get("color", "No especificado"))
print("Año:", auto.get("año", "Desconocido"))

# ------------------------------------------
# 2. MODIFICAR VALORES EN UN DICCIONARIO
# ------------------------------------------

# Acceder y mostrar un valor
print("\nAcceso directo a 'marca':", auto["marca"])

# Modificar un valor existente
auto["año"] = 2022
print("Año actualizado:", auto["año"])

# Agregar una nueva clave-valor
auto["color"] = "Rojo"
print("Diccionario con nueva clave 'color':", auto)

# Sobrescribir valor si la clave ya existe
auto["color"] = "Azul"
print("Color actualizado:", auto)

# Eliminar un par clave-valor con pop()
auto.pop("modelo")
print("Diccionario después de eliminar 'modelo':", auto)

# También puedes usar del para eliminar
del auto["color"]
print("Después de usar 'del' en 'color':", auto)
