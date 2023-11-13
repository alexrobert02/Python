from LibraryItem import LibraryItem


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number):
        super().__init__(title, publisher, item_id)
        self.issue_number = issue_number
