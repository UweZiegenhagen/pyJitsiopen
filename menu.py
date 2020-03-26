#!/usr/bin/env python3

"""
Uwe Ziegenhagen, ziegenhagen@gmail.com
Simple tkinter GUI to start a Jitsi Meeting
"""

import tkinter as tk # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
import webbrowser
import configparser
from urllib.request import urlopen 
from urllib.error import HTTPError, URLError
import os.path


def internet_on():
    """
     Check online status
    """
    try:
        urlopen('https://github.com', timeout=2)
        return True
    except HTTPError as error: 
        return False
    except URLError as error: 
        return False 
    
url = ""
this_version = 0.1
standort = ''

# read URLs and names from Einstellungen.conf
Config = configparser.ConfigParser()
Config.read('Einstellungen.conf', encoding='utf-8')

# prepare lists of servers and names
servers = Config.items('Server')
serverList = []
for server in servers:
    serverList.append(server[1])


nameList = [] # leeres Array anlegen
nameConfig = configparser.ConfigParser()

# check if file exists, create one if necessary
# https://linuxize.com/post/python-check-if-file-exists/
if os.path.isfile('namen.txt'):
    print ("Namensdatei existiert")
else:
    print ("Namensdatei existiert nicht, wird angelegt")
    with open('namen.txt', 'wt') as names:
        names.write('[Standort]\nStandort=Altersheim ohne Umlaute\n')
        names.write('[Namen]\n')
        names.write('Name1=Max Mustermann\n')
        names.write('Name2=Gabriele Mustermann\n')        
        names.write('Name3=Marianne Mustermann\n')        

nameConfig.read('namen.txt', encoding='utf-8')

standort = nameConfig.get('Standort', 'Standort').replace(' ','').lower()

names = nameConfig.items('Namen')
for name in names:
    nameList.append(name[1])


def update():
    pass

def openweb():
    """
       Open default browser
       based on https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270
    """
    global url
    url = currentServer.get() + '/' + standort + '-' + currentName.get().replace(' ','').lower()
    print(url)
    webbrowser.open(url,new=1)


onlineCheck = internet_on()
if onlineCheck == True:
    onlineString = 'Mit dem Internet verbunden'
else:
    onlineString = 'Keine Verbindung zum Internet!'


# Check the version
# https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont
version_online = urlopen('https://raw.githubusercontent.com/UweZiegenhagen/pyJitsiopen/master/latest_version')
version_online = float(version_online.read())

app = tk.Tk() # the tkinter panel
app.title('Dingfabrik.de Jitsi-Zugang ' + str(this_version) + ': ' + onlineString)

app.geometry('800x400') # 800x600 should be fine for all laptops

currentServer = tk.StringVar(app) # some tkinter stuff
currentServer.set(serverList[0])

currentName = tk.StringVar(app) # more tkinter stuff
currentName.set(nameList[0])

url = currentServer.get() + '/' + currentName.get().replace(' ','')

srv = tk.OptionMenu(app, currentServer, *serverList) # dropdown for the server
srv.config(width=200, font=('Helvetica', 16))
srv.pack(side="top")

namedropdown = tk.OptionMenu(app, currentName, *nameList) # dropdown for the names
namedropdown.config(width=200, font=('Helvetica', 16))
namedropdown.pack(side="top")


urlText = tk.Text(app, height=2, width=100, font=('Helvetica', 16)) # https://www.delftstack.com/de/howto/python-tkinter/how-to-make-tkinter-text-widget-read-only/
urlText.delete(1.0, tk.END)

if version_online > this_version:
    urlText.insert(tk.END,'Eine neue Version ist online verfügbar')
    # TODO: https://www.freecodecamp.org/forum/t/git-pull-how-to-override-local-files-with-git-pull/13216
else:
        urlText.insert(tk.END,'Diese Version ist aktuell!')

urlText.pack(side="bottom")



# a label for the server url
labelTest = tk.Label(text="", font=('Helvetica', 16), fg='green')
labelTest.pack(side="top")

# the button to initiate the Jitsi session
buttonBrowser = tk.Button(app, 
              text="Starte Jitsi",font=('Helvetica', '20'), command=openweb) # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
buttonBrowser.pack(side="bottom") # put it at the bottom

buttonUpdate = tk.Button(app, 
              text="Aktualisieren",command=update, state=tk.DISABLED, font=('Helvetica', '20')) # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
buttonUpdate.pack(side="left")


def callback(*args):
    global url
    url = currentServer.get() + '/' + standort + '-' + currentName.get().replace(' ','').lower()
    print(url)
    labelTest.configure(text=url)

# call the callback() function if server or name dropdown is used.
currentName.trace("w", callback)
currentServer.trace("w", callback)

app.mainloop()