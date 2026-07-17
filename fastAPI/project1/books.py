from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "This is home"}

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book_title.lower() == book.get('title', '').lower():
            return book

    return (f'No book with title {book_title} found')


@app.get("/books/")
async def filter_by_category(category: str):
    books = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books.append(book)

    return books


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, cathegory: str):
    books = []
    for book in BOOKS:
        if book.get('cathegory').casefold() == cathegory.casefold() and\
                book.get('author').casefold() == book_author.casefold():
            books.append(book)

    return books


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get(
            'title'
        ).casefold():
            BOOKS[i] = updated_book
            break


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
