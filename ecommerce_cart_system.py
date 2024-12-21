cart_items = {'Laptop': 50000,'Headphones': 2000,'Mouse': 500,'Keyboard': 1500}
def calculate_total (cart_items):
    if not cart_items:
        return "Cart is empty. Please add items to your cart."
    else:
        total_price = sum(cart_items.values())
        if len (cart_items)>5:
            total_price = total_price - ((total_price*10)/100)
        else:
            return total_price

result = calculate_total(cart_items)
if isinstance (result,str):
    print(result)
else :
    print (f"Total Price: {result:.2f}")