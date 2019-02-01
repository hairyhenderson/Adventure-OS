from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import ItemFunc as Item
import RNG as RNG
import CharacterClasses
import Data
import CharacterCreatorMain as charCreate
import pickle
import pickletools

################ GUI LAYOUT #####################
## FUNCTIONS #
class mainWindow:
    def closeWindow(self):
        self.root.destroy()
    
    def createWindow(self, window):
        createCharWindow = window()

    def __init__(self):
        self.root = Tk()
        self.root.title("Adventure OS RPG")
        self.root.geometry("700x500")
        self.root.iconbitmap(bitmap=None, default="Icons\Window Icon.ico")


        self.createWidgets()

    def createWidgets(self):
        # Styles #
        ttk.Style().configure("TButton", padding=10, relief="flat", background="grey")

        # GUI #

        main = PanedWindow(self.root)
        main.pack(fill=BOTH, expand=1)

        topMenu = Menu(main)
        filemenu = Menu(topMenu, tearoff =0)
        rpgmenu = Menu(topMenu, tearoff =0)
        rpgmenu.add_command(label="New RPG")
        rpgmenu.add_command(label="Join RPG")
        rpgmenu.add_command(label="Save RPG")
        rpgmenu.add_command(label="Save RPG as...")
        rpgmenu.add_command(label="Close RPG")

        filemenu.add_separator()

        filemenu.add_command(label="New Character", command = self.createWindow(charCreate.characterCreateWindow))
        filemenu.add_command(label="Open Character")
        filemenu.add_command(label="Save Character")
        filemenu.add_command(label="Save Character as...")

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command =self.closeWindow)
        topMenu.add_cascade(label="File", menu=filemenu)
        topMenu.add_cascade(label="Game", menu=rpgmenu)
        #topMenu.add_cascade(label="Settings", menu=setmenu)

        self.root.config(menu=topMenu)

        leftPane = ttk.Frame(main)
        main.add(leftPane)

        rightPane = ttk.Frame(main)
        main.add(rightPane)

        #LEFT SIDE
        #top
        statsFrame = ttk.LabelFrame(leftPane, text="Username Here")
        statsFrame.pack()

        charIcon = Canvas(statsFrame, bg="blue", height=128, width=128)
        charIcon.pack(side=LEFT)

        topText = ttk.Frame(statsFrame)
        topText.pack(side=TOP, padx=5,pady=5)

        charName = ttk.Label(topText, text = "Character Name Here")
        charName.config(font=("Segoe UI", 15))
        charName.grid(column=0, row = 0, sticky=NW)

        HP = ttk.Label(topText, text = "HP")
        HP.grid(column=1, row = 1, sticky=W)

        charHealth = ttk.Progressbar(topText, orient="horizontal", length=200)
        charHealth.grid(column=0, row = 1, sticky=W, pady=3)

        AP = ttk.Label(topText, text = "AP")
        AP.grid(column=1, row = 2, sticky=W)

        charAct = ttk.Progressbar(topText, orient="horizontal", length=200)
        charAct.grid(column=0, row = 2, sticky=W, pady=3)

        EXP = ttk.Label(topText, text = "EXP")
        EXP.grid(column=1, row = 3, sticky=W)

        charExp = ttk.Progressbar(topText, orient="horizontal", length=200)
        charExp.grid(column=0, row = 3, sticky=W, pady=3)

        LVL = ttk.Label(topText, text = "LVL")
        LVL.grid(column=0, row = 4, sticky=W)

        lvlVar = ttk.Label(topText, text = "'level'")
        lvlVar.grid(column=1, row = 4, sticky=W)

        #bottom
        charInfo = ttk.LabelFrame(leftPane, text = "Character Info")
        charInfo.pack(side = LEFT, fill= Y)

        charMenu = ttk.Notebook(charInfo, height = 400)
        tabInv = ttk.Frame(charMenu)
        tabStat = ttk.Frame(charMenu)
        tabSpell = ttk.Frame(charMenu)

        charMenu.add(tabInv, text = "Inventory")
        charMenu.add(tabStat, text = "Stats")
        charMenu.add(tabSpell, text = "Abilities")

        charMenu.pack(fill=BOTH)

        #INVENTORY#

        invList = Listbox(tabInv, width = 50)
        invList.pack(fill=BOTH, side = TOP, expand = 1)

        invMenu = ttk.Frame(tabInv)
        invMenu.pack(fill=BOTH, side=BOTTOM)

        createItem = ttk.Button(invMenu, text="Create Item")
        openItem = ttk.Button(invMenu, text="Open Item", command = Item.readItem)

        createItem.pack(side=LEFT)
        openItem.pack(side=LEFT)

        #RIGHT SIDE
        chat = ttk.LabelFrame(rightPane,text="Chat Name Here")
        chat.pack()

        chatMenu = ttk.Frame(rightPane, width=50)
        chatMenu.pack(side = RIGHT, fill = Y)

        partyTxt = ttk.Button(chatMenu, text ="Party Chat")
        partyTxt.pack(fill=X, side = BOTTOM, padx = 5, pady =5)

        newTxt = ttk.Button(chatMenu,text ="New Chat")
        newTxt.pack(fill=X, side = BOTTOM, padx = 5, pady =5)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    app = mainWindow()
    app.root.mainloop()