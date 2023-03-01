
#1 Números pares hasta el 100:
for i in range(0,101,2):
    print(i)

#2 Hacer una tabla de múltiplicar 
print("Tabla de multiplicar")
a=int(input("Por favor digite la tabla de multiplicar que desea ver:"))
for z in range (1,10):
        mult=z*a
        print(f"{a}x{z}={mult}")    

#3 Presente los años del usuario desde 1 hasta su edad
edad=int(input("Por favor ingresa tu edad: "))
for u in range (1,edad+1):
    print(u)

#4 Solicitar un número entero positivo y mostrar en pantalla números impares desde uno hasta ese núm 
numero=int(input("Por favor digite un número entero positivo: "))
contador=0
for h in range(0,+numero+1):
     
     if h %2 != 0 :
          contador=contador+1
          print(h,end=",")

#5 Suma de los números pares del 1 al 100:

suma=0
cont=0
for g in range (0,101):
     if g%2 ==0:
          cont=cont+1
          suma=suma+g

print("\nEl resultado de la suma de los números pares es ",suma)
          





    
     


