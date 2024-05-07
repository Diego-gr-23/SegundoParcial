class NodoAdivinanza:
    def __init__(self, pregunta=None, objeto=None):
        self.pregunta = pregunta
        self.objeto = objeto
        self.izquierda = None
        self.derecha = None

def importar_arbol(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
        preorder = lineas[0][len("Preorder: "):].split()
        inorder = lineas[1][len("Inorder: "):].split()
        postorder = lineas[2][len("Postorder: "):].split()
    return construir_arbol_desde_traversals(preorder, inorder, postorder)

def construir_arbol_desde_traversals(preorder, inorder, postorder):
    if not preorder:
        return None
    raiz = NodoAdivinanza(preorder[0])
    indice_raiz_inorder = inorder.index(preorder[0])
    raiz.izquierda = construir_arbol_desde_traversals(preorder[1:indice_raiz_inorder + 1], inorder[:indice_raiz_inorder], postorder[:indice_raiz_inorder])
    raiz.derecha = construir_arbol_desde_traversals(preorder[indice_raiz_inorder + 1:], inorder[indice_raiz_inorder + 1:], postorder[indice_raiz_inorder:-1])
    return raiz

def construir_arbol_adivinanza():
    # Acá se construye el árbol de adivinanzas inicial
    raiz = NodoAdivinanza("¿Es un animal?", None)
    raiz.izquierda = NodoAdivinanza("¿Vuela?", None)
    raiz.derecha = NodoAdivinanza("¿Tiene cuatro patas?", None)
    raiz.izquierda.izquierda = NodoAdivinanza(None, "pájaro")
    raiz.izquierda.derecha = NodoAdivinanza(None, "avión")
    raiz.derecha.izquierda = NodoAdivinanza(None, "gato")
    raiz.derecha.derecha = NodoAdivinanza(None, "perro")
    return raiz

def jugar_adivinanza(raiz):
    nodo_actual = raiz
    while nodo_actual.objeto is None:
        respuesta = input(nodo_actual.pregunta + " (si/no): ").lower()
        if respuesta == "si":
            nodo_actual = nodo_actual.izquierda
        elif respuesta == "no":
            nodo_actual = nodo_actual.derecha
        else:
            print("Por favor, responde si o no.")
    adivinanza = nodo_actual.objeto
    respuesta_usuario = input("¿Es un/a " + adivinanza + "? (si/no): ").lower()
    if respuesta_usuario == "si":
        print("Felicidades, Ganaste!!!!! UwU")
    else:
        nuevo_objeto = input("¡Oh no! ¿Qué era entonces? ")
        nueva_pregunta = input("Por favor, ingresa una pregunta que distinga un/a " + adivinanza + " de un/a " + nuevo_objeto + ": ")
        respuesta_nueva_pregunta = input("Y la respuesta para un/a " + nuevo_objeto + " sería (si/no): ")

        # En esta parte se actializa el árbol con la nueva pregunta y respuesta
        nodo_actual.pregunta = nueva_pregunta
        nodo_actual.objeto = None
        if respuesta_nueva_pregunta == "si":
            nodo_actual.izquierda = NodoAdivinanza(None, nuevo_objeto)
            nodo_actual.derecha = NodoAdivinanza(None, adivinanza)
        else:
            nodo_actual.izquierda = NodoAdivinanza(None, adivinanza)
            nodo_actual.derecha = NodoAdivinanza(None, nuevo_objeto)

def exportar_arbol(raiz, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Preorder: ")
        _exportar_preorder(raiz, archivo)
        archivo.write("\nInorder: ")
        _exportar_inorder(raiz, archivo)
        archivo.write("\nPostorder: ")
        _exportar_postorder(raiz, archivo)

def _exportar_preorder(nodo, archivo):
    if nodo:
        archivo.write(str(nodo.pregunta) + ",")
        _exportar_preorder(nodo.izquierda, archivo)
        _exportar_preorder(nodo.derecha, archivo)

def _exportar_inorder(nodo, archivo):
    if nodo:
        _exportar_inorder(nodo.izquierda, archivo)
        archivo.write(str(nodo.pregunta) + ",")
        _exportar_inorder(nodo.derecha, archivo)

def _exportar_postorder(nodo, archivo):
    if nodo:
        _exportar_postorder(nodo.izquierda, archivo)
        _exportar_postorder(nodo.derecha, archivo)
        archivo.write(str(nodo.pregunta) + ",")

def main():
    print("¡Bienvenido al Juego de Adivinanzas!")
    opcion = input("¿Desea cargar un árbol existente desde un archivo? (si/no): ").lower()
    if opcion == "si":
        archivo = input("Ingrese el nombre del archivo: ")
        raiz = importar_arbol(archivo)
    else:
        raiz = construir_arbol_adivinanza()
    jugar_adivinanza(raiz)
    opcion_exportar = input("¿Desea exportar el árbol actual a un archivo? (si/no): ").lower()
    if opcion_exportar == "si":
        archivo_exportar = input("Ingrese el nombre del archivo para exportar: ")
        exportar_arbol(raiz, archivo_exportar)
    opcion = input("¿Desea jugar otra vez? (si/no): ").lower()
    while opcion == "si":
        jugar_adivinanza(raiz)
        opcion_exportar = input("¿Desea exportar el árbol actual a un archivo? (si/no): ").lower()
        if opcion_exportar == "si":
            archivo_exportar = input("Ingrese el nombre del archivo para exportar: ")
            exportar_arbol(raiz, archivo_exportar)
        opcion = input("¿Desea jugar otra vez? (si/no): ").lower()

main()
