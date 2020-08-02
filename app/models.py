# app/models.py
from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), index=True, unique=True)
    last_name = db.Column(db.String(25), index=True, unique=True)
    author_id = db.relationship("AuthorBook", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author: {self.id} {self.first_name} {self.last_name}>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    description = db.Column(db.Text)
    book_id = db.relationship("AuthorBook", backref="book", lazy="dynamic")

    def __str__(self):
        return f"<Book: {self.id} {self.title} {self.desription[:100]}>"

class AuthorBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    authorbook_id = db.relationship("Borrowed", backref="author_book", lazy="dynamic")

    def __str__(self):
        return f"<AuthorBook: {self.id} {self.author_id} {self.book_id}>"

class Borrowed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_from = db.Column(db.Date)
    date_to = db.Column(db.Date)
    authorbook_id = db.Column(db.Integer, db.ForeignKey('author_book.id'))

    def __str__(self):
        return f"<Rented: {self.id} {self.date_from} {self.date_to}>"