product_prices=[98,198,298,398,498]

def addone(price):
    return price+1

mpa_obj=map(lambda price:price+1,product_prices)

new_prices=list(mpa_obj)
print(product_prices)
print(new_prices)