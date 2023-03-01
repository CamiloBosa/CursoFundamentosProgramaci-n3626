print("Por favor digite los datos solicitados a continuación")
Identificacion=int(input("Número de identificación: "))
Nombres=str(input("Nombres: "))
Apellidos=str(input("Apellidos: "))
Direccion=str(input("Dirección: "))
Telefono=str(input("Teléfono: "))
Edad=int(input("Edad: "))
EstadoCivil=str(input("EstadoCivil: "))
NumeroDeHijos=int(input("Número de hijos: "))
Estatura=float(input("Estatura en centimetros: "))
FechaDeContratacion=str(input("Fecha de contratación (Día/mes/año): " ))
Sueldo=int(input("Sueldo Básico: $"))
DiasLaborados=int(input("Días laborados: "))

print("-------------------------------------------------------------------")
print("El usuario es "+Nombres+" "+ Apellidos)
print("Su dirección es: "+ Direccion)
print("Su teléfono es: "+ Telefono)
print("Su edad es: "+ str(Edad))
print("su estado civil es:"+ EstadoCivil)
print("Reporta tener: "+ str(NumeroDeHijos)+" hijos")
print("Su estatura es:"+str(Estatura))
print("La fecha de su contratación es:"+FechaDeContratacion)
print("Su sueldo es: "+ str(Sueldo))
print("Usted ha laborado un total de :"+str(DiasLaborados))


#Condicionales
#1
if Edad>55:
    Bono=0.05*Sueldo
    print("El empleado tiene bono el que corresponde a ${:,.0f}".format(Bono))
else:
    print("El empleado no aplica para el bono")
#2

if  EstadoCivil=="casado" and NumeroDeHijos>0:
    print("Al empleado le será otorgado un paseo en diciembre")
else:
    print("Al empleado no le será otorgado un paseo en diciembre")

#3
if Sueldo>1000000 and Sueldo<1500000:
    Comision=0.02*Sueldo
    TotalSueldo=Sueldo+Comision
    print("El valor de la comisión es ${:,.0f} y el total del sueldo sería ${:,.0f}".format(Comision,TotalSueldo))

elif Sueldo>1500001 and Sueldo<2000000:
    Comision=0.05*Sueldo
    TotalSueldo=Sueldo+Comision
    print("El valor de la comisión es ${:,.0f} y el total del sueldo sería ${:,.0f}".format(Comision,TotalSueldo))
else:
    print("En este caso no aplica comisión el sueldo es: ${:,.0f}".format(Sueldo))

#4
if DiasLaborados>20 and Sueldo<1000000:
    print("Aplica bono de alimentación")
else:
    print("No aplica bono de alimentación ")




