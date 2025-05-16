item_price = 50.00
customer_has_coupon = True

print(f"customer_has_coupon: {customer_has_coupon}, item_price: {item_price}")

if customer_has_coupon == True:
    final_price = item_price * 0.90
  
else:
   final_price = item_price

print (f"Price: ${final_price:.2f}")   
   


