import os

for valor in os.listdir('c:\windows\system32'):
	if valor[-3:] == 'exe':
		print valor