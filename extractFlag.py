### Author: Pablo ram (m3talm3rg3)
### Script para decodificar cifrado cesar 
### uso de python3
import argparse , string
from time import sleep
### Clase para agregar colores a nuestro script
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#abecedario apra descifar el texto
alfa= string.ascii_uppercase
def decrypt():
   f = open("decifrar.txt","r")
   print(f"{bcolors.WARNING}++++++----------{bcolors.FAIL}[++]{bcolors.WARNING}---Caesar Cipher Decryption---{bcolors.FAIL}[++]{bcolors.WARNING}---------++++")
   print(f"{bcolors.OKBLUE}Text to decryp: {bcolors.HEADER}",f.read())
   key = 12
   decrypted_message = ""
   with open("decifrar.txt") as fileobj:
      for ch in (fileobj.read()).upper(): 
         if ch in alfa:
            position = alfa.find(ch)
            new_position = (position - key) % 26
            new_character = alfa[new_position]
            decrypted_message += new_character
         else:
            decrypted_message += ch
      print(f"{bcolors.OKBLUE}\nDescifrando mensaje...\n")
      sleep(2) # give an appearance of doing something complicated
      print(f"{bcolors.OKCYAN}Casi Listo..\n")
      sleep(2) # more of the same
      flag_enc="TFN{Z3hqD_x3F_fT3_n4eFmDp5_S3f_K0g_p0iZ}"
      print(f"{bcolors.WARNING}[**]  {bcolors.FAIL} Flag descifrada previa{bcolors.OKGREEN}",decrypted_message[-41:])
      flag_dec=decrypted_message[-41:]
      flag=''
      for (c1, c2) in zip(flag_enc, flag_dec):
         if c1.isupper() and c2.isupper():
            flag+=c2
         else:
            flag+=c2.lower()
      print(f"{bcolors.WARNING}[*]  {bcolors.FAIL}Flag original descifrada:{bcolors.WARNING}",flag)
decrypt()
