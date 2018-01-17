
lista_articulos = list()

def agregar_articulo():
    print()
    articulo = input("Nombre del artículo a agregar: ")    
    art = ""; 
    lista_articulos.append(articulo.capitalize())
    print("Artículo agregado.")
    print()

def remover_articulo():
    print()   
    articulo = input("Nombre del artículo a remover: ")
    
    try:
        lista_articulos.remove(articulo.capitalize())
    except ValueError as ex:
        print("No se encuentra el artículo definido.")
    else: 
        print("El artículo ha sido removido")
    
    print()  

def ver_articulos():
    print()
    print("-----------Lista de compras-----------")
    for articulo in lista_articulos:
        print(articulo)
    print("--------------------------------------")
    print()

print("Bienvenido a nuestra lista de compras.")
print()
while True:
    print("Estas son las operaciones que puedes realizar:")
    print("1 - Agregar artículo")
    print("2 - Remover artículo")
    print("3 - Ver los artículos")
    print("4 - Salir")
    operacion = int(input(": "))
    
    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    else:
        break;

print("Gracias por usar nuestra lista de compras.")
print("Come back soon!")
 
        