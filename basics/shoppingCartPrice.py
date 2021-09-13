prices = []
total = 0
while True:
    price = float(
        input(f"Press 0 to complete\nEnter Price of item {len(prices)+1}: $"))
    if price == 0:
        break
    prices.append(price)
for price in prices:
    total += price
if total:
    print(f"Total Price of {len(prices)} items= ${total}")
else:
    print("No Items :( Please purchase. We have great offers!")
