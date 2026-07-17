from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book:
    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        description: str,
        rating: int
    ):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [
    Book(1, "The Lord Of The Rings", "J.R.R. Tolkien", "A very short man embarks on a very long travel", "5"),
    Book(2, "The Two Towers", "J.R.R. Tolkien", "The short man gets lost", "5"),
    Book(3, "The Return Of The King", "J.R.R. Tolkien", "The short man arrives at the destination, another man is named king", "5"),
    Book(4, "One", "Myself", "One book", "1"),
    Book(5, "Two", "Also me", "The continuation of One", "2"),
    Book(6, "Three", "Not me, but also me", "1 + 2 = 3", "3"),
]


@app.get("/")
async def home():
    return {"message": "This is home"}


@app.get("/books")
async def get_books():
    return BOOKS


@app.post("/new_book")
async def post_books(new_book=Body()):
    BOOKS.append(Book(
        new_book.get('id'),
        new_book.get('title'),
        new_book.get('author'),
        new_book.get('description'),
        new_book.get('rating'),
    ))


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(book_request)
