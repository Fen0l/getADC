#!/usr/bin/env python3
import threading 
import pickle
import time
from datetime import datetime
import urllib.request
from bs4 import BeautifulSoup
import re
import string
import datetime
from time import gmtime, strftime
import json
import codecs
import subprocess;
import urllib
import urllib.request
import os

def PagetoSoup(url): # Mise en beauté de la page
	try:
		response = urllib.request.urlopen(url)
	except urllib.error.HTTPError as e:
		print("HTTPError with: ", url, " as ", e)
		return None
	return BeautifulSoup(response.read())

def printLogo():
    subprocess.call(["printf", "'\033c"]);
    print("\033[91m     ___     _____ ___  _   _ ____  ____  _____ ____ _   _    _    ____ ____  _____ ")
    print("    / \ \   / |_ _/ _ \| \ | / ___||  _ \| ____/ ___| | | |  / \  / ___/ ___|| ____|")
    print("   / _ \ \ / / | | | | |  \| \___ \| | | |  _|| |   | |_| | / _ \ \___ \___ \|  _|  ")
    print("  / ___ \ V /  | | |_| | |\  |___) | |_| | |__| |___|  _  |/ ___ \ ___) ___) | |___ ")
    print(" /_/   \_\_/  |___\___/|_| \_|____/|____/|_____\____|_| |_/_/   \_|____|____/|_____|"+ '\033[0m')
    print("")  
     
def getLast():
    printLogo()
    print("                 ------------------------------------------------------")
    print("                 - Recherche des images présentes")
    print("                 ------------------------------------------------------")
    time.sleep(1)
    high = 1
    tmp = ""
    for f in os.listdir("avc"):
        tmp = f
        tmp = tmp.replace('.png', ' ')
        try:
            tmp = int(tmp)
            if(tmp > high):
                high = tmp
        except:
            continue
    printLogo()
    print("                 ------------------------------------------------------")
    print("                 - Recherche des images présentes finie")
    print("                 - "+str(len(os.listdir("avc")))+" images trouvée(s)")
    print("                 ------------------------------------------------------")
    return high

if __name__ == '__main__':

    if not os.path.isdir('avc'):
        os.mkdir('avc')
        printLogo()
        print("                 ------------------------------------------------------")
        print("                 - Création du dossier avc")
        print("                 ------------------------------------------------------")
        time.sleep(1)
    i = getLast();
    page = "http://avionsdechasse.org/en/sexy/"+str(int(i))+"/"

    while (__name__ == '__main__'):
        try:
            ta = time.clock()
            mainPage = PagetoSoup(page)
            if(mainPage == None):
                i+=1
                continue
            ArrayCate = []
            Total = []
            next = []
            for column in ['avion-pic']:
                next[:] = []
                columnDiv = mainPage.find('div', {'class' : column})
                columnDivNext = mainPage.find('a', {'class' : "next-pic"})
                ArrayCate.extend(aDiv.get('src') for aDiv in columnDiv.findAll('img', src = re.compile('^http://avionsdechasse.org/images/images_sources')))
                if columnDivNext == None:
                    __name__ = ""
                    ArrayCate[:] = []
                next.extend(aDiv.get('href') for aDiv in columnDiv.findAll('a', href = re.compile('^http://avionsdechasse.org/en/sexy')))
                for url in ArrayCate:
                    i+=1
                    Total.append(url)
                    try:
                        with open("avc/"+str(i)+".png"): pass
                    except IOError:
                            data = urllib.request.urlretrieve(url, "avc/"+str(i)+".png")
                    print(Total)
                    print(ArrayCate)
                    printLogo()
                    print("                 ------------------------------------------------------")
                    print("                 - Total: "+str(len(os.listdir("avc")))+ " images(s)")
                    print("                 - Current: "+page)
                    for n in next:
                        page = n
                    print("                 - next: "+ page)
                    print("                 ------------------------------------------------------")
                try:
                    ArrayCate.remove(url)
                except:
                    print("End.")
        except IOError:
            print("Link error")
            break
