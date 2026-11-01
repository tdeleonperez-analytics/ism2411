#REFLECTION:
#1) Lists start at index 0, so the first item within a list is at position 0 rather than 1.
#2) In my retail job, I could have used lists to keep track of inventory, sales, and employee schedules. For example, I could have created a list of all the items in stock and their quantities, which would have made it easier to see what needed to be restocked.

print()
#Excercise 1: Build the List
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory, " | ", len(inventory))

print()
#Excercise 2: Index Practice
middle_index = len(inventory) // 2
print(inventory[0], " | ", inventory[-1], " | ", inventory[middle_index])

print()
#Excercise 3: Slicing 
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print()
#Excercise 4: Modify
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print()
#Exercise 5: Tuple Comparison
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinations because they cant' be changed, meaning the value stays the same and can't be influenced")
    print(coords)

print()
#Excercise 6: Average of a List of Sales
sales = [100, 250, 75, 480, 200]
sumSales = sum(sales)
count = len(sales)
avgSales = sumSales / count
bestDay = max(sales)
worstDay = min(sales)
print(f"Total: {sumSales} \nCount: {count} \nAverage: {avgSales} \nBest Sale: {bestDay} \nWorst Sale: {worstDay}")

print()
#Excercise 7: Accumulator Pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discValue = round(price - (price*.10), 2)
    discounted.append(discValue)
print(prices)
print(discounted)

print()
#Excercise 8: Filter Above Threshold 
salesV2 = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
highSales = []
for sale in salesV2:
    if sale > 300:
        highSales.append(sale)
print(highSales, " | Count: ", len(highSales), " | Average: ", round((sum(highSales) / len(highSales)), 2))