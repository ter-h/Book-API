from app.db import get_connection

class BookRepository:

    @staticmethod
    def get_all():
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM books ORDER BY id")
                return cur.fetchall()
            
    @staticmethod
    def get_by_id(book_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM books WHERE id = %s", (book_id,)
                )
                return cur.fetchone()
            
    @staticmethod
    def create(data):
        query = """
            INSERT INTO books (title, author, year_published)
            VALUES (%s, %s, %s)
            RETURNING *
        """

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    query,
                    (data["title"], data["author"], data["year_published"])
                )
                conn.commit()
                return cur.fetchone()
            
    @staticmethod
    def delete(book_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM books WHERE id = %s RETURNING *",
                    (book_id,)
                )

                conn.commit()
                return cur.fetchone()