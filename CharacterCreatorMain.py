from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import CharacterClasses
import pickle
import pickletools

class characterCreateWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Adventrue OS Character Editor")
        self.root.geometry("400x400")
        self.root.iconbitmap(bitmap=None, default="Icons\Window Icon.ico")

        ttk.Style().configure("TButton", padding=10, relief="flat", background="grey")

        self.createWidgets()

    def createWidgets(self):
        charNameLabel= Label(self.root, text="Character Name")
        charNameLabel.pack(side=TOP)
        charName = ttk.Entry(self.root)
        charName.pack(pady= 10,side=TOP)

        char = CharacterClasses.Character(charName.get())
        print(char.name)

        skillBoxes = ttk.LabelFrame(self.root, text="Allocate Skill Points")
        skillBoxes.pack(fill=BOTH, side=BOTTOM)

        atkBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["atk"])
        defBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["def"])
        spdBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["spd"])
        vitBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["vit"])
        lukBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["luk"])
        dexBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["dex"])
        intBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["int"])
        chaBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["cha"])
        evaBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["eva"])
        strBox = ttk.Scale(skillBoxes, from_=-100, to= 100, variable = char.stats["str"])
        
        for c in sorted(skillBoxes.children):
            skillBoxes.children[c].pack(fill=X, pady=3)
        
    def onClose(self):
        """"""
        self.root.destroy()
    
    


