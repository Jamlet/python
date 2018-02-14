import os

letra = raw_input("Dime una letra: ")
total = 0
ficheros = os.listdir('c:\windows\system32')
for valor in ficheros:
	if valor.count(letra) > 0:
		total += 1

print "De un total de " + str(len(ficheros)) + " archivos hay " + str(total) + " que contienen la letra " + letra