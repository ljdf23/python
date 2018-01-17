#Agenda telefónica

print("Bienvenido a la agenda telefónica de Luis")

agenda_telefonica = dict()

def imprimir_operacion(nombre_operacion):
    print()
    print("---Agenda---") 
    print(nombre_operacion)
    print("------------") 
    print()


def agregar_contacto():
    nombre = input("Escribe el nombre del contacto: ")
    numero = input("Escribe el número del contacto: ")
    agenda_telefonica[nombre] = numero;
    imprimir_operacion("Contacto agregado")


def remover_contacto():
    nombre = input("Escribe el nombre del contacto: ")
    nombre_operacion = None
    print()
    try:
        del agenda_telefonica[nombre]
    except KeyError:
       nombre_operacion = "Ese contacto no existe"
    else:           
       nombre_operacion = "Contacto borrado" 
    imprimir_operacion(nombre_operacion); 


def actualizar_contacto():
    nombre = input("Escribe el nombre del contacto a actualizar: ")
    numero = input("Nuevo número de contacto: ")
    agenda_telefonica[nombre] = numero      
    imprimir_operacion("Contacto actualizado") 

def ver_contacto():   
    nombre = input("Escribe el nombre del contacto: ")
    print()    
    try:
        nombre_operacion = "{} - {}".format(nombre , agenda_telefonica[nombre])
    except KeyError:
        nombre_operacion = "Ese contacto no existe"
    imprimir_operacion(nombre_operacion)

def ver_todo(): 
    nombre_operacion = "\n"  
    if len(agenda_telefonica) == 0:
        nombre_operacion="No tienes ningun contacto"
    else: 
        for contacto in agenda_telefonica:
           # if nombre_operacion == None:
            nombre_operacion += "{} - {}".format(contacto, agenda_telefonica[contacto]) + "\n"     
           # else:
           #     nombre_operacion = "\n{} - {}".format(contacto, agenda_telefonica[contacto])     
            
    imprimir_operacion(nombre_operacion)

def iniciar_agenda():
    print("**Bienvenido a la agenda telefónica**")
    while True:
        print()
        operacion = ""
        print("1 - Agregar contacto")
        print("2 - Remover contacto")
        print("3 - Actualizar contacto")
        print("4 - Ver un contacto")
        print("5 - Ver todos los contactos")
        print("6 - Salir")

        try:
            operacion = int(input(":"))
        except ValueError:
            print("Operación no válida, intente de nuevo.")
        else:
            if operacion == 1:
                agregar_contacto()
            elif operacion == 2:
                remover_contacto()
            elif operacion ==   3:
                actualizar_contacto()
            elif operacion == 4:
                ver_contacto()
            elif operacion == 5:
                ver_todo()
            elif operacion == 6:        
                break
            else:
                print("Operación desconocida.")


iniciar_agenda()
print("Hasta luego! :)")
