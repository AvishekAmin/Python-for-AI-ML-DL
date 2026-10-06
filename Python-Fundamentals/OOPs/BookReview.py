# Concept: Classes & Objects

class Book:
    def __init__(self, title, author, reviews):
        self.title = title
        self.author = author
        self.reviews = reviews

    def add_review(self, new_review):
        self.reviews.append(new_review)
        print(f"New review: '{new_review}' added successfully")

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        print(self.reviews)

book1 = Book(
    "Gitanjali", 
    "R. N. Tagore", 
    ["Nice!", "Good Story", "Best one"]
)

print(
    f"Book: {book1.title} Author: {book1.author}\n"
    f"Reviews: {book1.reviews}"
)

book1.add_review("Very good")
print(f"Total number of reviews: {book1.count_reviews()}")
book1.display_reviews()