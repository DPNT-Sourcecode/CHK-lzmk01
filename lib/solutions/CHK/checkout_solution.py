

# noinspection PyUnusedLocal
# skus = unicode string

def getPrice(item):
    switcher =  {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }
    return switcher.get(item,0)
    

def checkout(skus):
    lengthOfSku = len(skus)

    if(lengthOfSku == 1):
        price = getPrice(skus)
        if(price == 0):
            return -1
        else:
            return price
    elif(lengthOfSku > 1):
        price = getPrice(skus[lengthOfSku - 1])
    raise NotImplementedError()


