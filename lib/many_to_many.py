class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("author must be and instance of Author.")
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("book must be an instance of Book.")
        if type(date) == str:
            self.date = date
        else:
            raise Exception("date must be a string.")
        if type(royalties) == int:
            self.royalties = royalties
        else:
            raise Exception("royaltiess but be an integer.")
        Contract.all.append(self)

    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]