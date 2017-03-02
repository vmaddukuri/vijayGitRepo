def sort(itemList):
    for i in range(len(itemList)-1,0,-1):
        for j in range(i):
            if itemList[j]>itemList[j+1]:
                temp=itemList[j]
                itemList[j]=itemList[j+1]
                itemList[j + 1]=temp
    return itemList

newList=sort(['is2', 'Thi1s', 'T4est', '3a'])
newList=sort(['b1',2,5,3,'a1'])
print newList

