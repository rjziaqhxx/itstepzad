class Book:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price

    @property
    def title(self):
        return self._title
    
    @title.setter
    def tittle(self, value):
        if value is str:
            self._title = value
        else:
            raise ValueError('Tytul musi byc stringiem')
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if value is str:
            self._author = value
        else:
            raise ValueError('Autor musi byc stringiem')
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError('Cena musi byc dodatnia')
        
book = Book('A', 'B', 1)
print(book.author, book.title, book.price)
        
    
        