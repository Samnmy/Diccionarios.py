# 📚 Guía de Diccionarios en Python 🐍

En este proyecto, exploramos los diccionarios en Python, una de las estructuras de datos más poderosas y versátiles. ¡Vamos a aprender cómo usarlos de manera interactiva y divertida!

## 🚀 ¿Qué es un Diccionario?
Un diccionario es una estructura de datos que almacena pares **clave:valor**. Se define con llaves `{ }` y cada elemento tiene una **clave única**.

### 🧑‍💻 Ejemplo Básico:
```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}
```

## 📝 Funcionalidades

### 1️⃣ **Acceder a Elementos** 🔑
Puedes acceder a los valores de un diccionario usando la clave. Existen dos formas:
- Acceso directo: `persona["nombre"]`
- Usando `.get()`: `persona.get("edad")`

### 2️⃣ **Modificar y Agregar Elementos** ✏️
Puedes modificar los valores de un diccionario y agregar nuevas claves:

```python
persona["edad"] = 31  # Modificar
persona["profesion"] = "Ingeniera"  # Agregar
```

### 3️⃣ **Eliminar Elementos** 🗑️
Para eliminar un par clave-valor, puedes usar:
- `del persona["ciudad"]`
- `persona.pop("nombre")`

### 4️⃣ **Recorrer un Diccionario** 🔄
Puedes recorrer un diccionario usando un bucle `for`:

```python
for clave, valor in persona.items():
    print(clave, "=>", valor)
```

### 5️⃣ **Métodos Útiles de Diccionarios** 🔧
- `keys()`: Devuelve las claves del diccionario.
- `values()`: Devuelve los valores del diccionario.
- `items()`: Devuelve los pares clave-valor.

### 6️⃣ **Diccionarios con Listas Dentro** 📋
Los diccionarios pueden almacenar listas como valores. Ideal para representar datos más complejos:

```python
estudiante = {
    "nombre": "Luis",
    "cursos": ["Matemáticas", "Física", "Programación"],
    "notas": [9.0, 8.5, 10]
}
```

### 7️⃣ **Recorrer Listas dentro de Diccionarios** 🔍
Puedes recorrer las listas dentro de un diccionario:

```python
for i in range(len(estudiante["cursos"])):
    curso = estudiante["cursos"][i]
    nota = estudiante["notas"][i]
    print(f"{curso}: {nota}")
```

### 8️⃣ **Diccionario dentro de una Lista** 🗂️
Puedes tener diccionarios dentro de listas para representar estructuras más complejas, como una lista de estudiantes con sus notas:

```python
clase = [
    {"nombre": "Luis", "nota": 9.5},
    {"nombre": "Ana", "nota": 8.0},
    {"nombre": "Carlos", "nota": 7.2}
]
```

### 9️⃣ **Diccionario con Diccionarios** 📅
Los diccionarios pueden tener otros diccionarios como valores. Ideal para representar agendas o contactos:

```python
agenda = {
    "Pedro": {"tel": "123456", "email": "pedro@mail.com"},
    "Marta": {"tel": "789012", "email": "marta@mail.com"}
}
```

## 🎯 Métodos Útiles de Diccionarios

### 1️⃣ **Método `keys()`** 🔑
Devuelve todas las claves de un diccionario.

```python
for clave in auto.keys():
    print("Clave:", clave)
```

### 2️⃣ **Método `values()`** 🏷️
Devuelve todos los valores del diccionario.

```python
for valor in auto.values():
    print("Valor:", valor)
```

### 3️⃣ **Método `items()`** 📑
Devuelve los pares clave-valor.

```python
for clave, valor in auto.items():
    print(f"{clave}: {valor}")
```

### 4️⃣ **Método `get()`** 🔍
Permite acceder a un valor sin causar error si la clave no existe, y puedes definir un valor por defecto.

```python
print("Color:", auto.get("color", "No especificado"))
```

## ✨ Modificar y Eliminar Valores

### 1️⃣ **Acceder y Modificar** ✍️
Accede a los valores y modifícalos fácilmente:

```python
auto["año"] = 2022
```

### 2️⃣ **Agregar Nuevas Claves** ➕
Puedes agregar nuevas claves y valores:

```python
auto["color"] = "Rojo"
```

### 3️⃣ **Eliminar Elementos** ❌
Elimina un par clave-valor con `pop()` o `del`:

```python
auto.pop("modelo")
del auto["color"]
```

## 🛠️ Ejemplo Completo

```python
auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

# Modificación y eliminación
auto["año"] = 2022
auto["color"] = "Rojo"
auto.pop("modelo")
del auto["color"]

print(auto)
```

### 🔚 **Resultado Final:**
```
{'marca': 'Toyota', 'año': 2022}
```

## 🎉 ¡Felicitaciones! 🎉

¡Ahora eres un experto en el manejo de diccionarios en Python! 🐍
Puedes usarlos para almacenar, manipular y organizar datos de manera eficiente en cualquier proyecto.

¡Sigue explorando más funciones y métodos de Python! 🚀
