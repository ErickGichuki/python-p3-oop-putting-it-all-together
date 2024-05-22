#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count ):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, title):
        if isinstance(title, int):
            self._page_count = title

        else:
            print("page_count must be an integer")
