#!/usr/bin/python
#-*- coding: latin-1 -*-

#print("###############################################")
#print("################ HACK FIREFOX #################")
#print("###############################################")

import os
import sqlite3

##################################################################
directorio_actual = os.getcwd()
directorio_raiz =  os.path.join(os.getcwd(), "/")
##############################################################################
########## DESCIFRA EL HISTORIAL Y COOKIES DE LOS NAVEGADORES ################
##############################################################################

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

firefox()
