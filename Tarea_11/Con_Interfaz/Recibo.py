import tkinter
def recibo(pp, cr):
	imp = pp * .16
	tot = pp + imp
	print ("Cantidad a pagar: " , tot)

	if cr >= tot:
		cam = cr - tot
		print ("___________________________")
		print ("Impuestos: " , imp)
		print ("Total: " , tot)
		print ("Dinero recibido: " , cr)
		print ("Su cambio: " , cam)
	else: 
		print("\nSu compra es invalida")

def CJ1():
	pp = cajaTexto1.get()
	return pp
def CJ2():
	cr = cajaTexto2.get()
	return cr			
#------------------------------------------------------------------------------------------------------------------------
ventana = tkinter.Tk()
ventana.geometry("225x125")
#------------------------------------------------------------------------------------------------------------------------
instruccion1 = tkinter.Label(ventana, text = "Ingresa el precio del producto:")
instruccion1.pack()

cajaTexto1 = tkinter.Entry(ventana)
cajaTexto1.pack()
#------------------------------------------------------------------------------------------------------------------------
instruccion2 = tkinter.Label(ventana, text = "Ingresa la cantidad recibida: ")
instruccion2.pack()

cajaTexto2 = tkinter.Entry(ventana)
cajaTexto2.pack()
#------------------------------------------------------------------------------------------------------------------------
boton = tkinter.Button(ventana, text = "Buscar", padx = 20, pady =10, command = lambda: recibo(float(CJ1()), float(CJ2())))
boton.pack()

ventana.mainloop()