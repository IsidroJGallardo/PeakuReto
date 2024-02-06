def message_creator(articulo):
    if articulo.lower() == 'computadora':
        return 'Con mi computadora puedo programar usando Python'
    elif articulo.lower() == 'celular':
        return 'En mi celular puedo aprender usando la app de Platzi'
    elif articulo.lower() == 'cable':
        return '¡Hay un cable en mi bota!'
    else:
        return 'Artículo no encontrado'

# Ejemplos de uso:
print(message_creator('computadora'))  # Output: Con mi computadora puedo programar usando Python
print(message_creator('celular'))      # Output: En mi celular puedo aprender usando la app de Platzi
print(message_creator('cable'))        # Output: ¡Hay un cable en mi bota!
print(message_creator('auriculares'))  # Output: Artículo no encontrado
