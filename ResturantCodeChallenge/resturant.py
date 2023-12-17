from lib.customer import Customer
from lib.review import Review


class Restaurant:

    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self.name

    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set(review.customer() for review in self._reviews))
    
    def customers(self):
        return list(self._customers.keys())
    
    def average_star_rating(self):
        total_rating = sum(review.rating() for review in self._reviews)
        number_of_reviews = len(self._reviews)
        if number_of_reviews > 0:
            return total_rating / number_of_reviews
        else:
            return None  



restaurant1 = Restaurant("")

customer1 = Customer("", "")
review1 = Review(customer1, restaurant1, 5)
restaurant1._reviews.append(review1)  

customer2 = Customer("", "")
review2 = Review(customer2, restaurant1, 4)
restaurant1._reviews.append(review2)

print(restaurant1.reviews())  
print(restaurant1.customers())  
print(restaurant1.average_star_rating())  

