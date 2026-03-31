class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    #Add new review
    def add_review(self, review):
        self.reviews.append(review)
        print("Review added sucessfully")

    #Count review
    def count_review(self):
        return len(self.reviews)
    
    #Display all reviews
    def display_review(self):
        if(len(self.reviews) == 0):
            print("No reviews available")
        else:
            print(f"Reviews for {self.title}")
            for r in self.reviews:
                print("-", r)

book1 = Book("python", "karthik", )
book1.add_review("very useful book")
book1.display_review()