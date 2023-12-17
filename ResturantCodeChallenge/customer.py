from lib.review import Review


class Customer:
    _all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        Customer._all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls._all_customers

    def restaurants(self):
        return list(set(review.restaurant() for review in self._reviews))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls._all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls._all_customers if customer.given_name() == name]
    

customer1 = Customer("", "")
customer2 = Customer("", "")

print(customer1.full_name())  
customer1.set_given_name("")
print(customer1.full_name()) 

print(Customer.all())