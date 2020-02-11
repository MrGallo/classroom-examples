# Variables for each:

# item cost
# quantity
# subtotal
# tax
# total
# reciept

cost = 5.99
quantity = 6
subtotal = cost * quantity
tax = subtotal * 0.13
total = subtotal + tax

# print a reciept
print(f"Apples @ ${cost}   x {quantity}  = ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")
