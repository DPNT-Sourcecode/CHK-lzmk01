

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

def calculatePrice(item,qty,ppu):
    if(item == 'A'):
        if(qty >= 3):
            mult = qty/3
            rem = qty%3
            price = mult * 130
            price += rem * ppu
            return price
    elif(item == 'B'):
        if(qty >= 2):
            mult = qty/2
            rem = qty%2
            price = mult * 45
            price += rem * ppu
            return price
    else:
        return qty*ppu



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
