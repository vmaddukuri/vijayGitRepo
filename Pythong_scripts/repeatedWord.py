def repeatCount(sentance):
    words=sentance.split(" ")
    print words
    dict={}
    for n in words:
        keys=dict.keys()
        print n
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict

sentance='I am vijay I vijay'
count=repeatCount(sentance)
print count