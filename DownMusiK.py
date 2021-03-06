import pafy
from pydub import AudioSegment
import os
print ("Que quieres descargar?")
print ("1. Lista predeterminanda")
print ("2. Introducir la url de tu lista.")
opcion = int(input("Opcion: "))
if opcion == 1:
	lista = "https://www.youtube.com/playlist?list=PLgLQAHLZtaRrenlDBCkwc2Rc-SR4Q_lQw"
elif opcion == 2:
	lista = raw_input("Introduce aqui tu lista: ")
else:
	print ("Opcion erronea. Vuelve a ejecutar")
	exit()
if not os.path.exists("MusiK"):
	os.mkdir("MusiK")
print ("ONLY TEKNO ALLOWED")
list = pafy.get_playlist(lista)
for i in list["items"]:
	title = ""
	for j in i["pafy"].title:
		if j == "<" or j == ">" or j == ":" or j == '"' or j == "/" or j == "|" or j == "?" or j == "*":
			title += "$"
		else:
			title += j
	if os.path.exists("MusiK/"+title+".mp3"):
		print (title+" already exists.")
	else:	
		print ("Downloading and converting..."+title)
		filename = i["pafy"].getbestaudio().download(quiet=False)
		AudioSegment.from_file(filename).export("MusiK/"+title+".mp3", format="mp3")
		os.remove(filename)
print ("Ale, gozatelo!")