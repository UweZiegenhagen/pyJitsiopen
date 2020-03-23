import tkinter as tk # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
import webbrowser

url = "https://www.dingfabrik.de"

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 


def openweb(): # https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270
    webbrowser.open(url,new=1)

def myprint():
    print('Hello World')

app = tk.Tk()

app.geometry('800x600')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=200, font=('Helvetica', 16))
opt.pack(side="top")

readOnlyText = tk.Text(app, height=2, width=100) # https://www.delftstack.com/de/howto/python-tkinter/how-to-make-tkinter-text-widget-read-only/
readOnlyText.insert(END,"ABCDEF")
#readOnlyText.configure(state='disabled')
readOnlyText.pack(side="bottom")


labelTest = tk.Label(text="", font=('Helvetica', 16), fg='red')
labelTest.pack(side="top")

buttonBrowser = tk.Button(app, 
              text="Open browser",command=openweb) # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
buttonBrowser.pack(side="bottom")


buttonExample = tk.Button(app, 
              text="Do something",command=myprint) # https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
buttonExample.pack(side="bottom")


def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))
    readOnlyText.insert(END,variable.get())
    
variable.trace("w", callback)

app.mainloop()