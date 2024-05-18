def order_pizza(pizza_type, extra_topping): 
    
    pizza = "Make a " + pizza_type + " pizza with " + extra_topping + "."
    return pizza

first_pizza = order_pizza("Pepperoni", "Extra Cheese")
print(first_pizza)

second_pizza = order_pizza("Chicken Fajita", "Extra Olives")
print(second_pizza)


