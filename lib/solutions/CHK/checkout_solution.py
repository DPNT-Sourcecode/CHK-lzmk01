import math
from collections import Counter
#from itemsModel import SuperMarketStockItem, BasketItem
from collections import namedtuple

BasketItem= namedtuple("Item",["basketSku"])

SuperMarketStockItem =  namedtuple(
    "StockItem", ["ItemName","ItemPrice","AsActiveDiscount","AsSpecialDscount","DiscountPrice","DiscountQuantity","SpecialDscountName"]
)

# noinspection PyUnusedLocal
# skus = unicode string

STORE_ITEM = [
    SuperMarketStockItem('A',50,True,[130,200],[3,5],''),
    SuperMarketStockItem('B',30,True,[45],[2],''),
    SuperMarketStockItem('C',20,False,False,[],[],''),
    SuperMarketStockItem('D',15,False,False,[],[],''),
    SuperMarketStockItem('E',40,False,True,[],[2],'1B'),
    SuperMarketStockItem('F',10,False,True,[],[2],'1F'),
    SuperMarketStockItem('G',20,False,False,[],[],''),
    SuperMarketStockItem('H',10,True,False,[45,10],[5,10],''),
    SuperMarketStockItem('I',35,False,False,[],[],''),
    SuperMarketStockItem('J',60,False,False,[],[],''),
    SuperMarketStockItem('K',80,True,False,[150],[2],''),
    SuperMarketStockItem('L',90,False,False,[],[],''),
    SuperMarketStockItem('M',15,False,False,[],[],''),
    SuperMarketStockItem('N',40,False,True,[],[3],'1M'),        
    SuperMarketStockItem('0',10,False,False,[],[],''),
    SuperMarketStockItem('P',50,True,False,[5],[100],''),
    SuperMarketStockItem('Q',30,True,False,[80],[3],''),
    SuperMarketStockItem('R',50,False,True,[],[3],'1Q'),
    SuperMarketStockItem('S',30,False,False,[],[],''),
    SuperMarketStockItem('T',20,False,False,[],[],''),
    SuperMarketStockItem('U',40,False,True,[],[3],'1U'),
    SuperMarketStockItem('V',50,True,False,[2,3],[90,130],''),
    SuperMarketStockItem('W',20,False,False,[],[],''),
    SuperMarketStockItem('X',90,False,False,[],[],''),
    SuperMarketStockItem('Y',10,False,False,[],[],''),
    SuperMarketStockItem('Z',50,False,False,[],[],''),
]

def getPrice(storeItem):
    for item in STORE_ITEM:
        return item[storeItem]

    switcher =  {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        'F': 10
    }
    return switcher.get(storeItem,0)

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
            storeItem = item[-1]
            itemPrice = getPrice(storeItem)
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

