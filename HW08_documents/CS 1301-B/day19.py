
def update_prices(productPriceDict, productDiscount):
    for product, discount in productDiscount:
        if product in productPriceDict:
            productPriceDict[product] = round((productPriceDict[product] - discount), 2)
        else:
            productPriceDict[product] = discount

    return productPriceDict

        
            


