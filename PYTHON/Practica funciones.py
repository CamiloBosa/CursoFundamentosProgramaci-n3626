#Dentro de una función es local y por fuera de la función es global
#Las funcciones deben ser preferiblemente en variables locales

def suma(n1,n2):
    res= num1+num2
    return res

num1=int(input("Ingrese el número 1:"))
num2=int(input("Ingrese el número 2:"))
# print(n1)
suma(num1,num2)

x = 4
def oper(a):
    a=a*a
    return a
resultado = oper(x)
print(resultado)

def saludar(nom):
    print("Hola "+nom+"!!!")

resp="si"
while resp=="si" or resp=="s":
    nombre=input("Digite su nombre: ")
    saludar(nombre)
    resp=input("¿Desea saludar a otra persona? ")


def validarestatura(est):
    if est >1.50:
        print("Eres una persona alta")
    else:
        print("Eres una persona chaparra")

resp="si"
while resp=="si" or resp=="s":
    estatura=float(input("Digite su estatura: "))
    validarestatura(estatura)
    resp=input("¿Desea realizar una comparación?")

