#!/usr/bin/python
#-*- coding: latin-1 -*-

#print("###############################################")
#print("################ HACK CHROME ##################")
#print("###############################################")

import os
import sqlite3

##################################################################
directorio_actual = os.getcwd()
directorio_raiz =  os.path.join(os.getcwd(), "/")
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

chrome()
