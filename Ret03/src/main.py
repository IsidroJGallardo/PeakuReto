import json

def message_creator(personaje, personajes_dict):
    personaje_lower = personaje.lower()
    if personaje_lower in personajes_dict:
        return personajes_dict[personaje_lower]
    else:
        return 'Personaje no encontrado'

# Diccionario de personajes famosos y sus frases
personajes_disponibles = {
    'elon musk': 'Con mis ideas revolucionarias, estoy cambiando el mundo.',
    'albert einstein': 'La imaginación es más importante que el conocimiento.',
    'cleopatra': 'En el corazón de los hombres, la reina Cleopatra nunca muere.'
}

while True:
    # Mostrar los personajes disponibles al usuario
    print('Personajes disponibles:', ', '.join(personajes_disponibles.keys()))

    # Solicitar al usuario que ingrese el personaje por consola
    personaje_usuario = input('Ingresa el nombre de un personaje famoso (o "salir" para terminar): ')

    if personaje_usuario.lower() == 'salir':
        print('Saliendo del programa. ¡Hasta luego!')
        break

    # Verificar si el personaje ingresado está en el diccionario de personajes disponibles
    resultado = message_creator(personaje_usuario, personajes_disponibles)
    
    if resultado == 'Personaje no encontrado':
        print('Personaje no válido. Por favor, selecciona uno de los personajes disponibles.')
    else:
        print(resultado)

# Convertir el diccionario a formato JSON y guardarlo en un archivo
with open('personajes_disponibles.json', 'w') as json_file:
    json.dump(personajes_disponibles, json_file, indent=2)
