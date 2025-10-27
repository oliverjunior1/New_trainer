# class big bang
class big_bang:
    def __init__(self, character, comic_books):
        self.character = character
        self.comic_books = comic_books

    def __str__(self):
        return f"The character {self.character} has {self.comic_books} comic books in his bedroom."

Sheldon = big_bang("Sheldon", 25000)
Leonard = big_bang("Leonard", 19985)

print(Sheldon)
print(Leonard)