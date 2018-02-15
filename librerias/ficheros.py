import os

def creadir(dir):
	ruta = '/tmp/'+dir
	if os.access(ruta,1):
		return "Ya existe el directorio " + dir
	os.mkdir(ruta)
	return "He creado el directorio " + dir

def entorno():
	respuesta = {}
	for x,a in os.environ.iteritems():
		if x == 'USER':
			respuesta['user'] = a
		if x == 'SHELL':
			respuesta['shell'] = a
		if x == 'PATH':
			respuesta['path'] = a
	return respuesta

def limpiar():
	os.system("clear")

def gordos(dir,size):
	archivos = os.listdir(dir)
	size_final = int(size[:-1])
	tipo = int({'K':1,'M':2,'G':3}[size[-1:]])o
	while tipo - 1 > 0:
		size_final *= 1024
		tipo -= 1
	for archivo in archivos:
		if os.path.isfile(archivo) and os.path.getsize(archivo) > size_final:
			print archivo + ' pesa ' + str(os.path.getsize(dir+archivo))

def visualizar(fichero):
	documento = open(fichero)
	print documento.read()
