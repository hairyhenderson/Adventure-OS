from tkinter import filedialog

#### Item Reader ####

def readItem():
    try:
        path = filedialog.askopenfilename(initialdir ="/", title="Select Item File")
        itemList = open(path, "r")

        allItems=[]
        
        amount = itemList.readline()

        for i in range (0, int(amount)):
            info = itemList.readline().split()
            
            name = info[0].replace("_"," ")
            
            itemId = info[1]
            
            statsList = info[2].split('|')
            
            stats = {}
            
            for x in range (0, len(statsList)):
                stats.update({int(statsList[x].split('/')[0]): statsList[x].split('/')[1]})

            weight = float(info[3])
            price = info[4].split('/')

            description = info[5].replace("_"," ")

            itemData = {"Name":name, "Id":itemId, "Stats":stats, "Weight":weight, "Price":price, "Description":description}

            allItems.append(itemData)
        
        return(allItems)
        
    finally:
        pass
    
    

