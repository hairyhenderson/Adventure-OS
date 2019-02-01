import random

def GenerateLoot(TABLE, LUCK):
    LootTable = open(TABLE, "r")
    Luck = LUCK / 1000
    length = LootTable.readline()

    loot = []
    num = 0
    itemList =[]

    for i in range(0, int(length)):    
        item = LootTable.readline().split()
        itemList.append(item)

    print(itemList)
    print("-------------")

    for j in range(0, int(length)):

        num = 0
        for l in range(0, int(itemList[j][3])+(int(itemList[j][3])*int(Luck))):
            x = random.randint(0,1000)        
            if x <= int(itemList[j][2]):
                num += 1

        v = random.randint(-int(itemList[j][4]), int(itemList[j][4]))       
        num += v

        num = abs(num)
        if num > int(itemList[j][3]):
            num = int(itemList[j][3])
        
        loot.append({itemList[j][0]:num})

    print(loot)
