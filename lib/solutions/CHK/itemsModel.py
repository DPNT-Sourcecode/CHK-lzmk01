from collections import namedtuple

BasketItem= namedtuple("Item",["basketSku"])

SuperMarketStockItem =  namedtuple(
    "StockItem", ["ItemName","ItemPrice","AsActiveDiscount","DiscountPrice","DiscountQunatity"]
)