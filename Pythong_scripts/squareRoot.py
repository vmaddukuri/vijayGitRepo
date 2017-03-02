def isSquare(itemList):
    FinalList=[]
    for value in itemList:
        item = 0
        while item*item < value:
            item=item+1
            if item*item == value:
                newItem=item
            else:
                newItem=value*value
        FinalList.append(newItem)
    return FinalList

itemList=[1,2,3,4,9,10]

newList=isSquare(itemList)
print newList

