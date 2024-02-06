import json

def combinar_json(json1=None, json2=None):
    # Definir JSONs por defecto
    json1_default = {"name": "Mr. Michi", "food": "Pescado"}
    json2_default = {"age": 12, "color": "Blanco"}

    # Combinar JSONs
    json_combinado = json1_default.copy()
    json_combinado.update(json1 or {})
    json_combinado.update(json2 or {})

    return json_combinado

# Input: Puedes modificar estos valores según sea necesario
json1_input = input("Ingresa el primer JSON (o deja en blanco para usar el valor por defecto): ")
json2_input = input("Ingresa el segundo JSON (o deja en blanco para usar el valor por defecto): ")

# Convertir los strings de input a diccionarios JSON
try:
    json1 = json.loads(json1_input) if json1_input else None
except json.JSONDecodeError:
    print("Error en el formato del primer JSON.")
    json1 = None

try:
    json2 = json.loads(json2_input) if json2_input else None
except json.JSONDecodeError:
    print("Error en el formato del segundo JSON.")
    json2 = None

# Llamar a la función
resultado = combinar_json(json1, json2)

# Mostrar el resultado
print("Resultado combinado:")
print(json.dumps(resultado, indent=2))
