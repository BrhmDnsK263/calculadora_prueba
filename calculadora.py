def suma(num_a,num_b):
    return num_a+num_b


a = int(input("ingrese un numero: "))
b = int(input("ingrese otro numero: "))

opcion = 0
while opcion not in (1,2,3):
    print("1-Suma")
    print("2-Resta")

    opcion = int(input("ingrese opcion: "))

if opcion == 1:
    print(suma(a,b))
else:
    print(a-b)