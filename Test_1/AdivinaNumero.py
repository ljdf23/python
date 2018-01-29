import random


#Darle 5 vidas al usuario
#Dar pistas, si el número es mayor o menor 
#Queremos poner la opción de volver a jugar generando numero diferente
def seleccion_de_dificultad():
    rango_maximo = 0;
    intentos = 0;
    while True:
        print("Ingresa el nivel de dificultad")
        print("1 . Facil")
        print("2 . Medio")
        print("3 . Dificil")
        try:
            dificultad = int(input("Opción: "))
        except ValueError as identifier:
            print("Opción no válida, intente de nuevo.")
        else:        
            if dificultad == 1:            
                rango_maximo = 10
                intentos = 5
            elif dificultad == 2:
                rango_maximo = 15
                intentos = 3
            elif dificultad == 3:
                rango_maximo = 20
                intentos = 1
            else:
                print("Opción inválida, intente de nuevo.")
                continue
            return (intentos, rango_maximo)

def jugar():
    tupla = (); 
    intentos = 0;

    print("Bienvenido a Adivina el número")
    tupla = seleccion_de_dificultad(); 

    print("Número de intentos posibles: {}".format(tupla[0]))
    print("Estoy pensando en un número del 1 al {}".format(tupla[1]))
    numero_aleatorio = random.randint(1, tupla[1]) 
    print("Adivina cual es, tienes 5 intentos.")

    while intentos < tupla[0]:
        try:
            adivinanza = int(input("El número es:"))
        except ValueError as error:
            print("Número inválido!")
        else:  
            if adivinanza == numero_aleatorio:
                print("Adivinaste!!")
                jugar_nuevamente = input("jugar de nuevo? si/no: ")
                if jugar_nuevamente.lower() == "si":
                    jugar();
                else:
                    break;
            elif (adivinanza > numero_aleatorio):
                print("El número aleatorio es menor al que elegiste")
            else:
                print("El número aleatorio es mayor al que elegiste")
                
            intentos += 1;
            print("Intento {}/5".format(intentos))
    else:
        print("Se te acabaron los intentos.")
        print("Gracias por jugar")
        jugar_nuevamente = input("jugar de nuevo? si/no: ")

        if jugar_nuevamente.lower() == "si":
            jugar();

jugar();