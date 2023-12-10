class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
       
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        
        print(f"The restaurant {self.restaurant_name} is now open!")
        

restaurant = Restaurant("Mezze Magic", "Lebanese")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


restaurant1 = Restaurant("Nile Nosh", "Egyptian")
restaurant2 = Restaurant("Moroccan Mint", "Moroccan")
restaurant3 = Restaurant("Istanbul Inn", "Turkish")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class RestaurantWithCustomers(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        
        self.number_served += increment

restaurant_with_customers = RestaurantWithCustomers("QuickBites", "Fast Food")
print(f"\nNumber of customers served: {restaurant_with_customers.number_served}")

restaurant_with_customers.number_served = 30
print(f"Number of customers served: {restaurant_with_customers.number_served}")

restaurant_with_customers.set_number_served(50)
print(f"Number of customers served: {restaurant_with_customers.number_served}")

restaurant_with_customers.increment_number_served(20)
print(f"Number of customers served: {restaurant_with_customers.number_served}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("\nAvailable Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Coldstone", "Dessert", ["Chessecake", "cotton candy", "Strawberry"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()