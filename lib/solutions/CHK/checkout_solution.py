

import math
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

def calPriceWithPromo(item,qty,promoQty,ppu,promoPrice):
    frac,mult = math.modf(qty/promoQty)
    rem = qty%promoQty
    price = mult * promoPrice
    price += rem * ppu
    return price

def calculatePrice(item,qty,ppu):
    if(item == 'A'):
        if(qty >= 3):
            price = calPriceWithPromo(item,qty,3,ppu,130)
            return price
    elif(item == 'B'):
        if(qty >= 2):
            price = calPriceWithPromo(item,qty,2,ppu,45)
            return price
    else:
        return qty*ppu

def seperateItems(sku):
    items = []
    p=0
    for i,l in enumerate(sku):
        validItem = (getPrice(l) != 0)
        validNumber = (sku[p:(i)]).isnumeric()

        if(l.isalpha()):
            if(validItem and validNumber):
                items.append(sku[p:(i+1)])
                p = i+1
            else: p = i
        
        return items



def checkout(skus):
    if(skus):
        lengthOfSku = len(skus)
    
        if(lengthOfSku == 0):
            return -1

        price = 0
        items = seperateItems(skus)
        if(lengthOfSku == 1):
            return itemPrice
        elif(lengthOfSku > 1):
            qty = skus[0:-1]
            if(qty.isnumeric()):
                return calculatePrice(item,int(qty),itemPrice)
            else: return -1
    
    return 0

