

import math
from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

def getPrice(item):
    switcher =  {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        'F': 10
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
        if((qty >= 5)):
            if((qty%5)<3):
                price = calPriceWithPromo(item,qty,5,ppu,200)
                return price
            else:
                frac,mult = math.modf(qty/5)
                price = calPriceWithPromo(item,(mult*5),5,ppu,200)
                price += calculatePrice(item,qty%5,ppu)
                return price
        elif(qty >= 3):
            price = calPriceWithPromo(item,qty,3,ppu,130)
            return price
        else:
            return qty*ppu
    elif(item == 'B'):
        if(qty >= 2):
            price = calPriceWithPromo(item,qty,2,ppu,45)
            return price
        else:
            return qty*ppu
    elif(item == 'E'):
        if(qty >= 2):
            price = qty*ppu
            return price
        else:
            return qty*ppu
    elif(item == 'F'):
        if(qty>=3):
            frac,freeCount = math.modf(qty/3)
            return (qty-freeCount)*ppu
        else:
            return qty*ppu
    else:
        return qty*ppu

def seperateItems(sku):
    items = []
    p=0
    for i in sku:
        validAlpha = i.isalpha() and (getPrice(i) != 0)
        if(not validAlpha and not i.isnumeric()):
            return []

    for i,l in enumerate(sku):
        if(l.isalpha()):
            items.append(sku[p:(i+1)])
            p = i+1
    
    uniq = []
    if(len(items) > 0):
        val = Counter(items)
        for k,v in val.items():
            uniq.append(str(v)+str(k))

        items = uniq
    
    return items

def calculate(item):
    itm = item[-1]
    qty = item[0:-1]
    itemPrice = getPrice(itm)
    if(qty.isnumeric()):
        return calculatePrice(itm,int(qty),itemPrice)
    else: return 0

def checkout(skus):
    if(skus):
        lengthOfSku = len(skus)
    
        if(lengthOfSku == 0):
            return -1

        price = 0
        items = seperateItems(skus)

        if(len(items) == 0):
            return -1

        for item in items:
            itm = item[-1]
            itemPrice = getPrice(itm)
            if(len(item)==1):
                itemPrice = getPrice(item)
                price+=itemPrice
            else:
                price += calculate(item)
        
        for item in items: 
            itm = item[-1]
            if(itm == 'E' and int(item[0:-1])>=2):
                for it in items:
                    im = it[-1]
                    if(im == 'B'):
                        frac,mult = math.modf(int(item[0:-1])/2)
                        if(int(it[0:-1]) == 2):
                           price -= calculatePrice('B',(int(it[0:-1])),30)
                           price+=mult*30
                           if(mult > 1):
                               price-=mult*30
                        else:
                            if(mult>=int(it[0:-1])):
                                price -= calculatePrice('B',(int(it[0:-1])),30)
                            else:
                                price -= calculatePrice('B',(mult),30)
        return price
    return 0


