def hola():
	print "Que me dejes!"
	
def adios():
	return "Menos mal!"
	
def paroimpar(num):
	return "par" if num%2==0 else "impar"

def alta_cliente(dni,nombre,*apellidos):
	print "DNI: " + str(dni)
	apellidos_completos = ''
	for apellido in apellidos:
		apellidos_completos += " " + apellido.capitalize() 
	print nombre + apellidos_completos
	
def iniciales(nombre,*apellidos):
	nombre_completo = nombre[0].upper()
	for apellido in apellidos:
		nombre_completo += "." + apellido[0].upper()
	return nombre_completo