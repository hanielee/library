class Library:
    def __init__(self, inventory={}): #empty dictionary 
        self.inventory = inventory

    def fill_inventory(self):
        with open('books.txt') as f:
            book_list = f.read().splitlines()
        for book in book_list:
            self.inventory[book] = "on shelf"

    def add_book(self): #functionality: add function to append to file
        book = input("Enter book title: ").strip()
        self.inventory[book] = "on shelf" #add book with "on shelf" status by default
        with open('books.txt', "a") as f:
            f.write("\n" + book)
            f.close()
        self.print_inventory()

    def print_inventory(self):
        print(".・。.・゜✭・.・✫・゜・。..・。.・゜✭・.・✫・゜・。.")
        print("\nLibrary Inventory:")

        #create list of books on shelf/checked out iterating over dict with items() -> list of key/value (book, status) based on status
        on_shelf_books = [book for book, status in self.inventory.items() if status == "on shelf"] 
        checked_out_books = [book for book, status in self.inventory.items() if status == "checked out"]
        
        #print out on shelf/checked out books with count
        print("______________________________________")
        print(f"On Shelf ({len(on_shelf_books)}):")
        print("______________________________________")
        for book in on_shelf_books:
            print(book)
        print() #space for formatting
        print("______________________________________")
        print(f"Checked Out ({len(checked_out_books)}):")
        print("______________________________________")
        for book in checked_out_books:
            print(book)
        print() #space for formatting

    def change_status(self):
        self.print_inventory()
        book = input("Enter book title: ").strip()
        book_lower = book.lower() #convert book title to ignore whether upper/lower case
        found = False
        for title in self.inventory:
            if title.lower().strip() == book_lower:
                found = True
                if self.inventory[title] == "on shelf":
                    self.inventory[title] = "checked out"
                elif self.inventory[title] == "checked out":
                    self.inventory[book] = "on shelf"
                print()
                print(f"{title} is now [{self.inventory[title]}]")
                break
        if not found:
            print(f"{book} not found in inventory")

    def search_inventory(self):
        title = input("Enter search term: ").strip()
        found_books = []
        for book, status in self.inventory.items():
            if title.lower() in book.lower():
                found_books.append((book, status))
        if found_books:
            print()
            print(f"Books containing '{title}':")
            for book, status in found_books:
                print(f"{book}: [{status}]")
        else:
            print(f"No books containing '{title}' found in inventory")

    def run(self):
        options = {
            '1': self.print_inventory,
            '2': self.add_book,
            '3': self.change_status,
            '4': self.search_inventory,
            'q': lambda: print("Thank you for visiting the Library. Please run again.") or exit(),
        }
        first_run = True
        while True:
            if first_run: #print welcome message on first run of program
                print("Welcome to the Library!\n")
                first_run = False
            print()
            print(".・。.・゜✭・.・✫・゜・。..・。.・゜✭・.・✫・゜・。.")
            print("Enter '1' to print inventory")
            print("Enter '2' to add a book")
            print("Enter '3' to check out/return a book")
            print("Enter '4' to search inventory")
            print("Enter 'q' to quit")
            print(".・。.・゜✭・.・✫・゜・。..・。.・゜✭・.・✫・゜・。.")
            print()
            option = input("What would you like to do?\n")
            func = options.get(option)
            if func:
                func()
            else:
                print("Invalid option, please enter 1, 2, 3, 4, or q")

library = Library()
library.fill_inventory()
library.run()
