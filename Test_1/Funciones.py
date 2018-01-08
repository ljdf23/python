def pedir_pizza():
    print("Pedir pizza")
 
def checar_entrada(edad):
    if edad < 18:
        print("No puedes entrar".upper()) 
    elif edad >= 21:
        print("Puedes entrar al bar y beber")
    else:
        print("Puedes entrar al bar y no puedes beber")

edad = 21
edad_2 = 17

checar_entrada(edad)
checar_entrada(edad_2)
