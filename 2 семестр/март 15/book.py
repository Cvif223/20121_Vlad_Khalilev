class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == "title" or key == "author":
            if isinstance(value, str):
                super().__setattr__(key, value)
            else:
                raise ValueError("неверный тип присваеваемых данных")
        elif key == "pages" or key == "year":
            if isinstance(value, int):
                super().__setattr__(key, value)
            else:
                raise ValueError("неверный тип присваеваемых данных")

b = Book("Amogus", "Jesse Pinkman", 1, 2)
b.title = "sadsadsa"  # Устанавливаем значение атрибута экземпляра
print(b.pages)  # Выводит: 1
