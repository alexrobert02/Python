class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.item_id}")
        print(f"Status: {'Checked out' if self.checked_out else 'Available'}")

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not checked out.")
