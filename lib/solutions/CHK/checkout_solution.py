

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

def calculatePrice(item,qty):
    if(item == 'A'):
        if(qty >= 3):
            mult = qty/3
            price = mult * 130
            pro

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
        if(price == 0):
            return -1
        else:
            qty = skus[0:-1]
            return price * qty
    raise NotImplementedError()




