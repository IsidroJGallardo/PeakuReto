instituciones_educativas = {
    'universidad Nacional': 'UN',
    'Pontificia universidad javeriana': 'PUJ',
    'universidad de los andes': 'UA',
    'universidad del rosario': 'UR',
    'universidad Externado de Colombia': 'UEC'
}

def corregir_mayusculas(palabra):
    # Excepciones para artículos
    articulos = ['de', 'del', 'la', 'las', 'los']
    
    # Verificar si la palabra está en minúsculas y no es un artículo
    if palabra.islower() and palabra.lower() not in articulos:
        # Convertir la primera letra a mayúscula
        return palabra.capitalize()
    else:
        return palabra

# Función para agregar una nueva institución al diccionario
def agregar_institucion():
    nueva_institucion = input("Ingrese el nombre de la nueva institución: ")
    codigo = input("Ingrese el código de la nueva institución: ")
    instituciones_educativas[corregir_mayusculas(nueva_institucion)] = codigo
    print(f"Institución agregada: {nueva_institucion}: {codigo}")

# Preguntar al usuario si desea agregar una nueva institución
agregar_nueva = input("¿Desea agregar una nueva institución? (s/n): ").lower()
if agregar_nueva == 's':
    agregar_institucion()

# Aplicar corrección a cada clave del diccionario
instituciones_educativas_corregido = {corregir_mayusculas(k): v for k, v in instituciones_educativas.items()}

# Imprimir el diccionario corregido
print("Diccionario corregido:")
print(instituciones_educativas_corregido)
