precioP = float(input("Ingresa el precio del producto: "))
imp = precioP * .16
tot = precioP + imp
print ("Cantidad a pagar: " , tot)
din = float(input("Ingresa la cantidad recibida: "))

if din >= tot:
	cam = din - tot
	print ("___________________________")
	print ("Impuestos: " , imp)
	print ("Total: " , tot)
	print ("Dinero recibido: " , din)
	print ("Su cambio: " , cam)

else: print("\nSu compra es invalida")
input("...")