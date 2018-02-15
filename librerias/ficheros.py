import os

def creadir(dir):
	ruta = '/tmp/'+dir
	if os.access(ruta,1):
		return "Ya existe el directorio " + dir
	os.mkdir(ruta)
	return "He creado el directorio " + dir
