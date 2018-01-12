 def realizar_operacion (operacion, primer_numero, segundo_numero):
    if operacion == '1':
        resultado = primer_numero + segundo_numero
    elif operacion == '2':
        resultado = primer_numero - segundo_numero
    elif operacion == '3':
        resultado = primer_numero * segundo_numero
    elif operacion == '4':
        resultado = primer_numero / segundo_numero
        
    return resultado
 
while True:
    print("Estas son las operaciones que puedes realizar")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")
    print("5 - Salir del programa")
    opcion = input("Introduce el numero de operación que quieres realizar: ")
    resultado = 0
    lista_de_opciones = ['1','2','3','4'];

    if opcion in lista_de_opciones:
        try:
            primer_numero = int(input("Introduce el primer número "))
            segundo_numero = int(input("Introduce el segundo número "))
        except ValueError as identifier:
            print("Números invalidos.")
        else:   
            resultado = realizar_operacion(opcion, primer_numero, segundo_numero)
            print("EL resultado final es " + str(resultado))  
            print()
    else:        
        print("Saliendo del programa.")
        break;


