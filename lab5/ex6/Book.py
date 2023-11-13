from LibraryItem import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre
