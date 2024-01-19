def sumar_n_elementos_segunda_columna(datos, n):
    suma = 0
    contador = 0

    # Iterar sobre los datos del diccionario
    for departamento, valor in datos.items():
        suma += valor
        contador += 1

        if contador == n:
            break  # Detener después de n elementos

    return suma

# Datos en forma de diccionario
datos_departamentos = {
    'Administration': 200,
    'Marketing': 201,
    'Purchasing': 114,
    'Human Resources': 203,
    'Shipping': 121,
    'IT': 103,
    'Public Relations': 204,
    'Sales': 145,
    'Executive': 100
}

# Solicitar al usuario la cantidad de elementos a sumar
cantidad_elementos_str = input("Ingrese la cantidad de elementos a sumar: ")

try:
    cantidad_elementos = int(cantidad_elementos_str)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
    cantidad_elementos = 0

if cantidad_elementos > 0:
    # Ejemplo de uso
    resultado = sumar_n_elementos_segunda_columna(datos_departamentos, cantidad_elementos)
    print(f"La suma de los {cantidad_elementos} primeros elementos es: {resultado}")