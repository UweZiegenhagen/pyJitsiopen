import tkinter as tk # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
from tkinter import font as tkFont  # https://stackoverflow.com/questions/20588417/how-to-change-font-and-size-of-buttons-and-frame-in-tkinter-using-python/20588878
import webbrowser
import configparser


# helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')

url = "https://www.dingfabrik.de"

Config = configparser.ConfigParser()
Config.read('Einstellungen.conf', encoding='utf-8')

servers = Config.items('Server')
serverList = []
for server in servers:
    serverList.append(server[1])

names = Config.items('Namen')
print(names)
nameList = []
for name in names:
    nameList.append(name[1])


def openweb(): # https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270
    webbrowser.open(url,new=1)

def onButton():
    """
        What is happen once the "Do something" button is pressed
    """
    pass

app = tk.Tk()

app.geometry('800x400') # 800x600 should be fine for all laptops

currentServer = tk.StringVar(app)
currentServer.set(serverList[0])

currentName = tk.StringVar(app)
currentName.set(nameList[0])

srv = tk.OptionMenu(app, currentServer, *serverList)
srv.config(width=200, font=('Helvetica', 16))
srv.pack(side="top")

namedropdown = tk.OptionMenu(app, currentName, *nameList)
namedropdown.config(width=200, font=('Helvetica', 16))
namedropdown.pack(side="top")


urlText = tk.Text(app, height=2, width=100) # https://www.delftstack.com/de/howto/python-tkinter/how-to-make-tkinter-text-widget-read-only/
#urlText.insert(tk.END,"ABCDEF")
#urlText.pack(side="bottom")


labelTest = tk.Label(text="", font=('Helvetica', 16), fg='red')
labelTest.pack(side="top")

buttonBrowser = tk.Button(app, 
              text="Starte Jitsi",font=('Helvetica', '20'), command=openweb) # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
#buttonBrowser['font'] = helv36
buttonBrowser.pack(side="bottom")


buttonExample = tk.Button(app, 
              text="Dingfabrik Köln",command=openweb) # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
#buttonExample.pack(side="bottom")


def callback(*args):
    url = currentServer.get() + '/' + currentName.get().replace(' ','')
    labelTest.configure(text=url)
    #urlText.delete(1.0,tk.END)
    #urlText.insert(tk.END,url)
    
currentName.trace("w", callback)
currentServer.trace("w", callback)

app.mainloop()