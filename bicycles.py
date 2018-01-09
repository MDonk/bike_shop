class bicycle:
    # Creates a bicycle with it's details.
    def __init__(self, model, cost):
        self.model = model
        self.cost = cost
        
    # Structures bicycle details in easy to read format.
    def __repr__(self):
        return "model:{model}, cost:{cost}".format(model=self.model, cost=self.cost)
        
class shop:
    # Creates a shop.
    def __init__(self, shop_name):
        self.shop_name = shop_name
        # Creates inventory dictionary.
        self.inventory = {}
        self.retail = 1.2
    
    # Add's bicycles into inventory dictionary for bicycles.
    def inital_inventory(self, bicycle, quantity):
        self.inventory[bicycle] = quantity

    # Changes bike from cost price to retail price.
    # Playing with code first to see if it's accessing the dictonary properly.
    # Can't access cost in objects in inventory dictionary
    # Doesn't work!
    def retail_price(self):
        for cost in self.inventory:
            print(cost)
        
class customer:
    # Creates a customer, with there bicycle budget.
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        # Creates list of affordable bikes for customer.
        self.bike_choices = []
    
    # Determines which bikes a customer can afford and adds them to bike_choices list.
    # Doesn't work!
    def afforable_bikes (self):
        for bicycle in bikes4you.inventory:
            if bicycle.cost <= self.budget:
                self.bike_choices.append(bicycle)
            return self.bike_choices

# Creates objects for bicycle.
bike1 = bicycle("red", 700)
bike2 = bicycle("blue", 800)
bike3 = bicycle("black", 400)
bike4 = bicycle("green", 300)
bike5 = bicycle("pink", 100)
bike6 = bicycle("yellow", 120)

# Creates instance for shop.
bikes4you = shop("bikes4you")

# Add's bicycle objects to inventory dictonary.
bikes4you.inital_inventory(bike1, 1)
bikes4you.inital_inventory(bike2, 1)
bikes4you.inital_inventory(bike3, 1)
bikes4you.inital_inventory(bike4, 1)
bikes4you.inital_inventory(bike5, 1)
bikes4you.inital_inventory(bike6, 1)

# Creates customer objects.
tim = customer("tim", 200)
jack = customer("jack", 500)
tom = customer("tom", 1000)

# Prints inventory.
print(bikes4you.inventory)

# Prints customer and list of bikes they can afford.
tim.afforable_bikes()
print(tim.bike_choices)

# Prints 
bikes4you.retail_price()
