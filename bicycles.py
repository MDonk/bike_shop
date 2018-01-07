class bicycle(object):
    def __init__(self, cost):
        self.cost = cost

    def sale_price(self, cost):
        for self.cost in cost:
            self.cost += 10

class customer(object):
    def __init__(self, budget):
        self.budget = budget
            
red = bicycle([700])
blue = bicycle([800])
black = bicycle([400])
green = bicycle([300])
pink = bicycle([100])
yellow = bicycle([120])

Tim = customer([200])
Jack = customer([500])
Tom = customer([1000])

bikes = bicycle(object)
bikes.sale_price()