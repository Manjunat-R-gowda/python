from functools import reduce

cart=[{"name":"laptop","price": 8000,"quantity": 1},
      {"name":"mouse","price":500,"quantity":2},
      {"name":"mointer","price":1200,"quantity":3}]

def name_list(item):
    return item["name"]
san=list(map(name_list,cart))

def some_cart(item):
    return item["price"]>1000
sagr=list(filter(some_cart,cart))

def price_inc(total,item):
    return total+item["price"]*item["quantity"]

saru=(reduce(price_inc,cart,0))

print("cart:-",cart)
print(san)
print(sagr)
print(saru)