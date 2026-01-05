from app.repository.book_db import BookRepository

class BookService():

    @staticmethod
    def list_books():
        return BookRepository.get_all()
        

    @staticmethod
    def get_book(book_id):
        book = BookRepository.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        return book
    
    @staticmethod
    def create_book(data):
        return BookRepository.create(data)
    
    @staticmethod
    def delete_book(book_id):
        book = BookRepository.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")
        
        return BookRepository.delete(book_id)