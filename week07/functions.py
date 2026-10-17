# AI Use: Used the built-in AI of VS code to help code some of the functions, specifically when redoing the same thing but with different tiers/price (Shorten the time of coding)

#Self-Assessment Questions
#1) The first bug I spotted was the missing colon (:) at the end of the for loop on line 10. I spotted it since I was going through the code line by line and stumbled upon it. I can say my current debugging skills are mediocre since I only found it after going line by line
#2) apply_discount(price, tier) is a function that takes in the price and tier of a customer and returns the discounted price based on the tier. A collegue could probably use it without reading the body since I think the name of the function and the parameters are pretty self explanatory.
#3) AI helped build my understanding, especially with the continue and break statements since I didn't really understand them before even with the readings. I can definetly see how AI would shorten other ones understanding since its so easy to just hit [tab] on each recommendation and not really understand how the code runs/works. 

print()
#Exercise 1: calculate_tax
def calculate_tax(price, rate): 
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

print()
#Excercise 2: apply_discount
def apply_discount(price, tier):
    if tier.lower() == "gold":
        discount = 0.15
    elif tier.lower() == "silver":
        discount = 0.10
    elif tier.lower() == "bronze":
        discount = 0.05
    else: 
        discount = 0
    return price * (1 - discount)
print(f"Gold Tier Discount: ${apply_discount(200, 'gold'):.2f}")
print(f"Silver Tier Discount: ${apply_discount(200, 'silver'):.2f}") 
print(f"Bronze Tier Discount: ${apply_discount(200, 'bronze'):.2f}")
print(f"No Tier Discount: ${apply_discount(200, 'none'):.2f}")

print()
#Excercise 3: Compose Them
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    total_price = calculate_tax(discounted_price, tax_rate)
    return round(total_price, 2)

starting_price = 200
discounted_step = apply_discount(starting_price, "gold")
final_step = discounted_step + calculate_tax(discounted_step, 0.07)

print(f"After gold discount: ${discounted_step:.2f}")
print(f"After tax: ${final_step:.2f}")
result = discounted_step + final_price(200, "gold", 0.07)
print(f"final_price(200, 'gold', 0.07) = ${result:.2f}")

print()
#Excercise 4: Loop + Function
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

print()
#Excercise 5: Debug first, Then ask
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

print()
#Excercise 6: Scope Experiment
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here? 100 since it refers to the global variable x
print(double_it()) # what prints here? 1998 since it goes into the function which returns the local variable x * 2
print(x)           # has x changed? No, it remains 100 since it still calls the global variable x. The other x is ONLY within the function
