from model.conexion import conexion

def mostrar_todo():
    db = conexion()
    collection = db["Words"]
    documentos = collection.find()
    for documento in documentos:
        print(documento)

def comparacion_id(palabra1, palabra2):
    db = conexion()
    collection = db["Words"]

    # Buscar el documento con la palabra en inglés
    documento1 = collection.find_one({"ingles": palabra1})
    if documento1:
        id1 = documento1["_id"]
    else:
        print(f"No se encontró el documento con la palabra en inglés: {palabra1}")
        return

    # Buscar el documento con la palabra en español
    documento2 = collection.find_one({"espanol": palabra2})
    if documento2:
        id2 = documento2["_id"]
    else:
        print(f"No se encontró el documento con la palabra en español: {palabra2}")
        return

    # Comparar los IDs
    if id1 == id2:
        print("Tienen el mismo ID.")
    else:
        print("Tienen IDs distintos.")


def agregar_documento(ingles,espanol):
    db = conexion()
    collection = db["Words"]
    # Crear un diccionario con los datos del nuevo documento
    nuevo_documento = {
        "ingles": ingles,
        "espanol": espanol
    }
    resultado = collection.insert_one(nuevo_documento)
    # Retornar el _id del nuevo documento insertado
    print(f"Nuevo documento agregado con el _id: {resultado.inserted_id}")


def eliminar_documento(palabra):
    # Obtener la conexión a la base de datos
    db = conexion()
    collection = db["Words"]

    # Buscar el documento que contiene la palabra en el campo "ingles" o "espanol"
    documento = collection.find_one({"ingles": palabra}) or collection.find_one({"espanol": palabra})

    if documento:
        # Eliminar el documento
        collection.delete_one({"_id": documento["_id"]})
        print(f"Documento con _id {documento['_id']} eliminado.")
    else:
        print(f"No se encontró ningún documento que contenga la palabra: {palabra}")


def editar_documento(palabra_original, nueva_palabra):
    db = conexion()
    collection = db["Words"]

    # Buscar el documento que contiene la palabra en el campo "ingles" o "espanol"
    documento = collection.find_one({"ingles": palabra_original}) or collection.find_one({"espanol": palabra_original})

    if documento:
        # Determinar el campo que contiene la palabra original
        campo_a_actualizar = "ingles" if documento["ingles"] == palabra_original else "espanol"

        # Actualizar el documento
        collection.update_one({"_id": documento["_id"]}, {"$set": {campo_a_actualizar: nueva_palabra}})
        print(f"Documento con _id {documento['_id']} actualizado. La palabra '{palabra_original}' fue reemplazada por '{nueva_palabra}'.")
    else:
        print(f"No se encontró ningún documento que contenga la palabra: {palabra_original}")



#comparacion_id("hello", "hola")
#agregar_documento("hi","hola")
#eliminar_documento("tank")
#editar_documento("saludo", "hola")
mostrar_todo()