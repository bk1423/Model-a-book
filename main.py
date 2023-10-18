class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def display_book_info(self):
        print("Book Information:")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


def main():
    # Create a book object
    book1 = Book("Python Crash Course", "Eric Matthes", 25.99)

    # Display book information
    book1.display_book_info()


if __name__ == "__main__":
    main()
