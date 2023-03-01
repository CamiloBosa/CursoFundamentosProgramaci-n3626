#Primer ejercicio

sueldoBase=int(input("Por favor digite el sueldo base: "))
valorVentas=int(input("Por favor digite el valor total de las ventas realizadas: "))
comisionVentas=valorVentas*0.10
sueldoTotal=sueldoBase + comisionVentas
print("El valor la comisión por las ventas del mes es= ${:,.0f} y el sueldo total es ${:,.0f}".format(comisionVentas,sueldoTotal))

#Segundo Ejercicio
valorCompra=float(input("Por favor digite el valor de la compra a realizar: "))
descuento=valorCompra-(valorCompra*0.15)
print(f"El valor de la compra es = {descuento}")
print("\n El valor de la compra en pesos es = ${:,.0f}".format(descuento))

#Cuarto ejercicio
mujeres=int(input("Digite el número de mujeres del grupo: "))
hombres=int(input("Digite el número de hombres del grupo: "))
porcentajeMujeres=(mujeres/(mujeres+hombres)*100)
porcentajeHombres=(hombres/(hombres+mujeres)*100)
print(f"El porcentaje de mujeres es: {porcentajeMujeres}%")
print(f"El porcentaje de hombres es: {porcentajeHombres}%")
