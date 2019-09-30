class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)


class PaperBook(Book):
    def __init__(self, title, author, numPages):
        Book.__init__(self, title, author)
        self.numPages = numPages


class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size


mybook = EBook('The Odyssey', 'Homer', 2)
mypaperbook = PaperBook('The Odyssey', 'Homer', 500)
print(mybook.size)
print(mypaperbook.numPages)